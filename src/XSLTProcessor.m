//
//  XSLTProcessor.m
//  TestXSLT
//
//  Created by Marc Liyanage on Thu Aug 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import "XSLTProcessor.h"


@implementation XSLTProcessor

- (id)init {

	if (self = [super init]) {
		[self clearResult];
		[self clearError];
		baseUri = nil;
	}

	return self;

}



- (void)setError:(NSString *)message atLine:(int)line inSource:(int)source {

	errorOccurred = YES;

	[message retain];
	[errorMessage release];
	errorMessage = message;
	errorLine = line;
	errorSource = source;

}

- (BOOL)errorOccurred {

	return errorOccurred;

}


- (void)clearError {

	errorOccurred = NO;

	[errorMessage release];
	errorMessage = @"";
	errorLine = 0;
	errorSource = 0;

}


- (void)clearResult {

	[result autorelease];
	result = nil;

}


- (NSData *)result {

	return result;

}

- (void)setResult:(NSData *)newResult {

	[newResult retain];
	[result autorelease];
	result = newResult;

}

- (int)resultEncoding {
	return resultEncoding;
}

- (void)setResultEncoding:(NSStringEncoding)newencoding {

	resultEncoding = newencoding;
}


- (void)setResultEncodingFromData:(NSData *)data {

	NSStringEncoding dataencoding = getEncodingFromXmlDecl((char *)[data bytes], [data length]);

	if (dataencoding == 0)
		dataencoding = NSUTF8StringEncoding;

	[self setResultEncoding:dataencoding];

}

- (NSString *)stringResult {
	return [[[NSString alloc] initWithData:result encoding:[self resultEncoding]] autorelease];
}

- (int)errorLine {

	return errorLine;
	
}


- (int)errorSource {

	return errorSource;

}

- (void)setErrorSource:(int)newSource {

	errorSource = newSource;

}

- (NSString *)errorMessage {

	return errorMessage;
	
}

- (void)setBaseUri:(NSString *)uri {

	[uri retain];
	[baseUri release];
	baseUri = uri;
}

- (NSString *)baseUri {
	return baseUri;
}


- (int)processorType {

	NSLog(@"Subclasses must override this method!");
	return 0;
	
}



- (BOOL)processStrings:(NSData *)xmlCode withXslt:(NSData *)xsltCode andParameters:(const char **)params {

	NSLog(@"Subclasses must override this method!");
	return NO;
}





@end
