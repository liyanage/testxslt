/* JumpToLinePanelController */

#import <Cocoa/Cocoa.h>

@interface JumpToLinePanelController : NSWindowController
{
    IBOutlet NSTextField *lineNumberField;
	unsigned int lineNumber;
}

- (IBAction)jumpToLine:(id)sender;
- (IBAction)abortJumpToLine:(id)sender;
- (void)setLineNumber:(unsigned int)lineNumber;
- (unsigned int)lineNumber;

@end
