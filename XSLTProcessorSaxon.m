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


- (NSString *) getJAXPProcessorName {

	return @"com.icl.saxon.TransformerFactoryImpl";
	
}



@end
