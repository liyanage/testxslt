//
//  XSLTProcessorLibxslt.m
//  TestXSLT
//
//  Created by Marc Liyanage on Thu Aug 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import "XSLTProcessorLibxslt.h"

#define MAX_PATHS 64


@implementation XSLTProcessorLibxslt

- (int)processorType {

	return PROCESSORTYPE_LIBXSLT;

}





- (BOOL)processStrings:(NSString *)xmlCode withXslt:(NSString *)xsltCode andParameters:(const char **)params {

	xmlChar *resultBuffer = NULL;
	int resultSize = 0;
	int bytesWritten = 0;

	XMLParserLibxml *xmlParser = [[[XMLParserLibxml alloc] init] autorelease];
	XMLParserLibxml *xsltParser = [[[XMLParserLibxml alloc] init] autorelease];

	if ([self baseUri] != nil) {
		[xsltParser setBaseUri:[self baseUri]];
	}

	xmlDocPtr resultDoc = NULL;
	xsltStylesheetPtr stylesheet = NULL;
	xsltTemplatePtr template = NULL;


	[self clearError];
	
	exsltRegisterAll();
	xsltRegisterTestModule();


	

	/* There might be a race condition here as the error handler seems to be set globally.
	 * Multiple Documents processing at the same time could interfere.
	 */
	xsltSetGenericErrorFunc(self, (xmlGenericErrorFunc)xsltErrorHandler);
	while (1) {

		if (![xmlParser parseString:xmlCode]) {
			[self setError:[xmlParser errorMessage] atLine:[xmlParser errorLine] inSource:XSLT_ERROR_SOURCE_XML];
			break;
		}
		
		if (![xsltParser parseString:xsltCode]) {
			[self setError:[xsltParser errorMessage] atLine:[xsltParser errorLine] inSource:XSLT_ERROR_SOURCE_XSLT];
			break;
		}

		

		
		stylesheet = xsltParseStylesheetDoc([xsltParser nativeDoc]);

		if (!stylesheet) {
			[self setErrorSource:XSLT_ERROR_SOURCE_XSLT];
			break;
		}

		resultDoc = xsltApplyStylesheet(stylesheet, [xmlParser nativeDoc], params);
//		resultDoc = xsltProfileStylesheet(stylesheet, [xmlParser nativeDoc], params, stderr);

		if (!resultDoc) {
			[self setErrorSource:XSLT_ERROR_SOURCE_XSLT];
			break;
		}

		break;
	}


	if (![self errorOccurred]) {

		bytesWritten = xsltSaveResultToString(&resultBuffer, &resultSize, resultDoc, stylesheet);
		[self setResult:[NSString stringWithCString:resultBuffer]];


		/*
		template = stylesheet->templates;
		while (template != NULL) {

			if (template->match) {
				NSLog(@"match: %s", template->match);
			}

			if (template->name) {
				NSLog(@"name: %s", template->name);
			}

			if (template->mode) {
				NSLog(@"mode: %s", template->mode);
			}

			NSLog(@"count: %d", template->nbCalls);
			NSLog(@"time: %ld", template->time);

			template = template->next;
		}
		*/
		
		
	}
	
	if (resultDoc) {
		xmlFreeDoc(resultDoc);
	}

	if (resultBuffer) {
		free(resultBuffer);
	}

	return ![self errorOccurred];
}





void xsltErrorHandler(id self, const char *message, ...) {

	const char *end = message + (strlen(message) - 1);
	char *pos = (char *)message;
	char *errorstring = NULL;
	int errorLine = 0;
	NSString *errorMessage;
	char completeMessage[512];
	va_list args;

	/*	Do not overwrite previous error information so the
		first error in a series will be preserved
	 */
	if ([self errorOccurred]) {
		return;
	}


	NSLog(@"xslt error handler: %s", message);
	
	va_start(args, message);

	while (pos <= end) {

		if (!strncmp(pos, "%s", 2)) {
			errorstring = va_arg(args, char *);
		} else if (!strncmp(pos, "%d", 2)) {
			errorLine = va_arg(args, int);
		}

		pos++;

	}

    va_end(args);

	va_start(args, message);
	vsnprintf(completeMessage, 512, message, args);
    va_end(args);

	errorMessage = [NSString stringWithCString:completeMessage];
	[self setError:errorMessage atLine:errorLine inSource:0];


}










@end
