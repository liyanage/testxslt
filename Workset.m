//
//  Workset.m
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Mar 03 2002.
//  Copyright (c) 2001 __MyCompanyName__. All rights reserved.
//

#import "Workset.h"


@implementation Workset

- (id)init {
	
	if (self = [super init]) {
		xmlCode = [[NSString stringWithFormat:@"<text>\nPut your XML code here.\nPut your XSLT code under the XSLT tab.\nThen click on the Process button.\n</text>"] retain];
		xsltCode = [[NSString stringWithFormat:@"<?xml version='1.0' encoding='iso-8859-1'?>\n\n<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>\n\n<xsl:output method='html' version='1.0' encoding='iso-8859-1' indent='no'/>\n\n</xsl:stylesheet>"] retain];
		result = [[NSData alloc] init];
		parameterSet = [[ParameterSet alloc] init];
		xmlFilename = nil;
		xsltFilename = nil;
		resultFilename = nil;
	}
//	NSLog(@"Workset init");
	return self;
	
}

- (id)initWithCoder:(NSCoder *)coder {

	if (self = [super init]) {
		[self setXmlCode:[coder decodeObject]];
		[self setXsltCode:[coder decodeObject]];
		[self setResult:[coder decodeObject]];
		[self setParameterSet:[coder decodeObject]];
		[self setXmlFilename:[coder decodeObject]];
		[self setXsltFilename:[coder decodeObject]];
		[self setResultFilename:[coder decodeObject]];
		
	}
	return self;

}


- (void)encodeWithCoder:(NSCoder *)coder {

	[coder encodeObject:xmlCode];
	[coder encodeObject:xsltCode];
	[coder encodeObject:result];
	[coder encodeObject:parameterSet];
	[coder encodeObject:xmlFilename];
	[coder encodeObject:xsltFilename];
	[coder encodeObject:resultFilename];

}


- (void)dealloc {

	[xmlCode release];
	[xsltCode release];
	[result release];
	[parameterSet release];


	[super dealloc];

//	NSLog(@"Workset dealloc");

}

- (NSString *)xmlCode {
	return xmlCode;
}

- (void)setXmlCode:(NSString *)s {
	[s retain];
	[xmlCode release];
	xmlCode = s;
}






- (NSString *)xmlFilename {
	return xmlFilename;
}

- (void)setXmlFilename:(NSString *)s {

	[s retain];
	[xmlFilename release];
	xmlFilename = s;

	[self updateXmlFileModificationDate];
}

- (BOOL)hasXmlFilename {
	return xmlFilename != nil;
}

- (BOOL)saveXml {

	if (![self hasXmlFilename]) {
		return FALSE;
	}
	
	[[XMLUtils getDataWithEncodingFromString:[self xmlCode]] writeToFile:[self xmlFilename] atomically:NO];
	[self updateXmlFileModificationDate];

	return YES;
	
}

- (BOOL)xmlModifiedExternally {

	NSDictionary *fileAttr;

	if (![self hasXmlFilename]) {
		return FALSE;
	}

	fileAttr = [[NSFileManager defaultManager] fileAttributesAtPath:[self xmlFilename] traverseLink:YES];

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
		fileAttr = [[NSFileManager defaultManager] fileAttributesAtPath:[self xmlFilename] traverseLink:YES];
		[xmlFileModificationDate release];
		xmlFileModificationDate = [fileAttr objectForKey:NSFileModificationDate];
		[xmlFileModificationDate retain];
//		NSLog(@"xml file mod date: %@", xmlFileModificationDate);
	}

}

- (void)reloadXmlFromFile {

	[self setXmlCode:[XMLUtils getStringWithEncodingFromFile:[self xmlFilename]]];
	[self updateXmlFileModificationDate];

}





- (int)resultEncoding {
	return resultEncoding;
}

- (void)setResultEncoding:(NSStringEncoding)newencoding {
	resultEncoding = newencoding;
}





- (NSString *)xsltFilename {
	return xsltFilename;
}

- (void)setXsltFilename:(NSString *)s {

	[s retain];
	[xsltFilename release];
	xsltFilename = s;

	[self updateXsltFileModificationDate];
	
}

- (BOOL)hasXsltFilename {
	return xsltFilename != nil;
}

- (BOOL)saveXslt {

	if (![self hasXsltFilename]) {
		return FALSE;
	}

	[[XMLUtils getDataWithEncodingFromString:[self xsltCode]] writeToFile:[self xsltFilename] atomically:NO];
	[self updateXsltFileModificationDate];

	return YES;

}

- (BOOL)xsltModifiedExternally {

	NSDictionary *fileAttr;

	if (![self hasXsltFilename]) {
		return FALSE;
	}

	fileAttr = [[NSFileManager defaultManager] fileAttributesAtPath:[self xsltFilename] traverseLink:YES];

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
		fileAttr = [[NSFileManager defaultManager] fileAttributesAtPath:[self xsltFilename] traverseLink:YES];
		[xsltFileModificationDate release];
		xsltFileModificationDate = [fileAttr objectForKey:NSFileModificationDate];
		[xsltFileModificationDate retain];
//		NSLog(@"xslt file mod date: %@", xsltFileModificationDate);
	}
}

- (void)reloadXsltFromFile {

	[self setXsltCode:[XMLUtils getStringWithEncodingFromFile:[self xsltFilename]]];
	[self updateXsltFileModificationDate];
		
}





- (NSString *)resultFilename {
	return resultFilename;
}

- (void)setResultFilename:(NSString *)s {
	[s retain];
	[resultFilename release];
	resultFilename = s;
}

- (BOOL)hasResultFilename {
	return resultFilename != nil;
}




- (NSString *)xsltCode {
	return xsltCode;
}

- (void)setXsltCode:(NSString *)s {
	[s retain];
	[xsltCode release];
	xsltCode = s;
}

- (NSData *)result {
	return result;
}

- (void)setResult:(NSData *)s {
	[s retain];
	[result release];
	result = s;
}


- (NSString *)stringResult {
	return [[[NSString alloc] initWithData:result encoding:[self resultEncoding]] autorelease];
}



- (ParameterSet *)parameterSet {
	return parameterSet;
}

- (void)setParameterSet:(ParameterSet *)newParams {
	[newParams retain];
	[parameterSet release];
	parameterSet = newParams;
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
