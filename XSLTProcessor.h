//
//  XSLTProcessor.h
//  TestXSLT
//
//  Created by Marc Liyanage on Thu Aug 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>


enum {
	XSLT_ERROR_SOURCE_XML = 1,
	XSLT_ERROR_SOURCE_XSLT,
};

enum {
	PROCESSORTYPE_SABLOTRON = 1,
	PROCESSORTYPE_LIBXSLT,
	PROCESSORTYPE_SAXON,
	PROCESSORTYPE_XALAN_J,
};



@interface XSLTProcessor : NSObject {

	NSString *result;

	NSString *errorMessage;
	NSString *baseUri;
	int errorLine;
	int errorSource;
	BOOL errorOccurred;
	
}


- (void)setError:(NSString *)message atLine:(int)line inSource:(int)source;
- (void)clearError;
- (BOOL)errorOccurred;
- (int)errorLine;
- (int)errorSource;
- (void)setErrorSource:(int)newSource;
- (NSString *)errorMessage;


- (BOOL)processStrings:(NSString *)xmlCode withXslt:(NSString *)xsltCode andParameters:(const char **)params;

- (void)setBaseUri:(NSString *)uri;
- (NSString *)baseUri;

- (void)clearResult;
- (NSString *)result;
- (void)setResult:(NSString *)newResult;
- (int)processorType;


@end
