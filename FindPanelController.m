//
//  FindPanelController.m
//  TestXSLT
//
//  Created by Marc Liyanage on Tue Aug 20 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import "FindPanelController.h"


@implementation FindPanelController

- (IBAction)findPrevious:(id)sender {

//	NSLog(@"Find Previous!");

	[self find:sender];
	[self setSearchFlags:NSBackwardsSearch | [self caseInsensitiveFlag]];
	
}

- (void)awakeFromNib {

	[self refresh];
}
	

- (IBAction)find:(id)sender {

//	NSLog(@"Find!");

	if ([[findField stringValue] length] > 0) {
		[self setFindString:[findField stringValue]];
	}
	
    [NSApp stopModal];
	[self setSearchFlags:0 | [self caseInsensitiveFlag]];


}


- (unsigned int)caseInsensitiveFlag {

	if ([caseInsensitiveCheckbox state] == NSOnState) {
		return NSCaseInsensitiveSearch;
	} else {
		return 0;
	}
}

- (void)setSearchFlags:(unsigned int)flags {

	searchFlags = flags;

}


- (unsigned int)searchFlags {

	return searchFlags;

}

- (IBAction)keyUp:(NSEvent *)event {

	BOOL state = [[findField stringValue] length] > 0;
	[nextButton setEnabled:state];
	[previousButton setEnabled:state];
	
}


- (IBAction)abortFind:(id)sender {

	aborted = YES;
    [NSApp stopModal];

}

- (BOOL)aborted {
	return aborted;
}

- (void)setFindString:(id)string {

	if (string != nil) {
		NSPasteboard *findBoard = [NSPasteboard pasteboardWithName:NSFindPboard];
		[findBoard declareTypes:[NSArray arrayWithObject:NSStringPboardType] owner:self];
		[findBoard setString:string forType:NSStringPboardType];

//		NSLog(@"setFindString: %@", string);
		[findField setStringValue:string];
	} else {
//		NSLog(@"null setFindString: %@", string);
	}
	

}

- (void)refresh {

	[findField setStringValue:[self findString]];

	BOOL state = [[findField stringValue] length] > 0;
	[nextButton setEnabled:state];
	[previousButton setEnabled:state];
	aborted = NO;
	
}



- (NSString *)findString {
	
	NSPasteboard *findBoard = [NSPasteboard pasteboardWithName:NSFindPboard];
	[findBoard types];	
	return [findBoard stringForType:NSStringPboardType];

}







@end
