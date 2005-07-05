//
//  XMLTextView.h
//  TestXSLT
//
//  Created by Marc Liyanage on Fri Aug 02 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <DragDestinationTextView.h>

#include <unistd.h>
#include "expat.h"
#include "ragel_xmlscanner.h"
#import "XMLUtils.h"

@interface XMLTextView : DragDestinationTextView
{

	char (*resultstack)[MAXTAGLENGTH];
	int stackresult;
	int tagpositions[STACKDEPTH];
	XML_Parser parser;
	BOOL hasError;
	int errorLine, errorColumn;
	NSString *errorString;
	NSUserDefaults *defaults;
	NSString *tagStack;
	
}

-(void)clearError;
-(void)flashRange:(NSRange)range;
-(BOOL)completeAfterSlash;
-(void)selectLineByNumber:(int)line;
-(void)calculateTagStack;
-(void)calculateTagStackAtLocation:(int)location;
-(BOOL)checkWellFormed;
-(void)setError:(NSString *)errstring atLine:(int)line atColumn:(int)column;
-(void)clearError;

@end
