//
//  MyDocument.m
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Mar 03 2002.
//  Copyright (c) 2001 __MyCompanyName__. All rights reserved.
//
// $Id$

#import "MyDocument.h"
#import "Workset.h"




@implementation MyDocument

- (id)init {

	if (self = [super init]) {
		workset = [[Workset alloc] init];
		processor = [XSLTProcessorFactory makeProcessorOfType:PROCESSORTYPE_SABLOTRON];
		wellFormedParser = [[XMLParserLibxml alloc] init];
		xmlDirty = NO;
		xsltDirty = NO;
	}

	
	
	return self;
}

- (void)dealloc {

	[workset release];
	[processor release];
	[wellFormedParser release];
	[findPanelController release];
	[jumpToLinePanelController release];
	[unsavedChangesPanelController release];

}

- (IBAction)selectTab:(id)sender {

	[self selectTabById:[sender tag]];
	
}






- (IBAction)selectTabById:(int)tabId {

	NSString *tabName;

	switch (tabId) {

		case XML:
			tabName = @"xmlTab";
			break;

		case XSLT:
			tabName = @"xsltTab";
			break;

		case PARAMETERS:
			tabName = @"parametersTab";
			break;

		case RESULT:
		default:
			tabName = @"resultTab";
			break;


	}

	[tabView selectTabViewItemWithIdentifier:tabName];

}


- (void)tabView:(NSTabView *)tabView didSelectTabViewItem:(NSTabViewItem *)tabViewItem {

	NSLog(@"switch tab xyz x");
	[[self undoManager] removeAllActions];

	if ([[tabViewItem identifier] isEqualToString:@"htmlResult"]) {
		[self resizeWebView];
		[self updateResultWebView];
	} else if ([[tabViewItem identifier] isEqualToString:@"xslfoResult"]) {
		[self updateResultImageView];
	}
	
}




- (void)updateUI {
	
//	NSLog(@"updateUI running...");

	[uiUpdateTimer invalidate];
	[uiUpdateTimer release];

	uiUpdateTimer = [NSTimer scheduledTimerWithTimeInterval:0.5 target:self selector:@selector(uiUpdateTimerTarget:) userInfo:nil repeats:NO];

	[uiUpdateTimer retain];

}

- (void)uiUpdateTimerTarget:(NSTimer *)timer {

	[self doUpdateUI];
	[timer release];
	uiUpdateTimer = nil;
}



- (void)doUpdateUI {

//	NSLog(@"doUpdateUI running...");
//	NSLog(@"debug: %@", [[[NSApp mainWindow] document] tabView]);


	[saveXmlAsButton setEnabled:[workset hasXmlCode]];
	[saveXsltAsButton setEnabled:[workset hasXsltCode]];
	[saveResultAsButton setEnabled:[workset hasResult]];

	[saveResultButton setEnabled:[workset hasResultFilename] && resultDirty];
	[autoSaveCheckbox setEnabled:[workset hasResultFilename]];

	[openResultURLButton setEnabled:[workset hasResultFilename]];
	[autoShowCheckbox setEnabled:[openResultURLButton isEnabled]];

	[paramRemoveButton setEnabled:[parameterTable selectedRow] != -1];

	[processButton setEnabled:[self canProcessNow]];

	[saveResultFilenameField setObjectValue:[workset resultFilename]];
	[saveResultFilenameField setToolTip:[workset resultFilename]];


	[saveXmlFilenameField setObjectValue:[workset xmlFilename]];
	[saveXmlFilenameField setToolTip:[workset xmlFilename]];
	[saveXmlButton setEnabled:[workset hasXmlFilename] && xmlDirty];

	
	[saveXsltFilenameField setObjectValue:[workset xsltFilename]];
	[saveXsltFilenameField setToolTip:[workset xsltFilename]];
	[saveXsltButton setEnabled:[workset hasXsltFilename] && xsltDirty];

	[self updateWellFormedIcons];
	
	[parameterTable reloadData];

	
	[resultView setString:[workset result]];

	if ([[[resultTabView selectedTabViewItem] identifier] isEqualToString:@"htmlResult"]) {
		[self updateResultWebView];
	} else if ([[[resultTabView selectedTabViewItem] identifier] isEqualToString:@"xslfoResult"]) {
		[self updateResultImageView];
	}
	
	[pdfCurrentPageField setIntValue: (pdfPageCount ? (pdfCurrentPage + 1) : 0)];
	[pdfPageCountField setIntValue:pdfPageCount];
	
	[pdfPreviousPageButton setEnabled:pdfCurrentPage > 0];
	[pdfNextPageButton setEnabled:pdfCurrentPage < (pdfPageCount - 1)];
	[pdfSaveAsButton setEnabled:(pdfPageCount > 0)];
	
	
}


