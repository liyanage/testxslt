//
//  XSLTProcessorSaxon.m
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Jun 08 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import "XSLTProcessorSaxon.h"


@implementation XSLTProcessorSaxon


- (int)processorType {

	return PROCESSORTYPE_SAXON;

}



- (BOOL)processStrings:(NSString *)xmlCode withXslt:(NSString *)xsltCode andParameters:(const char **)params {

	[self clearError];

	NSString *jaxpBaseUri = @"";
	if ([self baseUri] != nil) {
		jaxpBaseUri = [self baseUri];
	}
	
	
	NSMutableString *paramBuffer = [[NSMutableString alloc] init];
	int i = 0;
	while (params && params[i]) {

		[paramBuffer appendString:[NSString stringWithFormat:@"%s==_=!=_==%s", params[i], params[i+1]]];

		if (params[i+2]) {
			// more parameters to follow
			[paramBuffer appendString:@"--_-!-_--"];
		}
		
		i += 2;
	}
	
	JAXPWrapper *jw = (JAXPWrapper *)[[NSClassFromString(@"JAXPWrapper") alloc] init];
	BOOL swresult = [jw transform:@"com.icl.saxon.TransformerFactoryImpl" :xmlCode :xsltCode :paramBuffer :jaxpBaseUri];
	
	
	
	if (swresult) {
		[self setResult:[jw getResult]];
	} else {
		[self setError:[jw getErrorMessage] atLine:[jw getErrorLine] inSource:[jw getErrorSource]];	
	}
	
		
	[jw release];
	
	return ![self errorOccurred];

}





@end
