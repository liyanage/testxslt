//
//  XMLUtils.m
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Aug 31 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import "XMLUtils.h"


@implementation XMLUtils


+ (NSString *)getStringWithEncodingFromFile:(NSString *)filename {
	
	NSStringEncoding encoding;
	NSString *fileString;
	
	NSData *fileContents = [NSData dataWithContentsOfFile:filename];
	if (fileContents == nil) {
		return @"Unable to load file!";
	}
	
	encoding = getEncodingFromXmlDecl([fileContents bytes], [fileContents length]);
	
	if (encoding == 0)
		encoding = [NSString defaultCStringEncoding];
	
	NSLog(@"picked encoding: %d", encoding);
	
	
	fileString = [[[NSString alloc] initWithData:fileContents encoding:encoding] autorelease];
	
	if (fileString)
		return fileString;
	
	if (encoding == NSUTF8StringEncoding) {
		return @"Unable to load file, possibly invalid UTF-8 contents!";
	} else {
		return @"Unable to load file!";
	}
	
}



+ (NSData *)getDataWithEncodingFromString:(NSString *)text {
	
	NSStringEncoding encoding;
	
	encoding = getEncodingFromXmlDecl([text UTF8String], [text length]);
	
	if (encoding == 0)
		encoding = NSUTF8StringEncoding;
	
//	NSLog(@"Default output encoding UTF-8 used...");

	return [text dataUsingEncoding:encoding allowLossyConversion:YES];

}





@end
