//
//  XSLTProcessorSaxon.h
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Jun 08 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "XSLTProcessor.h"


@interface XSLTProcessorSaxon : XSLTProcessor {

}

@end


// Java class declarations to keep the compiler happy

@interface JAXPWrapper : NSObject
{}
- (int)getErrorSource;
- (int)getErrorLine;
- (NSString *)getErrorMessage;
- (NSString *)getResult;
- (BOOL)transform:(NSString *)processorClassName :(NSString *)xml :(NSString *)xslt :(NSString *)parameters :(NSString *)baseUri;
@end



