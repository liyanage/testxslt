//
//  XMLUtils.h
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Aug 31 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#include "ragel_xmldeclscanner.h"


@interface XMLUtils : NSObject {

}




+ (NSString *)getStringWithEncodingFromFile:(NSString *)filename;
+ (NSData *)getDataWithEncodingFromString:(NSString *)text;

@end
