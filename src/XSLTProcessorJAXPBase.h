//
//  XSLTProcessorJAXPBase.h
//  TestXSLT
//
//  Created by Marc Liyanage on Mon Aug 18 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "XSLTProcessor.h"



@interface XSLTProcessorJAXPBase : XSLTProcessor {

}

- (NSString *) getJAXPProcessorName;


@end


// Java class declarations to keep the compiler happy

@interface JAXPWrapper : NSObject
{}
- (int)getErrorSource;
- (int)getErrorLine;
- (NSString *)getErrorMessage;
- (NSData *)getResult;
- (BOOL)transform:(NSString *)processorClassName :(NSData *)xml :(NSData *)xslt :(NSString *)parameters :(NSString *)baseUri;
@end

