#import "JumpToLinePanelController.h"

@implementation JumpToLinePanelController


- (IBAction)jumpToLine:(id)sender {

	[self setLineNumber:[lineNumberField intValue]];

    [NSApp stopModal];

}



- (IBAction)abortJumpToLine:(id)sender {

//	NSLog(@"abort Jump!");
	[self setLineNumber:0];
	[NSApp stopModal];

}



- (void)setLineNumber:(unsigned int)line {


//	NSLog(@"setLineNumber: %d", line);
	lineNumber = line;

}

- (unsigned int)lineNumber {

	return lineNumber;
}





@end
