//
//  XSL_FO_Renderer.m
//  TestXSLT
//
//  Created by Marc Liyanage on Tue Aug 19 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import "XSL_FO_Renderer.h"


@implementation XSL_FO_Renderer


- (NSData *)render:(NSData *)foData {

	FOPWrapper *fw = (FOPWrapper *)[[NSClassFromString(@"FOPWrapper") alloc] init];

	NSData *resultData = [fw convert:foData];
	
	// fixme: autorelease on resultData? creation on Java side?
	
	[fw release];
	
	//NSLog(@"data: %@", resultData);
	
	return resultData;
}



@end
