//
//  XSLTProcessorSablotron.m
//  TestXSLT
//
//  Created by Marc Liyanage on Thu Aug 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import "XSLTProcessorSablotron.h"


@implementation XSLTProcessorSablotron



- (int)processorType {

	return PROCESSORTYPE_SABLOTRON;

}



+(BOOL)checkWellFormed:(NSString *)xmlCode {

	return NO;

}





- (id)init {

	if (self = [super init]) {

		[self clearResult];
		[self clearError];

		SablotCreateSituation(&S);
		SablotCreateProcessorForSituation(S, &processor);
		
		memset(&msgHandlerPtr, 0, sizeof(MessageHandler));

		msgHandlerPtr.makeCode = (MessageHandlerMakeCode *)rawMakeCodeHandler;
		msgHandlerPtr.log = (MessageHandlerLog *)rawLogHandler;
		msgHandlerPtr.error = (MessageHandlerError *)rawErrorHandler;
		SablotRegHandler(processor, HLR_MESSAGE, &msgHandlerPtr, self);

	}

	return self;

}




- (void)dealloc {

	SablotDestroyProcessor(processor);
	SablotDestroySituation(S);

	[super dealloc];
}











- (BOOL)processStrings:(NSString *)xmlCode withXslt:(NSString *)xsltCode andParameters:(const char **)params {

	char *resultBuffer;

	int resultCode = 0, i=0;


	[self clearError];


	if ([self baseUri] != nil) {
		SablotSetBase(processor, [[NSString stringWithFormat:@"%@/", [[self baseUri] stringByDeletingLastPathComponent]] cString]);
	}

	SablotAddArgBuffer(S, processor, "xslt", (char *)[xsltCode cString]);
	SablotAddArgBuffer(S, processor, "xml", (char *)[xmlCode cString]);

	while (params && params[i]) {
		SablotAddParam(S, processor, params[i], params[i+1]);
		i += 2;
	}

	
//	resultCode = SablotRunProcessor(processor, "arg:/xslt", "arg:/xml", "arg:/result", params, args);
	resultCode = SablotRunProcessorGen(S, processor, "arg:/xslt", "arg:/xml", "arg:/result");

	if ([self errorOccurred]) {
		return NO;
	}

	SablotGetResultArg(processor, "arg:/result", &resultBuffer);

	[self setResult:[NSString stringWithCString:resultBuffer]];
		 
	SablotFree(resultBuffer);

	return YES;
	
}



- (BOOL)processStringsOld:(NSString *)xmlCode withXslt:(NSString *)xsltCode andParameters:(const char **)params {

	char *resultBuffer;
	const char *args[7];

	int resultCode = 0;

	args[0] = "/xml";
	args[1] = (char *)[xmlCode cString];
	args[2] = "/xslt";
	args[3] = (char *)[xsltCode cString];
	args[4] = "/result";
	args[5] = (char *)&resultBuffer;
	args[6] = NULL;

	[self clearError];


	if ([self baseUri] != nil) {
		SablotSetBase(processor, [[self baseUri] cString]);
	}
	
	resultCode = SablotRunProcessor(processor, "arg:/xslt", "arg:/xml", "arg:/result", params, args);

	if ([self errorOccurred]) {
		return NO;
	}

	SablotGetResultArg(processor,"arg:/result", &resultBuffer);

	[self setResult:[NSString stringWithCString:resultBuffer]];
		 
	SablotFree(resultBuffer);

	return YES;
	
}



MH_ERROR rawErrorHandler(id self, SablotHandle processor_, MH_ERROR code, MH_LEVEL level, char **fields) {

	int i = 0;
	NSString *currentField;
	NSRange colonRange, keyRange, valueRange;
	NSString *key;
	NSString *value;

	NSString *errorMessage;
	int errorLine;
	int errorSource;

	for (i = 0; fields[i] != NULL; i++) {

		currentField = [NSString stringWithCString:fields[i]];

		colonRange = [currentField rangeOfString:@":"];
		keyRange = NSMakeRange(0, colonRange.location);
		valueRange = NSMakeRange(colonRange.location + 1, [currentField length] - (colonRange.location + 1));

		key = [currentField substringWithRange:keyRange];
		value = [currentField substringWithRange:valueRange];

		if ([key isEqual:@"msg"]) {
			errorMessage = value;
		}

		if ([key isEqual:@"line"]) {
			errorLine = [value intValue];
		}

		if ([key isEqual:@"URI"]) {

			if ([value isEqual:@"arg:/xml"]) {
				errorSource = XSLT_ERROR_SOURCE_XML;
			} else if ([value isEqual:@"arg:/xslt"]) {
				errorSource = XSLT_ERROR_SOURCE_XSLT;
			}
		}

	}

	[self setError:errorMessage atLine:errorLine inSource:errorSource];

	return 0;

}


MH_ERROR rawMakeCodeHandler(id self, SablotHandle processor_, int severity, unsigned short facility, unsigned short code) {

	//	NSLog(@"makeCode, proc %p, sev %d, fac %d, code %d", processor_, severity, facility, code);
	return 0;
}


MH_ERROR rawLogHandler(id self, SablotHandle processor_, MH_ERROR code, MH_LEVEL level, char **fields) {

	int i = 0;

	for (i = 0; fields[i] != NULL; i++) {
		//		NSLog(@"Sablotron Log: %s", fields[i]);
	}

	return 0;

}





@end
