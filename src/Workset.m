//
//  Workset.m
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Mar 03 2002.
//  Copyright (c) 2001 __MyCompanyName__. All rights reserved.
//

#import "Workset.h"


@implementation Workset

+ (void)initialize {
	[Workset setKeys:[NSArray arrayWithObject:@"xmlCode"] triggerChangeNotificationsForDependentKey:@"hasXmlCode"];
	[Workset setKeys:[NSArray arrayWithObject:@"xsltCode"] triggerChangeNotificationsForDependentKey:@"hasXsltCode"];
	[Workset setKeys:[NSArray arrayWithObject:@"result"] triggerChangeNotificationsForDependentKey:@"hasResult"];
	[Workset setKeys:[NSArray arrayWithObject:@"resultFilename"] triggerChangeNotificationsForDependentKey:@"hasResultFilename"];
	[Workset setKeys:[NSArray arrayWithObject:@"xmlFilename"] triggerChangeNotificationsForDependentKey:@"hasXmlFilename"];
	[Workset setKeys:[NSArray arrayWithObject:@"xsltFilename"] triggerChangeNotificationsForDependentKey:@"hasXsltFilename"];

	[Workset setKeys:[NSArray arrayWithObject:@"result"] triggerChangeNotificationsForDependentKey:@"stringResult"];

}



- (id)init {
	
	self = [super init];
	if (!self) return nil;
	
	id defaults = [NSUserDefaults standardUserDefaults];
	
	[self setValue:[defaults stringForKey:@"templateXML"] forKey:@"xmlCode"];
	[self setValue:[defaults stringForKey:@"templateXSLT"] forKey:@"xsltCode"];

	[self setValue:nil forKey:@"resultFilename"];
	
	result = [[NSData alloc] init];
	parameterSet = [[ParameterSet alloc] init];

	return self;
	
}


- (NSArray *)coderKeys {
	return [NSArray arrayWithObjects:
		@"xmlCode",
		@"xsltCode",
		@"result",
		@"parameterSet",
		@"xmlFilename",
		@"xsltFilename",
		@"resultFilename",
		nil];
}


- (id)initWithCoder:(NSCoder *)coder {

	if (self = [super init]) {
		NSEnumerator *keys = [[self coderKeys] objectEnumerator];
		id key;
		while (key = [keys nextObject]) {
			[self setValue:[coder decodeObjectForKey:key] forKey:key];
		}
	}
	return self;

}


- (void)encodeWithCoder:(NSCoder *)coder {

	NSEnumerator *keys = [[self coderKeys] objectEnumerator];
	id key;
	while (key = [keys nextObject]) {
		[coder encodeObject:[self valueForKey:key] forKey:key];
	}

}


- (void)dealloc {

	[xmlCode release];
	[xsltCode release];
	[result release];
	[parameterSet release];


	[super dealloc];

//	NSLog(@"Workset dealloc");

}


- (BOOL)hasXmlFilename {
	return xmlFilename != nil;
}

- (BOOL)saveXml {

	if (![self hasXmlFilename]) {
		return FALSE;
	}
	
	[[XMLUtils getDataWithEncodingFromString:xmlCode] writeToFile:xmlFilename atomically:NO];
	[self updateXmlFileModificationDate];

	return YES;
	
}

- (BOOL)xmlModifiedExternally {

	NSDictionary *fileAttr;

	if (![self hasXmlFilename]) {
		return FALSE;
	}

	fileAttr = [[NSFileManager defaultManager] fileAttributesAtPath:xmlFilename traverseLink:YES];

	if (fileAttr == nil || xmlFileModificationDate == nil) {
		return FALSE;
	}

	if (![xmlFileModificationDate isEqualToDate:[fileAttr objectForKey:NSFileModificationDate]]) {
		return TRUE;
	}

	return FALSE;
	
}

- (void)updateXmlFileModificationDate {

	NSDictionary *fileAttr;

	if ([self hasXmlFilename]) {
		fileAttr = [[NSFileManager defaultManager] fileAttributesAtPath:xmlFilename traverseLink:YES];
		[xmlFileModificationDate release];
		xmlFileModificationDate = [fileAttr objectForKey:NSFileModificationDate];
		[xmlFileModificationDate retain];
//		NSLog(@"xml file mod date: %@", xmlFileModificationDate);
	}

}

- (void)reloadXmlFromFile {
	[self setValue:[XMLUtils getStringWithEncodingFromFile:xmlFilename] forKey:@"xmlCode"];
	[self updateXmlFileModificationDate];
}





- (int)resultEncoding {
	return resultEncoding;
}

- (void)setResultEncoding:(NSStringEncoding)newencoding {
	resultEncoding = newencoding;
}



- (BOOL)hasXsltFilename {
	return xsltFilename != nil;
}

- (BOOL)saveXslt {

	if (![self hasXsltFilename]) {
		return FALSE;
	}

	[[XMLUtils getDataWithEncodingFromString:xsltCode] writeToFile:xsltFilename atomically:NO];
	[self updateXsltFileModificationDate];

	return YES;

}

- (BOOL)xsltModifiedExternally {

	NSDictionary *fileAttr;

	if (![self hasXsltFilename]) {
		return FALSE;
	}

	fileAttr = [[NSFileManager defaultManager] fileAttributesAtPath:xsltFilename traverseLink:YES];

	if (fileAttr == nil || xsltFileModificationDate == nil) {
		return FALSE;
	}

	if (![xsltFileModificationDate isEqualToDate:[fileAttr objectForKey:NSFileModificationDate]]) {
		return TRUE;
	}

	return FALSE;

}

- (void)updateXsltFileModificationDate {

	NSDictionary *fileAttr;

	if ([self hasXsltFilename]) {
		fileAttr = [[NSFileManager defaultManager] fileAttributesAtPath:xsltFilename traverseLink:YES];
		[xsltFileModificationDate release];
		xsltFileModificationDate = [fileAttr objectForKey:NSFileModificationDate];
		[xsltFileModificationDate retain];
//		NSLog(@"xslt file mod date: %@", xsltFileModificationDate);
	}
}

- (void)reloadXsltFromFile {
	[self setValue:[XMLUtils getStringWithEncodingFromFile:xsltFilename] forKey:@"xsltCode"];
	[self updateXsltFileModificationDate];
}


- (BOOL)hasResultFilename {
	return resultFilename != nil;
}


- (NSString *)stringResult {
	return [[[NSString alloc] initWithData:result encoding:[self resultEncoding]] autorelease];
}

- (void)saveResult {
	
	if (![self hasResultFilename]) {
		NSLog(@"saveResult called but no filename is available");
		return;
	}
	[result writeToFile:resultFilename atomically:NO];
}


- (BOOL)hasXmlCode {
	return ([xmlCode length] > 0);
}

- (BOOL)hasXsltCode {
	return ([xsltCode length] > 0);
}

- (BOOL)hasResult {
	return ([result length] > 0);
}

- (BOOL)hasParameters {
	return ([parameterSet count] > 0);
}





@end
