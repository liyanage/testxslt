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

@interface XMLTextView : DragDestinationTextView
{

	
}

-(void)flashRange:(NSRange)range;
-(BOOL)completeAfterSlash;
-(void)selectLineByNumber:(int)line;
-(NSRange)scanBackwardsForOpeningTagNameInRange:(NSRange)scanRange;




@end
