


#import "DragDestinationTextView.h"
#import "MyDocument.h"

@implementation DragDestinationTextView


// ==========================================================
// Overridden drag and drop methods
// ==========================================================

- (NSDragOperation)draggingEntered:(id <NSDraggingInfo>)sender {

	// We're only interested in files here, let the superclass handle everything else

	if (![self dragIsFile:sender]) {
		return [super draggingEntered:sender];
	}

	// It is a file, highlight drop target

	[self lockFocus];
	[[NSColor selectedControlColor] set];
	NSFrameRectWithWidth([self visibleRect], 2.5);
	[self unlockFocus];
	[[self window] flushWindow];
	
	return NSDragOperationGeneric;

}



- (NSDragOperation)draggingUpdated:(id <NSDraggingInfo>)sender {

	NSRect currentRect;

	// We're only interested in files here, let the superclass handle everything else

	if (![self dragIsFile:sender]) {
		return [super draggingUpdated:sender];
	}

	
	/* some code to handle the case where a user drags the mouse around an edge of the
	 * text field, triggering an autoscroll. If we don't do anything, our highlight rame
	 * would get scrolled along with the content and then redrawn immediately which
	 * obviously looks messy.
	 * Instead we check if the visible rectangle has moved since the last
	 * invocation. If it did, we just clear the frame and do no drawing.
	 * If the frame didn't move, we will draw the frame.
	 */
	currentRect = [self visibleRect];

	if (!NSEqualRects(currentRect, previousRect)) {

		previousRect = currentRect;
		[self setNeedsDisplay:YES];

	} else {

		[self lockFocus];
		[[NSColor selectedControlColor] set];
		NSFrameRectWithWidth(currentRect, 2);
		[self unlockFocus];
		[[self window] flushWindow];

	}

	return NSDragOperationGeneric;

}



- (BOOL)prepareForDragOperation:(id <NSDraggingInfo>)sender {

	if (![self dragIsFile:sender]) {
		return [super prepareForDragOperation:sender];
	}

	return YES;

}



- (BOOL)performDragOperation:(id <NSDraggingInfo>)sender {

	NSString *filename;
	BOOL result;
	
	if (![self dragIsFile:sender]) {
		return [super performDragOperation:sender];
	}

	filename = [self getFileForDrag:sender];
	result = [[self delegate] handleDroppedFile:filename forTextView:self];

	if (result == NO) {
		[self setNeedsDisplay:YES];
	}

	return result;
}



- (void)concludeDragOperation:(id <NSDraggingInfo>)sender {

	if (![self dragIsFile:sender]) {
		[super concludeDragOperation:sender];
		return;
	}

	[self setNeedsDisplay:YES];

}



- (void)draggingExited:(id <NSDraggingInfo>)sender {

	if (![self dragIsFile:sender]) {
		[super draggingExited:sender];
		return;
	}
	
	[self setNeedsDisplay:YES];

}







// ==========================================================
// Helper methods to find out if a given NSDraggingInfo refers to a file drag
// ==========================================================

- (BOOL)dragIsFile:(id <NSDraggingInfo>)sender {

	BOOL isDirectory;
	BOOL fileExists;
	
	NSString *dragFilename = [self getFileForDrag:sender];

	if (dragFilename == nil) {
		return NO;
	}
	
	fileExists = [[NSFileManager defaultManager] fileExistsAtPath:dragFilename isDirectory:&isDirectory];

	return (fileExists && (!isDirectory));
}



- (NSString *)getFileForDrag:(id <NSDraggingInfo>)sender {

	NSPasteboard *pb = [sender draggingPasteboard];
	NSString *availableType = [pb availableTypeFromArray:[NSArray arrayWithObjects:NSFilenamesPboardType, nil]];
	NSString *availableTypeString = [pb availableTypeFromArray:[NSArray arrayWithObjects:NSStringPboardType, nil]];
	NSString *dragFilename;
	NSArray *props;

	if (availableType == nil) {
		return nil;
	}

	if (availableTypeString != nil) {
		return nil;
	}

	


	
	props = [pb propertyListForType:availableType];
	dragFilename = [props objectAtIndex:0];

	return dragFilename;

}





@end
