//
//  NSApplicationScriptingCategory.h
//  AETest
//
//  Created by Marc Liyanage on Thu Jul 04 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//
// $Id$


#import <Cocoa/Cocoa.h>

@interface NSApplication(Scripting)

- (id)handleCreateScriptCommand:(NSScriptCommand*)command;

@end
