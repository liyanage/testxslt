//
//  NSDocumentControllerNotificationCategory.h
//  TestXSLT
//
//  Created by Marc Liyanage on Sat Mar 29 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface AppDelegate : NSObject
{
	IBOutlet NSWindow* prefsWindow;
}

- (void)applicationWillTerminate:(NSNotification *)aNotification;

@end
