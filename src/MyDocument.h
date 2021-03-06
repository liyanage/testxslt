//
//  MyDocument.h
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Mar 03 2002.
//  Copyright (c) 2001 __MyCompanyName__. All rights reserved.
//
//  $Id$


#import <Cocoa/Cocoa.h>
#import <WebKit/WebKit.h>
#import <Quartz/Quartz.h>
#include <sys/time.h>

#import "XMLUtils.h"
#import "Workset.h"
#import "ParameterSet.h"
#import "XSLTProcessorFactory.h"
#import "XMLParserLibxml.h"
#import "XMLTextView.h"
#import "FindPanelController.h"
#import "JumpToLinePanelController.h"
#import "UnsavedChangesPanelController.h"
#import "XSL_FO_Renderer.h"


enum {
	XML = 1,
	XSLT,
	PARAMETERS,
	RESULT,
};

@interface MyDocument : NSDocument {

	Workset *workset;
	NSTimer *uiUpdateTimer;
	BOOL resultDirty;
	BOOL xmlDirty;
	BOOL xsltDirty;
	
	BOOL webViewUpToDate;
	BOOL PDFViewUpToDate;

	int pdfPageCount, pdfCurrentPage;

	NSBundle *processorBundle;

	int processorType;
	XSLTProcessor *processor;
	XMLParserLibxml *wellFormedParser;
	
	NSImage *warningIcon;
	IBOutlet NSImageView *xmlWellFormedIcon;
	IBOutlet NSImageView *xsltWellFormedIcon;
	IBOutlet NSButton *processButton;
	IBOutlet NSButton *saveResultAsButton;
	IBOutlet NSButton *saveResultButton;
	IBOutlet NSButton *openResultURLButton;
	IBOutlet NSTextField *processingTimeField;
	IBOutlet NSTextField *saveResultFilenameField;
	IBOutlet NSTextField *saveXmlFilenameField;
	IBOutlet NSTextField *saveXsltFilenameField;
	IBOutlet NSButton *saveXmlAsButton;
	IBOutlet NSButton *saveXmlButton;
	IBOutlet NSButton *saveXsltButton;
	IBOutlet NSButton *saveXsltAsButton;
	IBOutlet NSButton *paramRemoveButton;
	IBOutlet NSTabView *tabView;
	IBOutlet NSTabView *resultTabView;
	IBOutlet XMLTextView *xmlView;
	IBOutlet XMLTextView *xsltView;
	IBOutlet NSTextView *resultView;
	IBOutlet NSTableView *parameterTable;
	IBOutlet NSButton *autoSaveCheckbox;
	IBOutlet NSButton *autoShowCheckbox;
	IBOutlet NSDrawer *errorDrawer;
	IBOutlet NSPopUpButton *processorTypePopUp;
	IBOutlet WebView *resultWebView;

	IBOutlet NSTextField *pdfCurrentPageField;
	IBOutlet NSTextField *pdfPageCountField;
	IBOutlet NSButton *pdfPreviousPageButton;
	IBOutlet NSButton *pdfNextPageButton;
	IBOutlet NSButton *pdfSaveAsButton;

	IBOutlet NSTextField *xmlTagStackField;
	IBOutlet NSTextField *xsltTagStackField;

	IBOutlet PDFView *resultPDFView;

	NSData *pdfData, *xslfoRendererResultData;
	NSConditionLock *xslfoRendererLock;

	NSString *drawerMessage;
	NSString *messageLog;
	
	IBOutlet NSTextField *webViewBaseURL;

	FindPanelController *findPanelController;
	JumpToLinePanelController *jumpToLinePanelController;
	UnsavedChangesPanelController *unsavedChangesPanelController;

	NSUserDefaults *defaults;
}

- (BOOL)canUseSelectionForFindNow;
- (BOOL)canFindNow;
- (BOOL)canFindAgainNow;
- (IBAction)showFindPanel:(id)sender;
- (IBAction)findNext:(id)sender;
- (IBAction)findPrevious:(id)sender;
- (IBAction)useSelectionForFind:(id)sender;
- (void)findStringWithSearchFlags:(int)flags;

- (IBAction)switchProcessor:(id)sender;

- (BOOL)canJumpToLineNow;
- (IBAction)showJumpToLinePanel:(id)sender;

- (BOOL)showUnsavedChangesPanel;

- (void)updateCompleteUI;
- (void)updateUI;
- (void)doUpdateUI;
- (NSTabView *)tabView;
- (IBAction)selectTab:(id)sender;
- (IBAction)selectTabById:(int)tabId;

//- (IBAction)setProcessorType:(id)sender;
- (IBAction)switchProcessorToType:(int)newType updateUI:(BOOL)updateUI;

- (IBAction)showInBrowser:(id)sender;
- (void)uiUpdateTimerTarget:(NSTimer *)timer;
- (BOOL)canProcessNow;
- (BOOL)validateMenuItem:(NSMenuItem *)menuItem;

- (void)resizeWebView;

- (NSTextView *)currentTextView;

// AppleScript Stuff
- (id)handleProcessScriptCommand:(NSScriptCommand *)command;
- (id)handleExportScriptCommand:(NSScriptCommand *)command;
- (id)handleSetParamScriptCommand:(NSScriptCommand *)command;
- (id)handleClearParamScriptCommand:(NSScriptCommand *)command;
- (id)handleSetProcessorTypeScriptCommand:(NSScriptCommand *)command;


// AppleScript accessors
- (NSString *)xmlcode;
- (void)setXmlcode:(NSString *)s;
- (NSString *)xsltcode;
- (void)setXsltcode:(NSString *)s;
- (NSString *)result;

// Drag and Drop for our custom NSTextView subclass
- (BOOL)handleDroppedFile:(NSString *)filename forTextView:(NSTextView *)sender;

- (IBAction)process:(id)sender;
- (IBAction)loadXml:(id)sender;
- (IBAction)loadXslt:(id)sender;

- (BOOL)canSaveXmlNow;
- (BOOL)canSaveXsltNow;
- (BOOL)canSaveResultNow;

- (IBAction)saveResultAs:(id)sender;
- (IBAction)saveResult:(id)sender;
- (IBAction)saveXmlAs:(id)sender;
- (IBAction)saveXml:(id)sender;
- (IBAction)saveXsltAs:(id)sender;
- (IBAction)saveXslt:(id)sender;
- (IBAction)saveCurrentAs:(id)sender;
- (IBAction)saveCurrent:(id)sender;
- (IBAction)newParameter:(id)sender;
- (IBAction)removeParameter:(id)sender;
- (IBAction)openResultURL:(id)sender;
- (void)autoSave;

- (void)updateResultWebView;
- (void)updateResultPDFView;

- (IBAction)renderFo:(id)sender;

- (IBAction)showErrorLocation:(id)sender;

- (IBAction)pdfSaveAs:(id)sender;

- (void)checkForExternalModifications;

- (void)logMessage:(NSString *)string;
- (void)clearMessageLog;

/*
- (IBAction)showXmlTab:(id)sender;
- (IBAction)showXsltTab:(id)sender;
- (IBAction)showParameterTab:(id)sender;
- (IBAction)showResultTab:(id)sender;
*/

@end
