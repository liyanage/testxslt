//
//  XSLTProcessorFactory.m
//  TestXSLT
//
//  Created by Marc Liyanage on Thu Aug 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import "XSLTProcessorFactory.h"


@implementation XSLTProcessorFactory


+ (XSLTProcessor *)makeProcessorOfType:(int)processorType {

	if (processorType == PROCESSORTYPE_SABLOTRON) {
		return [[XSLTProcessorSablotron alloc] init];
	} else if (processorType == PROCESSORTYPE_LIBXSLT) {
		return [[XSLTProcessorLibxslt alloc] init];
	} else if (processorType == PROCESSORTYPE_SAXON) {
		return [[XSLTProcessorSaxon alloc] init];
	}

	NSLog(@"Unknown processor type '%d' passed!", processorType);
	return nil;

}



@end
