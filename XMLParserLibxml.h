//
//  XMLParserLibxml.h
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Aug 04 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>

#include "libxml/parser.h"

extern void *xmlGenericErrorContext;

@interface XMLParserLibxml : NSObject {

	xmlParserCtxtPtr xmlContext;
	xmlDocPtr parsedXmlDoc;
	NSMutableString *errorMessage;
	int errorLine;
	BOOL errorOccurred;
	NSString *baseUri;

}


void makeUnixLineFeeds(char *buffer);

- (BOOL)parseString:(NSString *)xmlCode;
- (BOOL)checkWellFormedString:(NSString *)xmlCode;
- (void)setErrorMessage:(NSString *)message;
- (void)appendErrorMessage:(NSString *)message;
- (void)markFirstErrorLine;
- (NSString *)errorMessage;
- (void)clearError;
- (void)setError:(NSString *)message atLine:(int)line;
- (xmlDocPtr)nativeDoc;

- (void)setBaseUri:(NSString *)uri;
- (NSString *)baseUri;

- (int)errorLine;

void XMLParserLibxml_xmlErrorHandler(id self, const char *message, ...);
void XMLParserLibxml_xmlErrorHandler2(id self, const char *message, ...);


@end
