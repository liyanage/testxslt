//
//  FindPanelController.h
//  TestXSLT
//
//  Created by Marc Liyanage on Tue Aug 20 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import <AppKit/AppKit.h>

@interface FindPanelController : NSWindowController {

	IBOutlet NSTextField *findField;
	IBOutlet NSButton *caseInsensitiveCheckbox;
	IBOutlet NSButton *nextButton;
	IBOutlet NSButton *previousButton;
	unsigned int searchFlags;
	BOOL aborted;
	
}

- (unsigned int)caseInsensitiveFlag;
- (unsigned int)searchFlags;
- (void)setFindString:(id)string;
- (void)setSearchFlags:(unsigned int)flags;
- (NSString *)findString;
- (IBAction)find:(id)sender;
- (IBAction)findPrevious:(id)sender;
- (IBAction)abortFind:(id)sender;
- (IBAction)keyUp:(NSEvent *)event;
- (void)refresh;
- (BOOL)aborted;

@end
