//
//  NSDocumentControllerNotificationCategory.m
//  TestXSLT
//
//  Created by Marc Liyanage on Sat Mar 29 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import "AppDelegate.h"

@implementation AppDelegate

- (void)applicationDidBecomeActive:(NSNotification *)aNotification {

	/* no longer active, now using the windowDidBecomeMain method in the window delegate (MyDocument.m)
	 */

	//	NSArray *documents = [[NSDocumentController sharedDocumentController] documents];
//	[documents makeObjectsPerformSelector:@selector(checkForExternalModifications)];
	
}

@end
