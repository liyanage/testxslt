//
//  XMLTextView.m
//  TestXSLT
//
//  Created by Marc Liyanage on Fri Aug 02 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import "XMLTextView.h"


@implementation XMLTextView



-(void)awakeFromNib {

	[self setRichText:NO];
	resultstack = NULL;
	defaults = [NSUserDefaults standardUserDefaults];
	
	// register our two input text views to receive file drags
	//
 //	[xmlView registerForDraggedTypes:[NSArray arrayWithObjects:NSFilenamesPboardType, nil]];
 //	[xsltView registerForDraggedTypes:[NSArray arrayWithObjects:NSFilenamesPboardType, nil]];
	
	NSFont *computerFont = [NSFont fontWithName:@"Courier" size:12.0];
	[self setFont:computerFont];
	
	[self setAllowsUndo:YES];
	
}


- (void)dealloc {
	
	if (resultstack)
		free(resultstack);
	[errorString release];
}

-(void)selectLineByNumber:(int)line {

	NSString *data = [self string];
	unsigned int i, startIndex, lineEndIndex;
	NSRange aRange;

	if (line == 0) {
		return;
	}


	aRange.location = 0;
	aRange.length = 0;

	for (i = 1; i <= line; i++) {

		[data getLineStart:&startIndex end:&lineEndIndex contentsEnd:nil forRange:aRange];
		aRange.location = lineEndIndex;

	}

	aRange.location = startIndex;
	aRange.length = lineEndIndex - startIndex;

	[self setSelectedRange:aRange];
	[self scrollRangeToVisible:aRange];

	
}





- (void)keyDown:(NSEvent *)event {

	NSRange selectedRange;
	
	if (![defaults boolForKey:@"enableSyntaxAnalysis"]) {
		[super keyDown:event];
		return;
	}
	
	if ([[event characters] isEqual:@"\033"]) {

		if ([event modifierFlags] || [event isARepeat]) {
			return;
		}
		[self complete:nil];
		return;

	} else if ([[event characters] isEqual:@"/"]) {

		selectedRange = [self selectedRange];
		if (selectedRange.location < 2 || selectedRange.length > 0) {
			[super keyDown:event];
			return;
		}

		if ([[[self string] substringWithRange:NSMakeRange(selectedRange.location - 1, 1)] isEqual:@"<"]) {
			if([self completeAfterSlash]) {
				return;
			}
		}
	}

	
	/*
	if ([event modifierFlags] & NSFunctionKeyMask) {
		[self didChangeText];
	}
	*/
	
	//NSFunctionKeyMask
	
	
	[super keyDown:event];

}



- (BOOL)completeAfterSlash {

	int location = [self selectedRange].location - 1;
	
	[self calculateTagStackAtLocation:location];
	
	if (stackresult) {
		return NO;
	}

	NSTextStorage *storage = [self textStorage];
	[storage beginEditing];
	[storage deleteCharactersInRange:NSMakeRange(location, 1)];
	[storage endEditing];

	[self setSelectedRange:NSMakeRange(location, 0)];

	[self complete:nil];

	
	return YES;
}



- (void)flashRange:(NSRange)range {

	NSRect tagNameRect;

	tagNameRect = [self firstRectForCharacterRange:range];

	tagNameRect.origin = [[self window] convertScreenToBase:tagNameRect.origin];

	tagNameRect = [self convertRect:tagNameRect fromView:[[self window] contentView]];


	[self lockFocus];
	[[[NSColor selectedControlColor] colorWithAlphaComponent:0.75] set];
/*
	NSFrameRectWithWidth(tagNameRect, 2);
 */
	[NSBezierPath fillRect:tagNameRect];
	[self unlockFocus];
	[[self window] flushWindow];

	usleep(100000);

	[self setNeedsDisplay:YES];

	
}

-(NSString *)calculateTagStack {

	return [self calculateTagStackAtLocation:[self selectedRange].location];
	
}