- (void)updateResultWebView {
	if (!webViewUpToDate) {
		WebFrame *mainFrame = [resultWebView mainFrame];
		[mainFrame loadHTMLString:[workset result] baseURL:nil];
		webViewUpToDate = YES;
	}
}


- (void)updateResultImageView {
	if (!imageViewUpToDate) {
		[self renderFo:self];
		imageViewUpToDate = YES;
	}
}


- (void)updateWellFormedIcons {

	if (![workset hasXmlCode] || [wellFormedParser checkWellFormedString:[workset xmlCode]]) {
		[xmlWellFormedIcon setImage:nil];
		[xmlWellFormedIcon setToolTip:nil];
	} else {
		[xmlWellFormedIcon setImage:warningIcon];
		[xmlWellFormedIcon setToolTip:[NSString stringWithFormat:@"The XML code is not well-formed, error at line %d:\n%@", [wellFormedParser errorLine], [wellFormedParser errorMessage]]];
	}


	if (![workset hasXsltCode] || [wellFormedParser checkWellFormedString:[workset xsltCode]]) {
		[xsltWellFormedIcon setImage:nil];
		[xsltWellFormedIcon setToolTip:nil];
	} else {
		[xsltWellFormedIcon setImage:warningIcon];
		[xsltWellFormedIcon setToolTip:[NSString stringWithFormat:@"The XSLT code is not well-formed, error at line %d:\n%@", [wellFormedParser errorLine], [wellFormedParser errorMessage]]];
	}

	
}


- (BOOL)canProcessNow {

	return [workset hasXmlCode] && [workset hasXsltCode];

}

- (BOOL)validateMenuItem:(NSMenuItem *)menuItem {

//	NSLog(@"validate: %@, tag: %d", menuItem, [menuItem tag]);

	switch ([menuItem tag]) {

		case 10:	// Process
			return [self canProcessNow];
			break;

		case 11:	// Save
			return [workset hasResultFilename];
			break;

		case 12:	// Find
			return [self canFindNow];
			break;

		case 13:	// Find Next
		case 14:	// Find Previous
			return [self canFindAgainNow];
			break;

		case 15:	// Use Selection for Find
			return [self canUseSelectionForFindNow];
			break;

		case 16:	// Jump to Line
			return [self canJumpToLineNow];
			break;

		default:
			return YES;
			break;

	}


}

- (IBAction)showInBrowser:(id)sender {

	

}


- (void)updateCompleteUI {

	[xmlView setString:[workset xmlCode]];
	[xsltView setString:[workset xsltCode]];
	[self doUpdateUI];
	
}



- (void)textDidChange:(NSNotification *)aNotification {

	id sender = [aNotification object];

	if ([sender isEqual:xmlView]) {
		[workset setXmlCode:[xmlView string]];
		xmlDirty = YES;
	} else if ([sender isEqual:xsltView]) {
		[workset setXsltCode:[xsltView string]];
		xsltDirty = YES;
	}

	[self updateChangeCount:NSChangeDone];
	[self updateUI];
	
}



- (NSTabView *)tabView {

	return tabView;

}

- (BOOL)canJumpToLineNow {

	NSTextView *view = [self currentTextView];

	return (view == xmlView) || (view == xsltView);
	
}


- (IBAction)showJumpToLinePanel:(id)sender {

	[NSApp beginSheet:[jumpToLinePanelController window]
       modalForWindow:[[[self windowControllers] objectAtIndex:0] window]
        modalDelegate:nil
       didEndSelector:nil
          contextInfo:nil];

    [NSApp runModalForWindow:[jumpToLinePanelController window]];
    [NSApp endSheet:[jumpToLinePanelController window]];
    [[jumpToLinePanelController window] orderOut:self];

	if ([jumpToLinePanelController lineNumber] == 0) {
		return;
	}

	[((XMLTextView *)[self currentTextView]) selectLineByNumber:[jumpToLinePanelController lineNumber]];

//	NSLog(@"jump to line: %d", [jumpToLinePanelController lineNumber]);

}


