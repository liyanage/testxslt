//
//  TabViewDraggingCategory.h
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Oct 26 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//


#import <Cocoa/Cocoa.h>
#import <AppKit/NSDragging.h>


@interface NSTabView (DraggingCategory)

- (NSDragOperation)draggingUpdated:(id)dragInfo;
- (NSDragOperation)draggingEntered:(id)dragInfo;

@end



