//
//  XSL_FO_Renderer.h
//  TestXSLT
//
//  Created by Marc Liyanage on Tue Aug 19 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>


@interface XSL_FO_Renderer : NSObject {

}

- (NSData *)render:(NSString *)foString;

@end

// Java class declarations to keep the compiler happy

@interface FOPWrapper : NSObject
{}
/*
- (int)getErrorSource;
- (int)getErrorLine;
- (NSString *)getResult;
*/

- (NSString *)getErrorMessage;
- (BOOL)errorOccurred;
- (NSData *)convert:(NSString *)foString;

@end