- (IBAction)showFindPanel:(id)sender {

	[findPanelController refresh];

	[NSApp beginSheet:[findPanelController window]
       modalForWindow:[[[self windowControllers] objectAtIndex:0] window]
        modalDelegate:nil
       didEndSelector:nil
          contextInfo:nil];
	
    [NSApp runModalForWindow:[findPanelController window]];
    [NSApp endSheet:[findPanelController window]];
    [[findPanelController window] orderOut:self];

	if ([findPanelController aborted]) {
		return;
	}

	[self findStringWithSearchFlags:[findPanelController searchFlags]];
	
}




- (IBAction)findNext:(id)sender {

	[self findStringWithSearchFlags:[findPanelController searchFlags] & NSCaseInsensitiveSearch];

}


- (IBAction)findPrevious:(id)sender {

	[self findStringWithSearchFlags:([findPanelController searchFlags] | NSBackwardsSearch)];

}

- (BOOL)canUseSelectionForFindNow {

	NSTextView *view = [self currentTextView];
	NSRange selectedRange;

	if (view == nil) {
		return NO;
	}

	selectedRange = [view selectedRange];

	if (selectedRange.length < 1) {
		return NO;
	}

	return YES;
	
}



- (IBAction)useSelectionForFind:(id)sender {

	NSString *text;
	NSTextView *view = [self currentTextView];
	
	text = [[view string] substringWithRange:[view selectedRange]];

	[findPanelController setFindString:text];
	
}




- (BOOL)canFindNow {

	NSString *currentTabViewItem = [[[self tabView] selectedTabViewItem] identifier];
	
	if ([currentTabViewItem isEqualToString:@"xmlTab"]
	    || [currentTabViewItem isEqualToString:@"xsltTab"]
	    || [currentTabViewItem isEqualToString:@"resultTab"]) {
		return YES;
	}

	return NO;
	
}

- (BOOL)canFindAgainNow {

	return ([findPanelController findString] != nil) && [self canFindNow];

}


- (void)findStringWithSearchFlags:(int)flags {

	NSTextView *currentView;
	NSString *text;
	NSString *string;
	NSRange selectedRange, leftRange, rightRange, resultRange, searchRange;

	NSPasteboard *findBoard = [NSPasteboard pasteboardWithName:NSFindPboard];
	[findBoard types];
	string = [findBoard stringForType:NSStringPboardType];

	currentView = [self currentTextView];
	if (currentView == nil) {
		return;
	}

	text = [currentView string];
	
	selectedRange = [currentView selectedRange];
	leftRange = NSMakeRange(0, selectedRange.location);
	rightRange = NSMakeRange(NSMaxRange(selectedRange), [text length] - NSMaxRange(selectedRange));
	
	if (flags & NSBackwardsSearch) {
		searchRange = leftRange;
	} else {
		searchRange = rightRange;
	}
	
	resultRange = [text rangeOfString:string options:flags range:searchRange];

	if (resultRange.location == NSNotFound) {
		NSBeep();
		return;
	}

	[currentView setSelectedRange:resultRange];
	[currentView scrollRangeToVisible:resultRange];

}




- (NSTextView *)currentTextView {

	NSString *currentTabViewItem = [[[self tabView] selectedTabViewItem] identifier];

	if ([currentTabViewItem isEqualToString:@"xmlTab"]) {
		return xmlView;
	} else if ([currentTabViewItem isEqualToString:@"xsltTab"]) {
		return xsltView;
	} else if ([currentTabViewItem isEqualToString:@"resultTab"]) {
		return resultView;
	}

	return nil;

}





