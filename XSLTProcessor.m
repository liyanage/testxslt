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


- (NSString *)result {

	return result;

}

- (void)setResult:(NSString *)newResult {

	[newResult retain];
	[result autorelease];
	result = newResult;

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



- (BOOL)processStrings:(NSString *)xmlCode withXslt:(NSString *)xsltCode andParameters:(const char **)params {

	NSLog(@"Subclasses must override this method!");
	return NO;
}





@end
