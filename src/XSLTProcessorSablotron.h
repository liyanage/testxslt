//
//  XSLTProcessorSablotron.h
//  TestXSLT
//
//  Created by Marc Liyanage on Thu Aug 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "XSLTProcessor.h"

#include "sablot.h"


@interface XSLTProcessorSablotron : XSLTProcessor {

	SablotSituation S;
	SablotHandle processor;
	MessageHandler msgHandlerPtr;

}

MH_ERROR rawErrorHandler(id self, SablotHandle processor_, MH_ERROR code, MH_LEVEL level, char **fields);
MH_ERROR rawMakeCodeHandler(id self, SablotHandle processor_, int severity, unsigned short facility, unsigned short code);
MH_ERROR rawLogHandler(id self, SablotHandle processor_, MH_ERROR code, MH_LEVEL level, char **fields);
		


@end