- (IBAction)process:(id)sender {

	
	const char **params = [[workset parameterSet] cArray];
	
	struct timeval tstart, tend;
	gettimeofday(&tstart, NULL);
	
	long processingTime;

	if ([workset hasXsltFilename]) {
		[processor setBaseUri:[NSString stringWithFormat:@"file://%@", [workset xsltFilename]]];
	}

	if (![processor processStrings:[workset xmlCode] withXslt:[workset xsltCode] andParameters:params]) {

		[drawerMessageField setStringValue:[NSString stringWithFormat:@"Error on line %d of your %@ code:\n%@", [processor errorLine], ([processor errorSource] == XSLT_ERROR_SOURCE_XML ? @"XML" : @"XSLT"), [processor errorMessage]]];

		NSBeep();
		[errorDrawer openOnEdge:NSMinYEdge];
		[self showErrorLocation:nil];

	} else {

		gettimeofday(&tend, NULL);

		processingTime = ((tend.tv_sec * 1000000 + tend.tv_usec) - (tstart.tv_sec * 1000000 + tstart.tv_usec)) / 1000;
		
		[workset setResult:[processor result]];
		resultDirty = YES;
		[self autoSave];
		[errorDrawer close];
		[self selectTabById:RESULT];
		[processingTimeField setStringValue:[NSString stringWithFormat:@"Time: %ldms", processingTime]];
	}

	webViewUpToDate = NO;
	imageViewUpToDate = NO;
	
	[self updateUI];
}


- (void)autoSave {

	if (resultDirty && [autoSaveCheckbox state] == NSOnState) {
		[self saveResult:nil];
	}

}

- (void)autoShow {

	if ([autoShowCheckbox state] == NSOnState) {
		[self openResultURL:nil];
	}

}


- (IBAction)loadXml:(id)sender {

	NSOpenPanel *panel = [NSOpenPanel openPanel];

	if ([panel runModalForDirectory:nil file:nil types:nil] == NSOKButton) {

		//	NSLog(@"choosen: %@", [[panel filenames] objectAtIndex:0]);

		[workset setXmlCode:[NSString stringWithContentsOfFile:[[panel filenames] objectAtIndex:0]]];
		[workset setXmlFilename:[[panel filenames] objectAtIndex:0]];
		[self updateChangeCount:NSChangeDone];
		[self updateCompleteUI];
	}
}





- (IBAction)loadXslt:(id)sender {

	NSOpenPanel *panel = [NSOpenPanel openPanel];

	if ([panel runModalForDirectory:nil file:nil types:nil] == NSOKButton) {

		//	NSLog(@"choosen: %@", [[panel filenames] objectAtIndex:0]);

		[workset setXsltCode:[NSString stringWithContentsOfFile:[[panel filenames] objectAtIndex:0]]];
		[workset setXsltFilename:[[panel filenames] objectAtIndex:0]];
		[self updateChangeCount:NSChangeDone];
		[self updateCompleteUI];

	}
}



- (IBAction)saveXmlAs:(id)sender {

	NSSavePanel *panel = [NSSavePanel savePanel];

	if ([panel runModal] == NSFileHandlingPanelOKButton) {

		[workset setXmlFilename:[panel filename]];
		[self saveXml:nil];

	}
}



- (IBAction)saveXml:(id)sender {


	if ([workset hasXmlFilename]) {
		[workset saveXml];
		xmlDirty = NO;
	}

	[self updateUI];
}


- (IBAction)saveXsltAs:(id)sender {

	NSSavePanel *panel = [NSSavePanel savePanel];

	if ([panel runModal] == NSFileHandlingPanelOKButton) {

		[workset setXsltFilename:[panel filename]];
		[self saveXslt:nil];

	}
}



- (IBAction)saveXslt:(id)sender {

	if ([workset hasXsltFilename]) {
		[workset saveXslt];
		xsltDirty = NO;
	}

	[self updateUI];
}



- (IBAction)saveResultAs:(id)sender {

	NSSavePanel *panel = [NSSavePanel savePanel];

	if ([panel runModal] == NSFileHandlingPanelOKButton) {

		[workset setResultFilename:[panel filename]];

		[self saveResult:nil];
		
	}
}

- (IBAction)saveResult:(id)sender {

	if ([workset hasResultFilename]) {

		[[workset result] writeToFile:[workset resultFilename] atomically:NO];
		resultDirty = NO;

	}

	[self updateUI];
	[self autoShow];
	
}


- (IBAction)openResultURL:(id)sender {

//	NSLog(@"openResultURL running...");
	
	if ([workset hasResultFilename]) {

		[[NSWorkspace sharedWorkspace] openURL:[NSURL fileURLWithPath:[workset resultFilename]]];

	}
}


- (IBAction)newParameter:(id)sender {

	[[workset parameterSet] addParameter:@"name" withValue:@"value"];
	[self doUpdateUI];
	
}

- (IBAction)removeParameter:(id)sender {

	int row = [parameterTable selectedRow];

	if (row != -1) {
		[[workset parameterSet] removeParameterAtIndex:row];
		[self doUpdateUI];
	} else {
		NSBeep();
	}

}

