/* UnsavedChangesPanelController */

#import <Cocoa/Cocoa.h>



@interface UnsavedChangesPanelController : NSWindowController
{
	BOOL keepChanges;
}
- (IBAction)discardUnsavedChanges:(id)sender;
- (IBAction)keepUnsavedChanges:(id)sender;
- (BOOL)keepChanges;
@end
