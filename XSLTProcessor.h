//
//  XSLTProcessor.h
//  TestXSLT
//
//  Created by Marc Liyanage on Thu Aug 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#include "ragel_xmldeclscanner.h"


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

	NSData *result;

	NSString *errorMessage;
	NSString *baseUri;
	int errorLine;
	int errorSource;
	BOOL errorOccurred;
	NSStringEncoding resultEncoding;
	
}


- (void)setError:(NSString *)message atLine:(int)line inSource:(int)source;
- (void)clearError;
- (BOOL)errorOccurred;
- (int)errorLine;
- (int)errorSource;
- (void)setErrorSource:(int)newSource;
- (NSString *)errorMessage;
- (int)resultEncoding;
- (void)setResultEncoding:(NSStringEncoding)encoding;
- (void)setResultEncodingFromData:(NSData *)data;

- (BOOL)processStrings:(NSData *)xmlCode withXslt:(NSData *)xsltCode andParameters:(const char **)params;

- (void)setBaseUri:(NSString *)uri;
- (NSString *)baseUri;

- (void)clearResult;
- (NSData *)result;
- (NSString *)stringResult;
- (void)setResult:(NSData *)newResult;
- (int)processorType;


@end