- (int)numberOfRowsInTableView:(NSTableView *)aTableView {
	return [[workset parameterSet] count];
}

- (id)tableView:(NSTableView *)aTableView
objectValueForTableColumn:(NSTableColumn *)aTableColumn
					 row:(int)rowIndex {

	return [[workset parameterSet] getField:[aTableColumn identifier] atIndex:rowIndex];
}



- (void)tableView:(NSTableView *)aTableView
   setObjectValue:(id)anObject
   forTableColumn:(NSTableColumn *)aTableColumn
			  row:(int)rowIndex {

	[[workset parameterSet] setField:[aTableColumn identifier] atIndex:rowIndex toString:anObject];
}




- (IBAction)setProcessorType:(id)sender {

	int newType = [sender tag];

	if ([processor processorType] == newType) {
		return;
	}

	[self switchProcessorToType:newType updateUI:NO];

	NSLog(@"change processor type menu: %d", [sender tag]);

}


- (IBAction)switchProcessorToType:(int)newType updateUI:(BOOL)updateUI {

	XSLTProcessor *newProcessor = nil;

	newProcessor = [XSLTProcessorFactory makeProcessorOfType:newType];

	if (!newProcessor) {
		NSLog(@"Unable to create new processor of type '%d'", newType);
	}

	[processor release];
	processor = newProcessor;

	if (updateUI) {
		[processorTypePopUp selectItemAtIndex:[processorTypePopUp indexOfItemWithTag:newType]];
	}


}



- (id)handleProcessScriptCommand:(NSScriptCommand *)command {

	if ([self canProcessNow]) {
		[self process:nil];
	}

	return nil;
	
}


- (id)handleExportScriptCommand:(NSScriptCommand *)command {

	NSDictionary *args = [command evaluatedArguments];
    NSString *file = [args objectForKey:@"File"];

//	NSLog(file);

	if (file != nil) {

		[workset setResultFilename:file];

		[self saveResult:nil];
	}

	return nil;
	
}

- (id)handleSetParamScriptCommand:(NSScriptCommand *)command {

	NSDictionary *args = [command evaluatedArguments];
    NSString *paramName = [args objectForKey:@"Name"];
    NSString *paramValue = [args objectForKey:@"Value"];

	[[workset parameterSet] removeParameterByName:paramName];
	
	[[workset parameterSet] addParameter:paramName withValue:paramValue];
	[self doUpdateUI];

	return nil;
	
}

- (id)handleClearParamScriptCommand:(NSScriptCommand *)command {

	NSDictionary *args = [command evaluatedArguments];
    NSString *paramName = [args objectForKey:@"Name"];

	[[workset parameterSet] removeParameterByName:paramName];
	return nil;
	
}

- (id)handleSetProcessorTypeScriptCommand:(NSScriptCommand *)command {

	NSDictionary *args = [command evaluatedArguments];
    NSString *processorType = [args objectForKey:@"Name"];
	
	if ([processorType caseInsensitiveCompare:@"libxslt"] == NSOrderedSame) {

		[self switchProcessorToType:PROCESSORTYPE_LIBXSLT updateUI:YES];

	} else if ([processorType caseInsensitiveCompare:@"sablotron"] == NSOrderedSame) {

		[self switchProcessorToType:PROCESSORTYPE_SABLOTRON updateUI:YES];

	} else if ([processorType caseInsensitiveCompare:@"saxon"] == NSOrderedSame) {

		[self switchProcessorToType:PROCESSORTYPE_SAXON updateUI:YES];

	} else if ([processorType caseInsensitiveCompare:@"xalan-j"] == NSOrderedSame) {
		
		[self switchProcessorToType:PROCESSORTYPE_XALAN_J updateUI:YES];
		
	} else {
		NSLog(@"unknown processor");
	}

	[self doUpdateUI];
	return nil;

}

- (BOOL)handleDroppedFile:(NSString *)filename forTextView:(NSTextView *)sender {

	
	NSString *fileContents = [NSString stringWithContentsOfFile:filename];

	if (fileContents == nil) {
		return NO;
	}

	if ([sender isEqual:xmlView]) {

		[self setXmlcode:fileContents];
		[workset setXmlFilename:filename];
		
	} else if ([sender isEqual:xsltView]) {

		[self setXsltcode:fileContents];
		[workset setXsltFilename:filename];
		
	} else {

		NSLog(@"Unknown sender view");

	}

	[self updateUI];
	return YES;
	
}


