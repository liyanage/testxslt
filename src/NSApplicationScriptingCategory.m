//
//  NSApplicationScriptingCategory.m
//  AETest
//
//  Created by Marc Liyanage on Thu Jul 04 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//
// $Id$


#import "NSApplicationScriptingCategory.h"


@implementation NSApplication(Scripting)

- (id)handleCreateScriptCommand:(NSScriptCommand*)command
{
//	NSLog(@"Create...");

	[[NSDocumentController sharedDocumentController] newDocument:nil];

	return nil;
}

@end
