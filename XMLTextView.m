//
//  XMLTextView.m
//  TestXSLT
//
//  Created by Marc Liyanage on Fri Aug 02 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import "XMLTextView.h"


@implementation XMLTextView


- (id)init {

	if (self = [super init]) {
		[self setRichText:NO];
	}

	return self;

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



-(void)pasteAsRichText:(id)sender {


	NSLog(@"paste as rich text");
	//	[self pasteAsPlainText:sender];

}




- (void)keyDown:(NSEvent *)event {

	NSRange selectedRange;
	
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

	[super keyDown:event];

}



- (BOOL)completeAfterSlash {

	NSRange selectedRange = [self selectedRange], tagNameRange;
	NSString *tagName = nil;

	tagNameRange = [self scanBackwardsForOpeningTagNameInRange:NSMakeRange(0, selectedRange.location - 1)];

	if (tagNameRange.location == NSNotFound) {
		return NO;
	}

	tagName = [[self string] substringWithRange:tagNameRange];
	
//	NSLog(@"completion!");

	if (tagName == nil) {
		return NO;
	}

	[self insertText:[NSString stringWithFormat:@"/%@>", tagName]];

	[self flashRange:tagNameRange];
		
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



- (void)complete:(id)sender {

	NSRange selectedRange, leftRange, rightRange, tagNameRange;
	NSString *tagName = nil;
	NSString *data = nil;
	int location;

	data = [self string];

	selectedRange = [self selectedRange];
	location = selectedRange.location;

	/* May not have a selection, and insertion point must be preceded by at
		* least one tag, which means at least 3 characters must be to its left
		*/
	if (selectedRange.length > 0 || location < 3) {
		NSBeep();
		return;
	}

	/* leftRange is everything from beginning of data to the insertion point.
		* rightRange is everything after the insertion point to the end of the data
		*/
	leftRange  = NSMakeRange(0, location);
	rightRange = NSMakeRange(location, [data length] - leftRange.length);



	tagNameRange = [self scanBackwardsForOpeningTagNameInRange:leftRange];

	if (tagNameRange.location == NSNotFound) {
		NSBeep();
		return;
	}

	tagName = [data substringWithRange:tagNameRange];
	
	[self insertText:[NSString stringWithFormat:@"</%@>", tagName]];
	[self setSelectedRange:selectedRange];

	[self flashRange:tagNameRange];
	
}



-(NSRange)scanBackwardsForOpeningTagNameInRange:(NSRange)scanRange {

	NSRange tagNameEndRange, tagContentPlusEndRange, leftAngleRange, openingTagRange, slashRange;
	NSCharacterSet *angleSet = [NSCharacterSet characterSetWithCharactersInString:@"<>"];
	NSCharacterSet *tagNameDelimiterSet = [NSCharacterSet characterSetWithCharactersInString:@" <>"];
	NSString *tagName = nil;
	NSString *data = [self string];
	NSString *character;
	NSRange tagNameRange;

	
	/* find the first occurence of angle brackets, both opening or closing,
	* in the range to the left of the insertion point, searching backwards
	* from the insertion point
	*/
	leftAngleRange = [data rangeOfCharacterFromSet:angleSet options:NSBackwardsSearch range:scanRange];

	/* abort unless we found something */
	if (leftAngleRange.location == NSNotFound) {
		return NSMakeRange(NSNotFound, 0);
	}

	//	NSLog(@"leftbracket: %d %d", leftAngleRange.location, leftAngleRange.length);


	/* We expect the nearest angle bracket to our left to be a closing one, we will
		* not try to complete an open tag if we find an opening bracket instead.
		*/
	character = [data substringWithRange:leftAngleRange];
	if (![character isEqual:@">"]) {
		return NSMakeRange(NSNotFound, 0);
	}

	/* shift end of scanRange so it ends after the closing angle bracket we just found */
	scanRange = NSMakeRange(0, leftAngleRange.location);


	/* Now search again from the end of that range backward to the beginning of the data
		* and look for another angle bracket.
		*/
	leftAngleRange = [data rangeOfCharacterFromSet:angleSet options:NSBackwardsSearch range:NSMakeRange(0, scanRange.length - 1)];

	/* again abort unless we found something */
	if (leftAngleRange.location == NSNotFound) {
		return NSMakeRange(NSNotFound, 0);
	}

	//NSLog(@"leftbracket: %d %d", leftAngleRange.location, leftAngleRange.length);

	/* This time we expect to see an opening angle bracket */
	character = [data substringWithRange:leftAngleRange];
	if (![character isEqual:@"<"]) {
		return NSMakeRange(NSNotFound, 0);
	}


	/* This will indicate the range of the entire nearest tag to our left,
		* we assume that's the opening tag */
	openingTagRange = NSMakeRange(leftAngleRange.location, (scanRange.length - leftAngleRange.location) + 1);

	/* check if it is indeed an opening tag, i.e. no slash after the opening bracket */
	slashRange = NSMakeRange(openingTagRange.location + 1, 1);
	character = [data substringWithRange:slashRange];
	if ([character isEqual:@"/"]) {
		return NSMakeRange(NSNotFound, 0);
	}

	/* Don't complete processing instructions, comments etc. */
	if ([character isEqual:@"?"] || [character isEqual:@"!"]) {
		return NSMakeRange(NSNotFound, 0);
	}
	
	
	/* check if it is a merged start and end tag, i.e. slash before closing bracket */
	slashRange = NSMakeRange((openingTagRange.location + openingTagRange.length) - 2, 1);
	character = [data substringWithRange:slashRange];
	if ([character isEqual:@"/"]) {
		return NSMakeRange(NSNotFound, 0);
	}


	tagContentPlusEndRange = NSMakeRange(openingTagRange.location + 1, openingTagRange.length - 1);

	//NSLog(@"tagcontent: %d %d", tagContentPlusEndRange.location, tagContentPlusEndRange.length);

	tagNameEndRange = [data rangeOfCharacterFromSet:tagNameDelimiterSet options:0 range:tagContentPlusEndRange];


	tagNameRange = NSMakeRange(tagContentPlusEndRange.location, tagNameEndRange.location - tagContentPlusEndRange.location);

	tagName = [data substringWithRange:tagNameRange];

	if ([tagName length] < 1) {
		return NSMakeRange(NSNotFound, 0);
	}


	return tagNameRange;
	
	//NSLog(@"tagrange: %d %d / %@", tagNameEndRange.location, tagNameEndRange.length, tagName);

	





}




@end