- (NSString *)xmlcode {
	return [workset xmlCode];
}

- (void)setXmlcode:(NSString *)s {

	NSString *currentContents = [[[NSString alloc] initWithString:[self xmlcode]] autorelease];

	[[self undoManager] registerUndoWithTarget:self
								   selector:@selector(setXmlcode:)
									 object:currentContents];

	[workset setXmlCode:s];
	[self updateCompleteUI];
}



- (NSString *)xsltcode {
	return [workset xsltCode];
}

- (void)setXsltcode:(NSString *)s {

	NSString *currentContents = [[[NSString alloc] initWithString:[self xsltcode]] autorelease];

	[[self undoManager] registerUndoWithTarget:self
									  selector:@selector(setXsltcode:)
									    object:currentContents];

	[workset setXsltCode:s];
	[self updateCompleteUI];
}


- (NSString *)result {
	return [workset result];
}



- (void)tableViewSelectionDidChange:(NSNotification *)notification {
	[self doUpdateUI];
}


- (void)checkForExternalModifications {

	BOOL keep = NO;
	
	if ([workset xmlModifiedExternally] && xmlDirty || [workset xsltModifiedExternally] && xsltDirty) {

		/* external changes conflicting with local changes detected.
		 * Ask the user if we should keep the local unsaved changes
		 */
		keep = [self showUnsavedChangesPanel];

	}

	if ([workset xmlModifiedExternally] && !(xmlDirty && keep)) {
			[workset reloadXmlFromFile];
			[self updateChangeCount:NSChangeDone];
			[self updateCompleteUI];
			xmlDirty = NO;
	}

	if ([workset xsltModifiedExternally] && !(xsltDirty && keep)) {
			[workset reloadXsltFromFile];
			[self updateChangeCount:NSChangeDone];
			[self updateCompleteUI];
			xsltDirty = NO;
	}

	[self updateUI];
	
}


- (BOOL)showUnsavedChangesPanel {

	[NSApp beginSheet:[unsavedChangesPanelController window]
	modalForWindow:[[[self windowControllers] objectAtIndex:0] window]
	 modalDelegate:nil
	didEndSelector:nil
	   contextInfo:nil];

    [NSApp runModalForWindow:[unsavedChangesPanelController window]];
    [NSApp endSheet:[unsavedChangesPanelController window]];
    [[unsavedChangesPanelController window] orderOut:self];

	return ([unsavedChangesPanelController keepChanges]);

}

- (IBAction)renderFo:(id)sender {

	XSL_FO_Renderer *xfr = [[XSL_FO_Renderer alloc] init];

	NSData *resultData = [xfr render:[workset result]];

	[resultData retain];
	[pdfData release];
	pdfData = resultData;
	
	NSImage *pdfImage = [[[NSImage alloc] initWithData:resultData] autorelease];
	[pdfImage setBackgroundColor:[NSColor whiteColor]];
	[pdfImage setCacheMode:NSImageCacheNever];
	
	[resultImageView setImage:pdfImage];
	[resultImageView setFrameSize:[pdfImage size]];

	//:[[[pdfImage representations] objectAtIndex:0] bounds]
	//[resultImageView sizeToFit];
	
	//[resultImageView setNeedsDisplay:YES];

	NSLog(@"image reps: -%@-", [pdfImage representations]);
	NSLog(@"count: -%d-", [[[pdfImage representations] objectAtIndex:0] pageCount]);
	
	pdfPageCount = [[[pdfImage representations] objectAtIndex:0] pageCount];
	pdfCurrentPage = 0;
		
	[xfr release];
	
}


- (IBAction)pdfPreviousPage:(id)sender {
	
	if (pdfCurrentPage > 0) {
		pdfCurrentPage--;
		[[[[resultImageView image] representations] objectAtIndex:0] setCurrentPage:pdfCurrentPage];
		[resultImageView setNeedsDisplay:YES];
		[self doUpdateUI];
	}
	
}

- (IBAction)pdfNextPage:(id)sender {
	
	if (pdfCurrentPage < (pdfPageCount - 1)) {
		pdfCurrentPage++;
		[[[[resultImageView image] representations] objectAtIndex:0] setCurrentPage:pdfCurrentPage];
		[resultImageView setNeedsDisplay:YES];
		[self doUpdateUI];
	}
	
}


