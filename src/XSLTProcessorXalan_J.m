//
//  XSLTProcessorXalan_J.m
//  TestXSLT
//
//  Created by Marc Liyanage on Mon Aug 18 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import "XSLTProcessorXalan_J.h"


@implementation XSLTProcessorXalan_J


- (int)processorType {
	
	return PROCESSORTYPE_XALAN_J;
	
}


- (NSString *) getJAXPProcessorName {
	
	return @"org.apache.xalan.processor.TransformerFactoryImpl";
	
}


@end
