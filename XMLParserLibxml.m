//
//  XMLParserLibxml.m
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Aug 04 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import "XMLParserLibxml.h"


@implementation XMLParserLibxml


- (id)init {

	if (self = [super init]) {

		errorMessage = [[NSMutableString alloc] init];
		errorLine = 0;
		errorOccurred = NO;
		//xmlContext = malloc(sizeof(xmlParserCtxt));
		//bzero(xmlContext, sizeof(xmlParserCtxt));
		parsedXmlDoc = NULL;
		baseUri = NULL;
		
	}
	
	return self;
}


- (xmlDocPtr)nativeDoc {

	return parsedXmlDoc;
	
}

- (void)dealloc {

	[errorMessage release];
	[baseUri release];

	if (parsedXmlDoc) {
		xmlFreeDoc(parsedXmlDoc);
//		free(xmlContext);
	}

	
}




- (void)setErrorMessage:(NSString *)message {

	[errorMessage setString:message];

}

- (int)errorLine {

	return errorLine;

}

- (NSString *)errorMessage {

	return errorMessage;

}


- (void)setErrorOccurred:(BOOL)flag {

	errorOccurred = flag;
	
}

- (void)appendErrorMessage:(NSString *)message {

	if ([errorMessage length] > 0) {
		[errorMessage appendString:@"\n"];
	}
	[errorMessage appendString:[message substringWithRange:NSMakeRange(0, [message length] - 1)]];
	[self setErrorOccurred:YES];

}

- (BOOL)errorOccurred {

	return errorOccurred;

}


- (void)setError:(NSString *)message atLine:(int)line {

	[self setErrorMessage:message];
	errorLine = line;
	[self setErrorOccurred:YES];
	

}


- (void)clearError {

	[errorMessage setString:@""];
	[self setErrorOccurred:NO];
	errorLine = 0;

}


void makeUnixLineFeeds(char *buffer) {

	int i = 0;

	while (buffer[i] != '\0') {

		if (buffer[i] == '\r') {
			if (buffer[i + 1] == '\n') {
				i++;
			} else {
				buffer[i] = '\n';
			}
		}
		i++;
	}
	
}


- (BOOL)checkWellFormedData:(NSData *)xmlCode {

	/*
	// fixme: using nsdata now, not null-terminated. maybe replace with expat.
	return YES;
	char *xmlString = (char *)[xmlCode bytes];
	//const char *xmlString = [stringData bytes];
	int error = 0;

	makeUnixLineFeeds(xmlString);
	
	/*
	NSData *stringData = [xmlCode dataUsingEncoding:NSUTF8StringEncoding];
	NSData *stringData = [xmlCode dataUsingEncoding:NSISOLatin1StringEncoding];


	 xmlString = malloc([stringData length] + 1);
	[stringData getBytes:xmlString];
	xmlString[[stringData length]] = '\0';
	 */
		

//	xmlContext = xmlCreateDocParserCtxt(xmlString);
	/*
	if (!xmlContext) {
		return NO;
	}


	[self clearError];
	xmlSetGenericErrorFunc(self, (xmlGenericErrorFunc)XMLParserLibxml_xmlErrorHandler);

	error = xmlParseDocument(xmlContext);

	if (xmlContext->myDoc) {
		xmlFreeDoc(xmlContext->myDoc);
	}

	xmlFreeParserCtxt(xmlContext);
	xmlContext = NULL;

	if (error != XML_ERR_OK) {
		return NO;
	} else {
		[self clearError];
		return YES;
	}

*/
	 
}




- (BOOL)parseData:(NSData *)xmlCode {

	int error = 0;

//	makeUnixLineFeeds(xmlString);

    xmlSubstituteEntitiesDefault(1);
	xmlLoadExtDtdDefaultValue = 1;

	[self clearError];
	xmlSetGenericErrorFunc(self, (xmlGenericErrorFunc)XMLParserLibxml_xmlErrorHandler);

	if (parsedXmlDoc) {
		xmlFreeDoc(parsedXmlDoc);
	}
	
	parsedXmlDoc = xmlParseMemory([xmlCode bytes], [xmlCode length]);

	if (!parsedXmlDoc) {
		return NO;
	}
	
	if ([self baseUri] != nil) {
		xmlNodeSetBase((xmlNodePtr)parsedXmlDoc, (xmlChar *)[[self baseUri] cString]);
	}
	[self clearError];
	return YES;

		
}



- (void)markFirstErrorLine {

//	if (errorLine == 0 && xmlContext && xmlContext->input) {
//		errorLine = xmlContext->input->line;
//	}

	
}

void XMLParserLibxml_xmlErrorHandler(id self, const char *message, ...) {

	char *messageData;
	va_list args;


	
	[self markFirstErrorLine];

	/* we're only interested in messages with the format string "%s" */
	if (strcmp(message, "%s")) {
		return;
	}

	va_start(args, message);
	messageData = va_arg(args, char *);

	[self appendErrorMessage:[NSString stringWithCString:messageData]];

    va_end(args);


}


void XMLParserLibxml_xmlErrorHandler2(id self, const char *message, ...) {

	const char *end = message + (strlen(message) - 1);
	char *pos = (char *)message;
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

//	NSLog(@"xml error handler: %s", message);

	va_start(args, message);

	while (pos <= end) {

		if (!strncmp(pos, "%s", 2)) {
			va_arg(args, char *);
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
	[self setError:errorMessage atLine:errorLine];


}


- (void)setBaseUri:(NSString *)uri {

	[uri retain];
	[baseUri release];
	baseUri = uri;
}

- (NSString *)baseUri {
	return baseUri;
}



@end
