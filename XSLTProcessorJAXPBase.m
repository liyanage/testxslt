//
//  XSLTProcessorJAXPBase.m
//  TestXSLT
//
//  Created by Marc Liyanage on Mon Aug 18 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import "XSLTProcessorJAXPBase.h"


@implementation XSLTProcessorJAXPBase






- (BOOL)processStrings:(NSData *)xmlCode withXslt:(NSData *)xsltCode andParameters:(const char **)params {
	
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
	BOOL swresult = [jw transform:[self getJAXPProcessorName] :xmlCode :xsltCode :paramBuffer :jaxpBaseUri];
	
	[self setResultEncodingFromData:xsltCode];
	
	if (swresult) {
		[self setResult:[jw getResult]];
	} else {
		[self setError:[jw getErrorMessage] atLine:[jw getErrorLine] inSource:[jw getErrorSource]];	
	}
	
	
	[jw release];
	
	return ![self errorOccurred];
	
}


- (NSString *) getJAXPProcessorName {
	
	NSLog(@"subclass must override getJAXPProcessorName in XSLTProcessorJAXPBase!");
	return nil;
	
}



@end
