//
//  XSLTProcessorLibxslt.h
//  TestXSLT
//
//  Created by Marc Liyanage on Thu Aug 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "XSLTProcessor.h"
#import "XMLParserLibxml.h"

#include <stdarg.h>

#include "libxml/parser.h"
#include "libxslt/documents.h"
#include "libxslt/extensions.h"
#include "libxslt/extra.h"
#include "libxslt/functions.h"
#include "libxslt/imports.h"
#include "libxslt/keys.h"
#include "libxslt/namespaces.h"
#include "libxslt/numbersInternals.h"
#include "libxslt/pattern.h"
#include "libxslt/preproc.h"
#include "libxslt/templates.h"
#include "libxslt/transform.h"
#include "libxslt/variables.h"
#include "libxslt/xslt.h"
#include "libxslt/xsltInternals.h"
#include "libxslt/xsltconfig.h"
#include "libxslt/xsltutils.h"
#include "libxslt/attributes.h"

#include "libexslt/exslt.h"
#include "libexslt/exsltconfig.h"


@interface XSLTProcessorLibxslt : XSLTProcessor {

	
}

void xsltErrorHandler(id self, const char *message, ...);



@end