- (IBAction)pdfSaveAs:(id)sender {

	NSSavePanel *panel = [NSSavePanel savePanel];
	
	if ([panel runModal] == NSFileHandlingPanelOKButton) {
		
		[pdfData writeToFile:[panel filename] atomically:YES];

	}
	
}




- (void)windowDidBecomeMain:(NSNotification *)aNotification {

	[self checkForExternalModifications];

}

- (void)windowDidResize:(NSNotification *)aNotification {

	[self resizeWebView];
	
}

- (void)resizeWebView {
	
	[[[resultWebView mainFrame] frameView] setFrame:[resultWebView frame]];
	[resultWebView setNeedsDisplay:YES];

}





- (NSString *)windowNibName
{
    // Override returning the nib file name of the document
    // If you need to use a subclass of NSWindowController or if your document supports multiple NSWindowControllers, you should remove this method and override -makeWindowControllers instead.
    return @"MyDocument";
}

- (void)windowControllerDidLoadNib:(NSWindowController *) aController
{
	NSFont *computerFont = [resultView font];
	
	NSLog(@"resultview: ", resultView);
	NSLog(@"font: ", computerFont);
		
	NSSize errorDrawerSize;

	[super windowControllerDidLoadNib:aController];

	[resultImageView setImageAlignment:NSImageAlignTopLeft];
//	[resultImageView setImageFrameStyle:NSImageFrameGroove];
	[resultImageView setImageScaling:NSScaleNone];
	[resultImageView setEditable:NO];
	

	// Add any code here that need to be executed once the windowController has loaded the document's window.

	// register our two input text views to receive file drags
	//
//	[xmlView registerForDraggedTypes:[NSArray arrayWithObjects:NSFilenamesPboardType, nil]];
//	[xsltView registerForDraggedTypes:[NSArray arrayWithObjects:NSFilenamesPboardType, nil]];

/*
	[xmlView setFont:computerFont];
	[xsltView setFont:computerFont];
*/
	[xmlView setAllowsUndo:YES];
	[xsltView setAllowsUndo:YES];

	[resultWebView setTextSizeMultiplier:0.9];
	
	warningIcon = [xmlWellFormedIcon image];
	
	[self updateCompleteUI];

	errorDrawerSize = [errorDrawer contentSize];
	errorDrawerSize.height = 130;
	[errorDrawer setContentSize:errorDrawerSize];

	if (findPanelController == nil) {
		findPanelController = [[FindPanelController alloc] initWithWindowNibName:@"FindPanel"];
//		NSLog(@"init find panel controller: %@", findPanelController);
	}

	if (jumpToLinePanelController == nil) {
		jumpToLinePanelController = [[JumpToLinePanelController alloc] initWithWindowNibName:@"JumpToLine"];
//		NSLog(@"init jump to line panel controller: %@", jumpToLinePanelController);
	}

	if (unsavedChangesPanelController == nil) {
		unsavedChangesPanelController = [[UnsavedChangesPanelController alloc] initWithWindowNibName:@"UnsavedChanges"];
//		NSLog(@"init unsaved changes panel controller: %@", unsavedChangesPanelController);
	}

	

	
}



- (IBAction)showErrorLocation:(id)sender {

	XMLTextView *textView;
	int errorLine = 0;

	if ([processor errorSource] == XSLT_ERROR_SOURCE_XML) {
		[self selectTabById:XML];
		textView = xmlView;
	} else {
		[self selectTabById:XSLT];
		textView = xsltView;
	}

	errorLine = [processor errorLine];

	[textView selectLineByNumber:errorLine];
}


- (NSData *)dataRepresentationOfType:(NSString *)aType
{
    // Insert code here to write your document from the given data.  You can also choose to override -fileWrapperRepresentationOfType: or -writeToFile:ofType: instead.
	return [NSArchiver archivedDataWithRootObject:workset];
}

- (BOOL)loadDataRepresentation:(NSData *)data ofType:(NSString *)aType
{
    // Insert code here to read your document from the given data.  You can also choose to override -loadFileWrapperRepresentation:ofType: or -readFromFile:ofType: instead.

	[workset release];
	workset = [[NSUnarchiver unarchiveObjectWithData:data] retain];
	[self updateCompleteUI];

	return YES;
}

@end
