//
//  TabViewDraggingCategory.m
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Oct 26 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

#import "TabViewDraggingCategory.h"


@implementation NSTabView (DraggingCategory)

- (NSDragOperation)draggingUpdated:(id)dragInfo {

	NSPoint mouse = [self convertPoint:[dragInfo draggingLocation] fromView:nil];
	
	NSTabViewItem *hitItem = [self tabViewItemAtPoint:mouse];
	NSString *identifier = [hitItem identifier];

	if (hitItem && ([identifier isEqualToString:@"xmlTab"] || [identifier isEqualToString:@"xsltTab"])) {
		[self selectTabViewItem:hitItem];
	}
	
	return NSDragOperationGeneric;
	
}

- (NSDragOperation)draggingEntered:(id)dragInfo {
	
	return NSDragOperationGeneric;
	
}


@end
