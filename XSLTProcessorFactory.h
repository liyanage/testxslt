//
//  XSLTProcessorFactory.h
//  TestXSLT
//
//  Created by Marc Liyanage on Thu Aug 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "XSLTProcessor.h"
#import "XSLTProcessorSablotron.h"
#import "XSLTProcessorLibxslt.h"
#import "XSLTProcessorSaxon.h"
#import "XSLTProcessorXalan_J.h"


@interface XSLTProcessorFactory : NSObject {

	
}


+ (XSLTProcessor *)makeProcessorOfType:(int)processorType;





@end
