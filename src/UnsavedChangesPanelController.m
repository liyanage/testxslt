#import "UnsavedChangesPanelController.h"

@implementation UnsavedChangesPanelController

- (IBAction)discardUnsavedChanges:(id)sender
{
	keepChanges = FALSE;
	[NSApp stopModal];
}

- (IBAction)keepUnsavedChanges:(id)sender
{
	keepChanges = TRUE;
	[NSApp stopModal];
}

- (BOOL)keepChanges
{
	return keepChanges;
}

@end