-(BOOL)checkWellFormed {

	int result;
	NSData *data = [XMLUtils getDataWithEncodingFromString:[self string]];

	parser = XML_ParserCreate(NULL);

	if (!parser) {
		NSLog(@"Unable to allocate expat parser in XMLTextView:checkWellFormed!");
		return NO;
	}

	result = XML_Parse(parser, [data bytes], [data length], 1);

	if (!result) {
		[self setError:[NSString stringWithFormat:@"%s, line %d, column %d", XML_ErrorString(XML_GetErrorCode(parser)), XML_GetCurrentLineNumber(parser), XML_GetCurrentColumnNumber(parser)] atLine:XML_GetCurrentLineNumber(parser) atColumn:XML_GetCurrentColumnNumber(parser)];
	} else if (error) {
		[self clearError];
	}
	
	XML_ParserFree(parser);
	
	return result > 0;
}



-(void)clearError {
	
	errorLine = errorColumn = 0;
	error = NO;
	[errorString release];
	errorString = @"";
	
}

-(BOOL)hasError {
	
	return error;
	
}
-(void)setError:(NSString *)errstring atLine:(int)line atColumn:(int)column {
	
	errorLine = line;
	errorColumn = column;
	error = YES;
	[errstring retain];
	[errorString release];
	errorString = errstring;
	
}







-(NSString *)calculateTagStackAtLocation:(int)location {

	char *buffer;
	int i;
	NSRange selectedRange;
	NSMutableString *mystack;

	if (![[NSUserDefaults standardUserDefaults] boolForKey:@"enableSyntaxAnalysis"]) {
		return @"";
	}
	
	buffer = [[self string] lossyCString];
	selectedRange = [self selectedRange];
	
	if (resultstack)
		free(resultstack);

	stackresult = 0;
	resultstack = findCompletion(buffer, strlen(buffer), location, &stackresult, tagpositions);

	mystack = [NSMutableString stringWithCapacity:1000];
	
	for (i = 0; resultstack && *(resultstack[i]); i++) {
		if (*(resultstack[i+1])) {
			[mystack appendFormat:@"%s/", resultstack[i]];
		} else {
			if (stackresult) {
				[mystack appendFormat:@"%s", resultstack[i]];
			} else {
				[mystack appendFormat:@"<%s>", resultstack[i]];
			}
			
			
		}

	}


	switch (stackresult) {
	
		case 1:
			[mystack appendString:@" (In tag)"];
			break;

		case 3:
			[mystack appendString:@" (In comment section)"];
			break;
		case 5:
			[mystack appendString:@" (In CDATA section)"];
			break;
			
		case 8:
			[mystack appendString:@" (No open tags)"];
			break;
			
		case 16:
			[mystack appendString:@" (Tags are balanced)"];
			break;
	}
	
	
	return mystack;
	
}

- (void)complete:(id)sender {

	NSRange selectedRange, tagNameRange;
	NSString *tagName = nil;
	int location, i;

//	data = [self string];

	selectedRange = [self selectedRange];
	location = selectedRange.location;

	/* May not have a selection, and insertion point must be preceded by at
		* least one tag, which means at least 3 characters must be to its left
		*/
	if (selectedRange.length > 0 || location < 3 || stackresult) {
		NSBeep();
		return;
	}


	for (i = 0; resultstack && *(resultstack[i]); i++) {
		if (!*(resultstack[i+1])) {
			tagName = [NSString stringWithCString:resultstack[i]];
			tagNameRange = NSMakeRange(tagpositions[i*2], tagpositions[i*2+1]- tagpositions[i*2]);
		}
	}
	

	[self insertText:[NSString stringWithFormat:@"</%@>", tagName]];
	[self setSelectedRange:selectedRange];

	[self flashRange:tagNameRange];
	[self calculateTagStack];
	
}





@end
