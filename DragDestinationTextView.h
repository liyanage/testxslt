
// $Id$

/* DragDestinationTextView */

#import <Cocoa/Cocoa.h>


/* This is a subclass of NSTextView that behaves identically except for drag and drop.
 * Unlike NSTextView, this one will accept file drags, do all the highlighting etc.
 * If the user drops the file at the end, it calls its delegate which must implement
 * (BOOL)handleDroppedFile:(NSString *)filename forTextView:(NSTextView *)textView;
 */
@interface DragDestinationTextView : NSTextView
{
	NSRect previousRect;
}

- (BOOL)dragIsFile:(id <NSDraggingInfo>)sender;
- (NSString *)getFileForDrag:(id <NSDraggingInfo>)sender;




@end
