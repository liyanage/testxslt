#
# Functions from module HTMLparser
#

def htmlHandleOmittedElem(val):
    """Set and return the previous value for handling HTML omitted
       tags. """
    ret = libxml2mod.htmlHandleOmittedElem(val)
    return ret

def htmlIsScriptAttribute(name):
    """Check if an attribute is of content type Script """
    ret = libxml2mod.htmlIsScriptAttribute(name)
    return ret

def htmlParseDoc(cur, encoding):
    """parse an HTML in-memory document and build a tree. """
    ret = libxml2mod.htmlParseDoc(cur, encoding)
    if ret is None:raise parserError('htmlParseDoc() failed')
    return xmlDoc(_obj=ret)

def htmlParseFile(filename, encoding):
    """parse an HTML file and build a tree. Automatic support for
       ZLIB/Compress compressed document is provided by default
       if found at compile-time. """
    ret = libxml2mod.htmlParseFile(filename, encoding)
    if ret is None:raise parserError('htmlParseFile() failed')
    return xmlDoc(_obj=ret)

#
# Functions from module HTMLtree
#

def htmlIsBooleanAttr(name):
    """Determine if a given attribute is a boolean attribute. """
    ret = libxml2mod.htmlIsBooleanAttr(name)
    return ret

def htmlNewDoc(URI, ExternalID):
    """Creates a new HTML document """
    ret = libxml2mod.htmlNewDoc(URI, ExternalID)
    if ret is None:raise treeError('htmlNewDoc() failed')
    return xmlDoc(_obj=ret)

def htmlNewDocNoDtD(URI, ExternalID):
    """Creates a new HTML document without a DTD node if @URI and
       @ExternalID are None """
    ret = libxml2mod.htmlNewDocNoDtD(URI, ExternalID)
    if ret is None:raise treeError('htmlNewDocNoDtD() failed')
    return xmlDoc(_obj=ret)

#
# Functions from module catalog
#

def catalogAdd(type, orig, replace):
    """Add an entry in the catalog, it may overwrite existing but
       different entries. If called before any other catalog
       routine, allows to override the default shared catalog put
       in place by xmlInitializeCatalog(); """
    ret = libxml2mod.xmlCatalogAdd(type, orig, replace)
    return ret

def catalogCleanup():
    """Free up all the memory associated with catalogs """
    libxml2mod.xmlCatalogCleanup()

def catalogConvert():
    """Convert all the SGML catalog entries as XML ones """
    ret = libxml2mod.xmlCatalogConvert()
    return ret

def catalogDump(out):
    """Free up all the memory associated with catalogs """
    libxml2mod.xmlCatalogDump(out)

def catalogGetPublic(pubID):
    """Try to lookup the system ID associated to a public ID
       DEPRECATED, use xmlCatalogResolvePublic() """
    ret = libxml2mod.xmlCatalogGetPublic(pubID)
    return ret

def catalogGetSystem(sysID):
    """Try to lookup the system ID associated to a public ID
       DEPRECATED, use xmlCatalogResolveSystem() """
    ret = libxml2mod.xmlCatalogGetSystem(sysID)
    return ret

def catalogRemove(value):
    """Remove an entry from the catalog """
    ret = libxml2mod.xmlCatalogRemove(value)
    return ret

def catalogResolve(pubID, sysID):
    """Do a complete resolution lookup of an External Identifier """
    ret = libxml2mod.xmlCatalogResolve(pubID, sysID)
    return ret

def catalogResolvePublic(pubID):
    """Try to lookup the system ID associated to a public ID """
    ret = libxml2mod.xmlCatalogResolvePublic(pubID)
    return ret

def catalogResolveSystem(sysID):
    """Try to lookup the catalog resource for a system ID """
    ret = libxml2mod.xmlCatalogResolveSystem(sysID)
    return ret

def catalogResolveURI(URI):
    """Do a complete resolution lookup of an URI """
    ret = libxml2mod.xmlCatalogResolveURI(URI)
    return ret

def catalogSetDebug(level):
    """Used to set the debug level for catalog operation, 0
       disable debugging, 1 enable it """
    ret = libxml2mod.xmlCatalogSetDebug(level)
    return ret

def initializeCatalog():
    """Do the catalog initialization. this function is not thread
       safe, catalog initialization should preferably be done
       once at startup """
    libxml2mod.xmlInitializeCatalog()

def loadACatalog(filename):
    """Load the catalog and build the associated data structures.
       This can be either an XML Catalog or an SGML Catalog It
       will recurse in SGML CATALOG entries. On the other hand
       XML Catalogs are not handled recursively. """
    ret = libxml2mod.xmlLoadACatalog(filename)
    if ret is None:raise treeError('xmlLoadACatalog() failed')
    return catalog(_obj=ret)

def loadCatalog(filename):
    """Load the catalog and makes its definitions effective for
       the default external entity loader. It will recurse in
       SGML CATALOG entries. this function is not thread safe,
       catalog initialization should preferably be done once at
       startup """
    ret = libxml2mod.xmlLoadCatalog(filename)
    return ret

def loadCatalogs(pathss):
    """Load the catalogs and makes their definitions effective for
       the default external entity loader. this function is not
       thread safe, catalog initialization should preferably be
       done once at startup """
    libxml2mod.xmlLoadCatalogs(pathss)

def loadSGMLSuperCatalog(filename):
    """Load an SGML super catalog. It won't expand CATALOG or
       DELEGATE references. This is only needed for manipulating
       SGML Super Catalogs like adding and removing CATALOG or
       DELEGATE entries. """
    ret = libxml2mod.xmlLoadSGMLSuperCatalog(filename)
    if ret is None:raise treeError('xmlLoadSGMLSuperCatalog() failed')
    return catalog(_obj=ret)

def newCatalog(sgml):
    """create a new Catalog. """
    ret = libxml2mod.xmlNewCatalog(sgml)
    if ret is None:raise treeError('xmlNewCatalog() failed')
    return catalog(_obj=ret)

def parseCatalogFile(filename):
    """parse an XML file and build a tree. It's like
       xmlParseFile() except it bypass all catalog lookups. """
    ret = libxml2mod.xmlParseCatalogFile(filename)
    if ret is None:raise parserError('xmlParseCatalogFile() failed')
    return xmlDoc(_obj=ret)

#
# Functions from module debugXML
#

def boolToText(boolval):
    """Convenient way to turn bool into text """
    ret = libxml2mod.xmlBoolToText(boolval)
    return ret

def debugDumpString(output, str):
    """Dumps informations about the string, shorten it if necessary """
    libxml2mod.xmlDebugDumpString(output, str)

def shellPrintXPathError(errorType, arg):
    """Print the xpath error to libxml default error channel """
    libxml2mod.xmlShellPrintXPathError(errorType, arg)

#
# Functions from module encoding
#

def UTF8Strlen(utf):
    """compute the length of an UTF8 string, it doesn't do a full
       UTF8 checking of the content of the string. """
    ret = libxml2mod.xmlUTF8Strlen(utf)
    return ret

def UTF8Strloc(utf, utfchar):
    """a function to provide relative location of a UTF8 char """
    ret = libxml2mod.xmlUTF8Strloc(utf, utfchar)
    return ret

def UTF8Strndup(utf, len):
    """a strndup for array of UTF8's """
    ret = libxml2mod.xmlUTF8Strndup(utf, len)
    return ret

def UTF8Strpos(utf, pos):
    """a function to provide the equivalent of fetching a
       character from a string array """
    ret = libxml2mod.xmlUTF8Strpos(utf, pos)
    return ret

def UTF8Strsize(utf, len):
    """storage size of an UTF8 string """
    ret = libxml2mod.xmlUTF8Strsize(utf, len)
    return ret

def UTF8Strsub(utf, start, len):
    """Note:  positions are given in units of UTF-8 chars """
    ret = libxml2mod.xmlUTF8Strsub(utf, start, len)
    return ret

def addEncodingAlias(name, alias):
    """Registers and alias @alias for an encoding named @name.
       Existing alias will be overwritten. """
    ret = libxml2mod.xmlAddEncodingAlias(name, alias)
    return ret

def checkUTF8(utf):
    """Checks @utf for being valid utf-8. @utf is assumed to be
       null-terminated. This function is not super-strict, as it
       will allow longer utf-8 sequences than necessary. Note
       that Java is capable of producing these sequences if
       provoked. Also note, this routine checks for the 4-byte
       maximum size, but does not check for 0x10ffff maximum
       value. """
    ret = libxml2mod.xmlCheckUTF8(utf)
    return ret

def cleanupCharEncodingHandlers():
    """Cleanup the memory allocated for the char encoding support,
       it unregisters all the encoding handlers and the aliases. """
    libxml2mod.xmlCleanupCharEncodingHandlers()

def cleanupEncodingAliases():
    """Unregisters all aliases """
    libxml2mod.xmlCleanupEncodingAliases()

def delEncodingAlias(alias):
    """Unregisters an encoding alias @alias """
    ret = libxml2mod.xmlDelEncodingAlias(alias)
    return ret

def encodingAlias(alias):
    """Lookup an encoding name for the given alias. """
    ret = libxml2mod.xmlGetEncodingAlias(alias)
    return ret

def initCharEncodingHandlers():
    """Initialize the char encoding support, it registers the
       default encoding supported. NOTE: while public, this
       function usually doesn't need to be called in normal
       processing. """
    libxml2mod.xmlInitCharEncodingHandlers()

#
# Functions from module entities
#

def cleanupPredefinedEntities():
    """Cleanup up the predefined entities table. """
    libxml2mod.xmlCleanupPredefinedEntities()

def initializePredefinedEntities():
    """Set up the predefined entities. """
    libxml2mod.xmlInitializePredefinedEntities()

def predefinedEntity(name):
    """Check whether this name is an predefined entity. """
    ret = libxml2mod.xmlGetPredefinedEntity(name)
    if ret is None:raise treeError('xmlGetPredefinedEntity() failed')
    return xmlEntity(_obj=ret)

#
# Functions from module nanoftp
#

def nanoFTPCleanup():
    """Cleanup the FTP protocol layer. This cleanup proxy
       informations. """
    libxml2mod.xmlNanoFTPCleanup()

def nanoFTPInit():
    """Initialize the FTP protocol layer. Currently it just checks
       for proxy informations, and get the hostname """
    libxml2mod.xmlNanoFTPInit()

def nanoFTPProxy(host, port, user, passwd, type):
    """Setup the FTP proxy informations. This can also be done by
       using ftp_proxy ftp_proxy_user and ftp_proxy_password
       environment variables. """
    libxml2mod.xmlNanoFTPProxy(host, port, user, passwd, type)

def nanoFTPScanProxy(URL):
    """(Re)Initialize the FTP Proxy context by parsing the URL and
       finding the protocol host port it indicates. Should be
       like ftp://myproxy/ or ftp://myproxy:3128/ A None URL
       cleans up proxy informations. """
    libxml2mod.xmlNanoFTPScanProxy(URL)

#
# Functions from module nanohttp
#

def nanoHTTPCleanup():
    """Cleanup the HTTP protocol layer. """
    libxml2mod.xmlNanoHTTPCleanup()

def nanoHTTPInit():
    """Initialize the HTTP protocol layer. Currently it just
       checks for proxy informations """
    libxml2mod.xmlNanoHTTPInit()

def nanoHTTPScanProxy(URL):
    """(Re)Initialize the HTTP Proxy context by parsing the URL
       and finding the protocol host port it indicates. Should be
       like http://myproxy/ or http://myproxy:3128/ A None URL
       cleans up proxy informations. """
    libxml2mod.xmlNanoHTTPScanProxy(URL)

#
# Functions from module parser
#

def cleanupParser():
    """Cleanup function for the XML parser. It tries to reclaim
       all parsing related global memory allocated for the parser
       processing. It doesn't deallocate any document related
       memory. Calling this function should not prevent reusing
       the parser. One should call xmlCleanupParser() only when
       the process has finished using the library or XML document
       built with it. """
    libxml2mod.xmlCleanupParser()

def createDocParserCtxt(cur):
    """Creates a parser context for an XML in-memory document. """
    ret = libxml2mod.xmlCreateDocParserCtxt(cur)
    if ret is None:raise parserError('xmlCreateDocParserCtxt() failed')
    return parserCtxt(_obj=ret)

def initParser():
    """Initialization function for the XML parser. This is not
       reentrant. Call once before processing in case of use in
       multithreaded programs. """
    libxml2mod.xmlInitParser()

def keepBlanksDefault(val):
    """Set and return the previous value for default blanks text
       nodes support. The 1.x version of the parser used an
       heuristic to try to detect ignorable white spaces. As a
       result the SAX callback was generating
       ignorableWhitespace() callbacks instead of characters()
       one, and when using the DOM output text nodes containing
       those blanks were not generated. The 2.x and later version
       will switch to the XML standard way and
       ignorableWhitespace() are only generated when running the
       parser in validating mode and when the current element
       doesn't allow CDATA or mixed content. This function is
       provided as a way to force the standard behavior on 1.X
       libs and to switch back to the old mode for compatibility
       when running 1.X client code on 2.X . Upgrade of 1.X code
       should be done by using xmlIsBlankNode() commodity
       function to detect the "empty" nodes generated. This value
       also affect autogeneration of indentation when saving code
       if blanks sections are kept, indentation is not generated. """
    ret = libxml2mod.xmlKeepBlanksDefault(val)
    return ret

def lineNumbersDefault(val):
    """Set and return the previous value for enabling line numbers
       in elements contents. This may break on old application
       and is turned off by default. """
    ret = libxml2mod.xmlLineNumbersDefault(val)
    return ret

def parseDTD(ExternalID, SystemID):
    """Load and parse an external subset. """
    ret = libxml2mod.xmlParseDTD(ExternalID, SystemID)
    if ret is None:raise parserError('xmlParseDTD() failed')
    return xmlDtd(_obj=ret)

def parseDoc(cur):
    """parse an XML in-memory document and build a tree. """
    ret = libxml2mod.xmlParseDoc(cur)
    if ret is None:raise parserError('xmlParseDoc() failed')
    return xmlDoc(_obj=ret)

def parseEntity(filename):
    """parse an XML external entity out of context and build a
       tree.  [78] extParsedEnt ::= TextDecl? content  This
       correspond to a "Well Balanced" chunk """
    ret = libxml2mod.xmlParseEntity(filename)
    if ret is None:raise parserError('xmlParseEntity() failed')
    return xmlDoc(_obj=ret)

def parseFile(filename):
    """parse an XML file and build a tree. Automatic support for
       ZLIB/Compress compressed document is provided by default
       if found at compile-time. """
    ret = libxml2mod.xmlParseFile(filename)
    if ret is None:raise parserError('xmlParseFile() failed')
    return xmlDoc(_obj=ret)

def parseMemory(buffer, size):
    """parse an XML in-memory block and build a tree. """
    ret = libxml2mod.xmlParseMemory(buffer, size)
    if ret is None:raise parserError('xmlParseMemory() failed')
    return xmlDoc(_obj=ret)

def pedanticParserDefault(val):
    """Set and return the previous value for enabling pedantic
       warnings. """
    ret = libxml2mod.xmlPedanticParserDefault(val)
    return ret

def recoverDoc(cur):
    """parse an XML in-memory document and build a tree. In the
       case the document is not Well Formed, a tree is built
       anyway """
    ret = libxml2mod.xmlRecoverDoc(cur)
    if ret is None:raise treeError('xmlRecoverDoc() failed')
    return xmlDoc(_obj=ret)

def recoverFile(filename):
    """parse an XML file and build a tree. Automatic support for
       ZLIB/Compress compressed document is provided by default
       if found at compile-time. In the case the document is not
       Well Formed, a tree is built anyway """
    ret = libxml2mod.xmlRecoverFile(filename)
    if ret is None:raise treeError('xmlRecoverFile() failed')
    return xmlDoc(_obj=ret)

def recoverMemory(buffer, size):
    """parse an XML in-memory block and build a tree. In the case
       the document is not Well Formed, a tree is built anyway """
    ret = libxml2mod.xmlRecoverMemory(buffer, size)
    if ret is None:raise treeError('xmlRecoverMemory() failed')
    return xmlDoc(_obj=ret)

def substituteEntitiesDefault(val):
    """Set and return the previous value for default entity
       support. Initially the parser always keep entity
       references instead of substituting entity values in the
       output. This function has to be used to change the default
       parser behavior SAX::substituteEntities() has to be used
       for changing that on a file by file basis. """
    ret = libxml2mod.xmlSubstituteEntitiesDefault(val)
    return ret

#
# Functions from module parserInternals
#

def checkLanguageID(lang):
    """Checks that the value conforms to the LanguageID
       production:  NOTE: this is somewhat deprecated, those
       productions were removed from the XML Second edition. 
       [33] LanguageID ::= Langcode ('-' Subcode)* [34] Langcode
       ::= ISO639Code |  IanaCode |  UserCode [35] ISO639Code ::=
       ([a-z] | [A-Z]) ([a-z] | [A-Z]) [36] IanaCode ::= ('i' |
       'I') '-' ([a-z] | [A-Z])+ [37] UserCode ::= ('x' | 'X')
       '-' ([a-z] | [A-Z])+ [38] Subcode ::= ([a-z] | [A-Z])+ """
    ret = libxml2mod.xmlCheckLanguageID(lang)
    return ret

def copyChar(len, out, val):
    """append the char value in the array """
    ret = libxml2mod.xmlCopyChar(len, out, val)
    return ret

def copyCharMultiByte(out, val):
    """append the char value in the array """
    ret = libxml2mod.xmlCopyCharMultiByte(out, val)
    return ret

def createEntityParserCtxt(URL, ID, base):
    """Create a parser context for an external entity Automatic
       support for ZLIB/Compress compressed document is provided
       by default if found at compile-time. """
    ret = libxml2mod.xmlCreateEntityParserCtxt(URL, ID, base)
    if ret is None:raise parserError('xmlCreateEntityParserCtxt() failed')
    return parserCtxt(_obj=ret)

def createFileParserCtxt(filename):
    """Create a parser context for a file content. Automatic
       support for ZLIB/Compress compressed document is provided
       by default if found at compile-time. """
    ret = libxml2mod.xmlCreateFileParserCtxt(filename)
    if ret is None:raise parserError('xmlCreateFileParserCtxt() failed')
    return parserCtxt(_obj=ret)

def createMemoryParserCtxt(buffer, size):
    """Create a parser context for an XML in-memory document. """
    ret = libxml2mod.xmlCreateMemoryParserCtxt(buffer, size)
    if ret is None:raise parserError('xmlCreateMemoryParserCtxt() failed')
    return parserCtxt(_obj=ret)

def htmlCreateFileParserCtxt(filename, encoding):
    """Create a parser context for a file content. Automatic
       support for ZLIB/Compress compressed document is provided
       by default if found at compile-time. """
    ret = libxml2mod.htmlCreateFileParserCtxt(filename, encoding)
    if ret is None:raise parserError('htmlCreateFileParserCtxt() failed')
    return parserCtxt(_obj=ret)

def htmlInitAutoClose():
    """Initialize the htmlStartCloseIndex for fast lookup of
       closing tags names. This is not reentrant. Call
       xmlInitParser() once before processing in case of use in
       multithreaded programs. """
    libxml2mod.htmlInitAutoClose()

def isBaseChar(c):
    """Check whether the character is allowed by the production
       [85] BaseChar ::= ... long list see REC ...  VI is your
       friend ! :1,$ s/\[#x\([0-9A-Z]*\)-#x\([0-9A-Z]*\)\]/    
       (((c) >= 0x\1) \&\& ((c) <= 0x\2)) ||/ and :1,$
       s/#x\([0-9A-Z]*\)/     ((c) == 0x\1) ||/ """
    ret = libxml2mod.xmlIsBaseChar(c)
    return ret

def isBlank(c):
    """Check whether the character is allowed by the production
       [3] S ::= (#x20 | #x9 | #xD | #xA)+ Also available as a
       macro IS_BLANK() """
    ret = libxml2mod.xmlIsBlank(c)
    return ret

def isChar(c):
    """Check whether the character is allowed by the production
       [2] Char ::= #x9 | #xA | #xD | [#x20-#xD7FF] |
       [#xE000-#xFFFD] | [#x10000-#x10FFFF] any Unicode
       character, excluding the surrogate blocks, FFFE, and FFFF.
       Also available as a macro IS_CHAR() """
    ret = libxml2mod.xmlIsChar(c)
    return ret

def isCombining(c):
    """Check whether the character is allowed by the production
       [87] CombiningChar ::= ... long list see REC ... """
    ret = libxml2mod.xmlIsCombining(c)
    return ret

def isDigit(c):
    """Check whether the character is allowed by the production
       [88] Digit ::= ... long list see REC ... """
    ret = libxml2mod.xmlIsDigit(c)
    return ret

def isExtender(c):
    """Check whether the character is allowed by the production
       [89] Extender ::= #x00B7 | #x02D0 | #x02D1 | #x0387 |
       #x0640 | #x0E46 | #x0EC6 | #x3005 | [#x3031-#x3035] |
       [#x309D-#x309E] | [#x30FC-#x30FE] """
    ret = libxml2mod.xmlIsExtender(c)
    return ret

def isIdeographic(c):
    """Check whether the character is allowed by the production
       [86] Ideographic ::= [#x4E00-#x9FA5] | #x3007 |
       [#x3021-#x3029] """
    ret = libxml2mod.xmlIsIdeographic(c)
    return ret

def isLetter(c):
    """Check whether the character is allowed by the production
       [84] Letter ::= BaseChar | Ideographic """
    ret = libxml2mod.xmlIsLetter(c)
    return ret

def isPubidChar(c):
    """Check whether the character is allowed by the production
       [13] PubidChar ::= #x20 | #xD | #xA | [a-zA-Z0-9] |
       [-'()+,./:=?;!*#@$_%] """
    ret = libxml2mod.xmlIsPubidChar(c)
    return ret

def namePop(ctxt):
    """Pops the top element name from the name stack """
    if ctxt is None: ctxt__o = None
    else: ctxt__o = ctxt._o
    ret = libxml2mod.namePop(ctxt__o)
    return ret

def namePush(ctxt, value):
    """Pushes a new element name on top of the name stack """
    if ctxt is None: ctxt__o = None
    else: ctxt__o = ctxt._o
    ret = libxml2mod.namePush(ctxt__o, value)
    return ret

def newParserCtxt():
    """Allocate and initialize a new parser context. """
    ret = libxml2mod.xmlNewParserCtxt()
    if ret is None:raise parserError('xmlNewParserCtxt() failed')
    return parserCtxt(_obj=ret)

def nodePop(ctxt):
    """Pops the top element node from the node stack """
    if ctxt is None: ctxt__o = None
    else: ctxt__o = ctxt._o
    ret = libxml2mod.nodePop(ctxt__o)
    if ret is None:raise treeError('nodePop() failed')
    return xmlNode(_obj=ret)

def nodePush(ctxt, value):
    """Pushes a new element node on top of the node stack """
    if ctxt is None: ctxt__o = None
    else: ctxt__o = ctxt._o
    if value is None: value__o = None
    else: value__o = value._o
    ret = libxml2mod.nodePush(ctxt__o, value__o)
    return ret

#
# Functions from module python
#

def SAXParseFile(SAX, URI, recover):
    """Interface to parse an XML file or resource pointed by an
       URI to build an event flow to the SAX object """
    libxml2mod.xmlSAXParseFile(SAX, URI, recover)

def createInputBuffer(file, encoding):
    """Create a libxml2 input buffer from a Python file """
    ret = libxml2mod.xmlCreateInputBuffer(file, encoding)
    if ret is None:raise treeError('xmlCreateInputBuffer() failed')
    return inputBuffer(_obj=ret)

def createOutputBuffer(file, encoding):
    """Create a libxml2 output buffer from a Python file """
    ret = libxml2mod.xmlCreateOutputBuffer(file, encoding)
    if ret is None:raise treeError('xmlCreateOutputBuffer() failed')
    return outputBuffer(_obj=ret)

def createPushParser(SAX, chunk, size, URI):
    """Create a progressive XML parser context to build either an
       event flow if the SAX object is not None, or a DOM tree
       otherwise. """
    ret = libxml2mod.xmlCreatePushParser(SAX, chunk, size, URI)
    if ret is None:raise parserError('xmlCreatePushParser() failed')
    return parserCtxt(_obj=ret)

def debugMemory(activate):
    """Switch on the generation of line number for elements nodes.
       Also returns the number of bytes allocated and not freed
       by libxml2 since memory debugging was switched on. """
    ret = libxml2mod.xmlDebugMemory(activate)
    return ret

def dumpMemory():
    """dump the memory allocated in the file .memdump """
    libxml2mod.xmlDumpMemory()

def htmlCreatePushParser(SAX, chunk, size, URI):
    """Create a progressive HTML parser context to build either an
       event flow if the SAX object is not None, or a DOM tree
       otherwise. """
    ret = libxml2mod.htmlCreatePushParser(SAX, chunk, size, URI)
    if ret is None:raise parserError('htmlCreatePushParser() failed')
    return parserCtxt(_obj=ret)

def htmlSAXParseFile(SAX, URI, encoding):
    """Interface to parse an HTML file or resource pointed by an
       URI to build an event flow to the SAX object """
    libxml2mod.htmlSAXParseFile(SAX, URI, encoding)

def newNode(name):
    """Create a new Node """
    ret = libxml2mod.xmlNewNode(name)
    if ret is None:raise treeError('xmlNewNode() failed')
    return xmlNode(_obj=ret)

def setEntityLoader(resolver):
    """Set the entity resolver as a python function """
    ret = libxml2mod.xmlSetEntityLoader(resolver)
    return ret

#
# Functions from module relaxng
#

def relaxNGCleanupTypes():
    """Cleanup the default Schemas type library associated to
       RelaxNG """
    libxml2mod.xmlRelaxNGCleanupTypes()

def relaxNGNewMemParserCtxt(buffer, size):
    """Create an XML RelaxNGs parse context for that memory buffer
       expected to contain an XML RelaxNGs file. """
    ret = libxml2mod.xmlRelaxNGNewMemParserCtxt(buffer, size)
    if ret is None:raise parserError('xmlRelaxNGNewMemParserCtxt() failed')
    return relaxNgParserCtxt(_obj=ret)

def relaxNGNewParserCtxt(URL):
    """Create an XML RelaxNGs parse context for that file/resource
       expected to contain an XML RelaxNGs file. """
    ret = libxml2mod.xmlRelaxNGNewParserCtxt(URL)
    if ret is None:raise parserError('xmlRelaxNGNewParserCtxt() failed')
    return relaxNgParserCtxt(_obj=ret)

#
# Functions from module tree
#

def compressMode():
    """get the default compression mode used, ZLIB based. """
    ret = libxml2mod.xmlGetCompressMode()
    return ret

def isXHTML(systemID, publicID):
    """Try to find if the document correspond to an XHTML DTD """
    ret = libxml2mod.xmlIsXHTML(systemID, publicID)
    return ret

def newComment(content):
    """Creation of a new node containing a comment. """
    ret = libxml2mod.xmlNewComment(content)
    if ret is None:raise treeError('xmlNewComment() failed')
    return xmlNode(_obj=ret)

def newDoc(version):
    """Creates a new XML document """
    ret = libxml2mod.xmlNewDoc(version)
    if ret is None:raise treeError('xmlNewDoc() failed')
    return xmlDoc(_obj=ret)

def newPI(name, content):
    """Creation of a processing instruction element. """
    ret = libxml2mod.xmlNewPI(name, content)
    if ret is None:raise treeError('xmlNewPI() failed')
    return xmlNode(_obj=ret)

def newText(content):
    """Creation of a new text node. """
    ret = libxml2mod.xmlNewText(content)
    if ret is None:raise treeError('xmlNewText() failed')
    return xmlNode(_obj=ret)

def newTextLen(content, len):
    """Creation of a new text node with an extra parameter for the
       content's length """
    ret = libxml2mod.xmlNewTextLen(content, len)
    if ret is None:raise treeError('xmlNewTextLen() failed')
    return xmlNode(_obj=ret)

def setCompressMode(mode):
    """set the default compression mode used, ZLIB based Correct
       values: 0 (uncompressed) to 9 (max compression) """
    libxml2mod.xmlSetCompressMode(mode)

def validateNCName(value, space):
    """Check that a value conforms to the lexical space of NCName """
    ret = libxml2mod.xmlValidateNCName(value, space)
    return ret

def validateNMToken(value, space):
    """Check that a value conforms to the lexical space of NMToken """
    ret = libxml2mod.xmlValidateNMToken(value, space)
    return ret

def validateName(value, space):
    """Check that a value conforms to the lexical space of Name """
    ret = libxml2mod.xmlValidateName(value, space)
    return ret

def validateQName(value, space):
    """Check that a value conforms to the lexical space of QName """
    ret = libxml2mod.xmlValidateQName(value, space)
    return ret

#
# Functions from module uri
#

def URIEscape(str):
    """Escaping routine, does not do validity checks ! It will try
       to escape the chars needing this, but this is heuristic
       based it's impossible to be sure. """
    ret = libxml2mod.xmlURIEscape(str)
    return ret

def URIEscapeStr(str, list):
    """This routine escapes a string to hex, ignoring reserved
       characters (a-z) and the characters in the exception list. """
    ret = libxml2mod.xmlURIEscapeStr(str, list)
    return ret

def URIUnescapeString(str, len, target):
    """Unescaping routine, does not do validity checks ! Output is
       direct unsigned char translation of %XX values (no
       encoding) """
    ret = libxml2mod.xmlURIUnescapeString(str, len, target)
    return ret

def buildURI(URI, base):
    """Computes he final URI of the reference done by checking
       that the given URI is valid, and building the final URI
       using the base URI. This is processed according to section
       5.2 of the RFC 2396  5.2. Resolving Relative References to
       Absolute Form """
    ret = libxml2mod.xmlBuildURI(URI, base)
    return ret

def canonicPath(path):
    """Constructs a canonic path from the specified path. """
    ret = libxml2mod.xmlCanonicPath(path)
    return ret

def createURI():
    """Simply creates an empty xmlURI """
    ret = libxml2mod.xmlCreateURI()
    if ret is None:raise uriError('xmlCreateURI() failed')
    return URI(_obj=ret)

def normalizeURIPath(path):
    """Applies the 5 normalization steps to a path string--that
       is, RFC 2396 Section 5.2, steps 6.c through 6.g. 
       Normalization occurs directly on the string, no new
       allocation is done """
    ret = libxml2mod.xmlNormalizeURIPath(path)
    return ret

def parseURI(str):
    """Parse an URI  URI-reference = [ absoluteURI | relativeURI ]
       [ "#" fragment ] """
    ret = libxml2mod.xmlParseURI(str)
    if ret is None:raise uriError('xmlParseURI() failed')
    return URI(_obj=ret)

#
# Functions from module valid
#

def validateNameValue(value):
    """Validate that the given value match Name production """
    ret = libxml2mod.xmlValidateNameValue(value)
    return ret

def validateNamesValue(value):
    """Validate that the given value match Names production """
    ret = libxml2mod.xmlValidateNamesValue(value)
    return ret

def validateNmtokenValue(value):
    """Validate that the given value match Nmtoken production  [
       VC: Name Token ] """
    ret = libxml2mod.xmlValidateNmtokenValue(value)
    return ret

def validateNmtokensValue(value):
    """Validate that the given value match Nmtokens production  [
       VC: Name Token ] """
    ret = libxml2mod.xmlValidateNmtokensValue(value)
    return ret

#
# Functions from module xmlIO
#

def checkFilename(path):
    """function checks to see if @path is a valid source (file,
       socket...) for XML.  if stat is not available on the
       target machine, """
    ret = libxml2mod.xmlCheckFilename(path)
    return ret

def cleanupInputCallbacks():
    """clears the entire input callback table. this includes the
       compiled-in I/O. """
    libxml2mod.xmlCleanupInputCallbacks()

def cleanupOutputCallbacks():
    """clears the entire output callback table. this includes the
       compiled-in I/O callbacks. """
    libxml2mod.xmlCleanupOutputCallbacks()

def fileMatch(filename):
    """input from FILE * """
    ret = libxml2mod.xmlFileMatch(filename)
    return ret

def iOFTPMatch(filename):
    """check if the URI matches an FTP one """
    ret = libxml2mod.xmlIOFTPMatch(filename)
    return ret

def iOHTTPMatch(filename):
    """check if the URI matches an HTTP one """
    ret = libxml2mod.xmlIOHTTPMatch(filename)
    return ret

def normalizeWindowsPath(path):
    """This function is obsolete. Please see xmlURIFromPath in
       uri.c for a better solution. """
    ret = libxml2mod.xmlNormalizeWindowsPath(path)
    return ret

def parserGetDirectory(filename):
    """lookup the directory for that file """
    ret = libxml2mod.xmlParserGetDirectory(filename)
    return ret

def registerDefaultInputCallbacks():
    """Registers the default compiled-in I/O handlers. """
    libxml2mod.xmlRegisterDefaultInputCallbacks()

def registerDefaultOutputCallbacks():
    """Registers the default compiled-in I/O handlers. """
    libxml2mod.xmlRegisterDefaultOutputCallbacks()

def registerHTTPPostCallbacks():
    """By default, libxml submits HTTP output requests using the
       "PUT" method. Calling this method changes the HTTP output
       method to use the "POST" method instead. """
    libxml2mod.xmlRegisterHTTPPostCallbacks()

#
# Functions from module xmlreader
#

def newTextReaderFilename(URI):
    """Create an xmlTextReader structure fed with the resource at
       @URI """
    ret = libxml2mod.xmlNewTextReaderFilename(URI)
    if ret is None:raise treeError('xmlNewTextReaderFilename() failed')
    return xmlTextReader(_obj=ret)

#
# Functions from module xmlregexp
#

def regexpCompile(regexp):
    """Parses a regular expression conforming to XML Schemas Part
       2 Datatype Appendix F and build an automata suitable for
       testing strings against that regular expression """
    ret = libxml2mod.xmlRegexpCompile(regexp)
    if ret is None:raise treeError('xmlRegexpCompile() failed')
    return xmlReg(_obj=ret)

#
# Functions from module xmlunicode
#

def uCSIsAlphabeticPresentationForms(code):
    """Check whether the character is part of
       AlphabeticPresentationForms UCS Block """
    ret = libxml2mod.xmlUCSIsAlphabeticPresentationForms(code)
    return ret

def uCSIsArabic(code):
    """Check whether the character is part of Arabic UCS Block """
    ret = libxml2mod.xmlUCSIsArabic(code)
    return ret

def uCSIsArabicPresentationFormsA(code):
    """Check whether the character is part of
       ArabicPresentationForms-A UCS Block """
    ret = libxml2mod.xmlUCSIsArabicPresentationFormsA(code)
    return ret

def uCSIsArabicPresentationFormsB(code):
    """Check whether the character is part of
       ArabicPresentationForms-B UCS Block """
    ret = libxml2mod.xmlUCSIsArabicPresentationFormsB(code)
    return ret

def uCSIsArmenian(code):
    """Check whether the character is part of Armenian UCS Block """
    ret = libxml2mod.xmlUCSIsArmenian(code)
    return ret

def uCSIsArrows(code):
    """Check whether the character is part of Arrows UCS Block """
    ret = libxml2mod.xmlUCSIsArrows(code)
    return ret

def uCSIsBasicLatin(code):
    """Check whether the character is part of BasicLatin UCS Block """
    ret = libxml2mod.xmlUCSIsBasicLatin(code)
    return ret

def uCSIsBengali(code):
    """Check whether the character is part of Bengali UCS Block """
    ret = libxml2mod.xmlUCSIsBengali(code)
    return ret

def uCSIsBlock(code, block):
    """Check whether the caracter is part of the UCS Block """
    ret = libxml2mod.xmlUCSIsBlock(code, block)
    return ret

def uCSIsBlockElements(code):
    """Check whether the character is part of BlockElements UCS
       Block """
    ret = libxml2mod.xmlUCSIsBlockElements(code)
    return ret

def uCSIsBopomofo(code):
    """Check whether the character is part of Bopomofo UCS Block """
    ret = libxml2mod.xmlUCSIsBopomofo(code)
    return ret

def uCSIsBopomofoExtended(code):
    """Check whether the character is part of BopomofoExtended UCS
       Block """
    ret = libxml2mod.xmlUCSIsBopomofoExtended(code)
    return ret

def uCSIsBoxDrawing(code):
    """Check whether the character is part of BoxDrawing UCS Block """
    ret = libxml2mod.xmlUCSIsBoxDrawing(code)
    return ret

def uCSIsBraillePatterns(code):
    """Check whether the character is part of BraillePatterns UCS
       Block """
    ret = libxml2mod.xmlUCSIsBraillePatterns(code)
    return ret

def uCSIsByzantineMusicalSymbols(code):
    """Check whether the character is part of
       ByzantineMusicalSymbols UCS Block """
    ret = libxml2mod.xmlUCSIsByzantineMusicalSymbols(code)
    return ret

def uCSIsCJKCompatibility(code):
    """Check whether the character is part of CJKCompatibility UCS
       Block """
    ret = libxml2mod.xmlUCSIsCJKCompatibility(code)
    return ret

def uCSIsCJKCompatibilityForms(code):
    """Check whether the character is part of
       CJKCompatibilityForms UCS Block """
    ret = libxml2mod.xmlUCSIsCJKCompatibilityForms(code)
    return ret

def uCSIsCJKCompatibilityIdeographs(code):
    """Check whether the character is part of
       CJKCompatibilityIdeographs UCS Block """
    ret = libxml2mod.xmlUCSIsCJKCompatibilityIdeographs(code)
    return ret

def uCSIsCJKCompatibilityIdeographsSupplement(code):
    """Check whether the character is part of
       CJKCompatibilityIdeographsSupplement UCS Block """
    ret = libxml2mod.xmlUCSIsCJKCompatibilityIdeographsSupplement(code)
    return ret

def uCSIsCJKRadicalsSupplement(code):
    """Check whether the character is part of
       CJKRadicalsSupplement UCS Block """
    ret = libxml2mod.xmlUCSIsCJKRadicalsSupplement(code)
    return ret

def uCSIsCJKSymbolsandPunctuation(code):
    """Check whether the character is part of
       CJKSymbolsandPunctuation UCS Block """
    ret = libxml2mod.xmlUCSIsCJKSymbolsandPunctuation(code)
    return ret

def uCSIsCJKUnifiedIdeographs(code):
    """Check whether the character is part of CJKUnifiedIdeographs
       UCS Block """
    ret = libxml2mod.xmlUCSIsCJKUnifiedIdeographs(code)
    return ret

def uCSIsCJKUnifiedIdeographsExtensionA(code):
    """Check whether the character is part of
       CJKUnifiedIdeographsExtensionA UCS Block """
    ret = libxml2mod.xmlUCSIsCJKUnifiedIdeographsExtensionA(code)
    return ret

def uCSIsCJKUnifiedIdeographsExtensionB(code):
    """Check whether the character is part of
       CJKUnifiedIdeographsExtensionB UCS Block """
    ret = libxml2mod.xmlUCSIsCJKUnifiedIdeographsExtensionB(code)
    return ret

def uCSIsCat(code, cat):
    """Check whether the caracter is part of the UCS Category """
    ret = libxml2mod.xmlUCSIsCat(code, cat)
    return ret

def uCSIsCatC(code):
    """Check whether the character is part of C UCS Category """
    ret = libxml2mod.xmlUCSIsCatC(code)
    return ret

def uCSIsCatCc(code):
    """Check whether the character is part of Cc UCS Category """
    ret = libxml2mod.xmlUCSIsCatCc(code)
    return ret

def uCSIsCatCf(code):
    """Check whether the character is part of Cf UCS Category """
    ret = libxml2mod.xmlUCSIsCatCf(code)
    return ret

def uCSIsCatCo(code):
    """Check whether the character is part of Co UCS Category """
    ret = libxml2mod.xmlUCSIsCatCo(code)
    return ret

def uCSIsCatCs(code):
    """Check whether the character is part of Cs UCS Category """
    ret = libxml2mod.xmlUCSIsCatCs(code)
    return ret

def uCSIsCatL(code):
    """Check whether the character is part of L UCS Category """
    ret = libxml2mod.xmlUCSIsCatL(code)
    return ret

def uCSIsCatLl(code):
    """Check whether the character is part of Ll UCS Category """
    ret = libxml2mod.xmlUCSIsCatLl(code)
    return ret

def uCSIsCatLm(code):
    """Check whether the character is part of Lm UCS Category """
    ret = libxml2mod.xmlUCSIsCatLm(code)
    return ret

def uCSIsCatLo(code):
    """Check whether the character is part of Lo UCS Category """
    ret = libxml2mod.xmlUCSIsCatLo(code)
    return ret

def uCSIsCatLt(code):
    """Check whether the character is part of Lt UCS Category """
    ret = libxml2mod.xmlUCSIsCatLt(code)
    return ret

def uCSIsCatLu(code):
    """Check whether the character is part of Lu UCS Category """
    ret = libxml2mod.xmlUCSIsCatLu(code)
    return ret

def uCSIsCatM(code):
    """Check whether the character is part of M UCS Category """
    ret = libxml2mod.xmlUCSIsCatM(code)
    return ret

def uCSIsCatMc(code):
    """Check whether the character is part of Mc UCS Category """
    ret = libxml2mod.xmlUCSIsCatMc(code)
    return ret

def uCSIsCatMe(code):
    """Check whether the character is part of Me UCS Category """
    ret = libxml2mod.xmlUCSIsCatMe(code)
    return ret

def uCSIsCatMn(code):
    """Check whether the character is part of Mn UCS Category """
    ret = libxml2mod.xmlUCSIsCatMn(code)
    return ret

def uCSIsCatN(code):
    """Check whether the character is part of N UCS Category """
    ret = libxml2mod.xmlUCSIsCatN(code)
    return ret

def uCSIsCatNd(code):
    """Check whether the character is part of Nd UCS Category """
    ret = libxml2mod.xmlUCSIsCatNd(code)
    return ret

def uCSIsCatNl(code):
    """Check whether the character is part of Nl UCS Category """
    ret = libxml2mod.xmlUCSIsCatNl(code)
    return ret

def uCSIsCatNo(code):
    """Check whether the character is part of No UCS Category """
    ret = libxml2mod.xmlUCSIsCatNo(code)
    return ret

def uCSIsCatP(code):
    """Check whether the character is part of P UCS Category """
    ret = libxml2mod.xmlUCSIsCatP(code)
    return ret

def uCSIsCatPc(code):
    """Check whether the character is part of Pc UCS Category """
    ret = libxml2mod.xmlUCSIsCatPc(code)
    return ret

def uCSIsCatPd(code):
    """Check whether the character is part of Pd UCS Category """
    ret = libxml2mod.xmlUCSIsCatPd(code)
    return ret

def uCSIsCatPe(code):
    """Check whether the character is part of Pe UCS Category """
    ret = libxml2mod.xmlUCSIsCatPe(code)
    return ret

def uCSIsCatPf(code):
    """Check whether the character is part of Pf UCS Category """
    ret = libxml2mod.xmlUCSIsCatPf(code)
    return ret

def uCSIsCatPi(code):
    """Check whether the character is part of Pi UCS Category """
    ret = libxml2mod.xmlUCSIsCatPi(code)
    return ret

def uCSIsCatPo(code):
    """Check whether the character is part of Po UCS Category """
    ret = libxml2mod.xmlUCSIsCatPo(code)
    return ret

def uCSIsCatPs(code):
    """Check whether the character is part of Ps UCS Category """
    ret = libxml2mod.xmlUCSIsCatPs(code)
    return ret

def uCSIsCatS(code):
    """Check whether the character is part of S UCS Category """
    ret = libxml2mod.xmlUCSIsCatS(code)
    return ret

def uCSIsCatSc(code):
    """Check whether the character is part of Sc UCS Category """
    ret = libxml2mod.xmlUCSIsCatSc(code)
    return ret

def uCSIsCatSk(code):
    """Check whether the character is part of Sk UCS Category """
    ret = libxml2mod.xmlUCSIsCatSk(code)
    return ret

def uCSIsCatSm(code):
    """Check whether the character is part of Sm UCS Category """
    ret = libxml2mod.xmlUCSIsCatSm(code)
    return ret

def uCSIsCatSo(code):
    """Check whether the character is part of So UCS Category """
    ret = libxml2mod.xmlUCSIsCatSo(code)
    return ret

def uCSIsCatZ(code):
    """Check whether the character is part of Z UCS Category """
    ret = libxml2mod.xmlUCSIsCatZ(code)
    return ret

def uCSIsCatZl(code):
    """Check whether the character is part of Zl UCS Category """
    ret = libxml2mod.xmlUCSIsCatZl(code)
    return ret

def uCSIsCatZp(code):
    """Check whether the character is part of Zp UCS Category """
    ret = libxml2mod.xmlUCSIsCatZp(code)
    return ret

def uCSIsCatZs(code):
    """Check whether the character is part of Zs UCS Category """
    ret = libxml2mod.xmlUCSIsCatZs(code)
    return ret

def uCSIsCherokee(code):
    """Check whether the character is part of Cherokee UCS Block """
    ret = libxml2mod.xmlUCSIsCherokee(code)
    return ret

def uCSIsCombiningDiacriticalMarks(code):
    """Check whether the character is part of
       CombiningDiacriticalMarks UCS Block """
    ret = libxml2mod.xmlUCSIsCombiningDiacriticalMarks(code)
    return ret

def uCSIsCombiningHalfMarks(code):
    """Check whether the character is part of CombiningHalfMarks
       UCS Block """
    ret = libxml2mod.xmlUCSIsCombiningHalfMarks(code)
    return ret

def uCSIsCombiningMarksforSymbols(code):
    """Check whether the character is part of
       CombiningMarksforSymbols UCS Block """
    ret = libxml2mod.xmlUCSIsCombiningMarksforSymbols(code)
    return ret

def uCSIsControlPictures(code):
    """Check whether the character is part of ControlPictures UCS
       Block """
    ret = libxml2mod.xmlUCSIsControlPictures(code)
    return ret

def uCSIsCurrencySymbols(code):
    """Check whether the character is part of CurrencySymbols UCS
       Block """
    ret = libxml2mod.xmlUCSIsCurrencySymbols(code)
    return ret

def uCSIsCyrillic(code):
    """Check whether the character is part of Cyrillic UCS Block """
    ret = libxml2mod.xmlUCSIsCyrillic(code)
    return ret

def uCSIsDeseret(code):
    """Check whether the character is part of Deseret UCS Block """
    ret = libxml2mod.xmlUCSIsDeseret(code)
    return ret

def uCSIsDevanagari(code):
    """Check whether the character is part of Devanagari UCS Block """
    ret = libxml2mod.xmlUCSIsDevanagari(code)
    return ret

def uCSIsDingbats(code):
    """Check whether the character is part of Dingbats UCS Block """
    ret = libxml2mod.xmlUCSIsDingbats(code)
    return ret

def uCSIsEnclosedAlphanumerics(code):
    """Check whether the character is part of
       EnclosedAlphanumerics UCS Block """
    ret = libxml2mod.xmlUCSIsEnclosedAlphanumerics(code)
    return ret

def uCSIsEnclosedCJKLettersandMonths(code):
    """Check whether the character is part of
       EnclosedCJKLettersandMonths UCS Block """
    ret = libxml2mod.xmlUCSIsEnclosedCJKLettersandMonths(code)
    return ret

def uCSIsEthiopic(code):
    """Check whether the character is part of Ethiopic UCS Block """
    ret = libxml2mod.xmlUCSIsEthiopic(code)
    return ret

def uCSIsGeneralPunctuation(code):
    """Check whether the character is part of GeneralPunctuation
       UCS Block """
    ret = libxml2mod.xmlUCSIsGeneralPunctuation(code)
    return ret

def uCSIsGeometricShapes(code):
    """Check whether the character is part of GeometricShapes UCS
       Block """
    ret = libxml2mod.xmlUCSIsGeometricShapes(code)
    return ret

def uCSIsGeorgian(code):
    """Check whether the character is part of Georgian UCS Block """
    ret = libxml2mod.xmlUCSIsGeorgian(code)
    return ret

def uCSIsGothic(code):
    """Check whether the character is part of Gothic UCS Block """
    ret = libxml2mod.xmlUCSIsGothic(code)
    return ret

def uCSIsGreek(code):
    """Check whether the character is part of Greek UCS Block """
    ret = libxml2mod.xmlUCSIsGreek(code)
    return ret

def uCSIsGreekExtended(code):
    """Check whether the character is part of GreekExtended UCS
       Block """
    ret = libxml2mod.xmlUCSIsGreekExtended(code)
    return ret

def uCSIsGujarati(code):
    """Check whether the character is part of Gujarati UCS Block """
    ret = libxml2mod.xmlUCSIsGujarati(code)
    return ret

def uCSIsGurmukhi(code):
    """Check whether the character is part of Gurmukhi UCS Block """
    ret = libxml2mod.xmlUCSIsGurmukhi(code)
    return ret

def uCSIsHalfwidthandFullwidthForms(code):
    """Check whether the character is part of
       HalfwidthandFullwidthForms UCS Block """
    ret = libxml2mod.xmlUCSIsHalfwidthandFullwidthForms(code)
    return ret

def uCSIsHangulCompatibilityJamo(code):
    """Check whether the character is part of
       HangulCompatibilityJamo UCS Block """
    ret = libxml2mod.xmlUCSIsHangulCompatibilityJamo(code)
    return ret

def uCSIsHangulJamo(code):
    """Check whether the character is part of HangulJamo UCS Block """
    ret = libxml2mod.xmlUCSIsHangulJamo(code)
    return ret

def uCSIsHangulSyllables(code):
    """Check whether the character is part of HangulSyllables UCS
       Block """
    ret = libxml2mod.xmlUCSIsHangulSyllables(code)
    return ret

def uCSIsHebrew(code):
    """Check whether the character is part of Hebrew UCS Block """
    ret = libxml2mod.xmlUCSIsHebrew(code)
    return ret

def uCSIsHighPrivateUseSurrogates(code):
    """Check whether the character is part of
       HighPrivateUseSurrogates UCS Block """
    ret = libxml2mod.xmlUCSIsHighPrivateUseSurrogates(code)
    return ret

def uCSIsHighSurrogates(code):
    """Check whether the character is part of HighSurrogates UCS
       Block """
    ret = libxml2mod.xmlUCSIsHighSurrogates(code)
    return ret

def uCSIsHiragana(code):
    """Check whether the character is part of Hiragana UCS Block """
    ret = libxml2mod.xmlUCSIsHiragana(code)
    return ret

def uCSIsIPAExtensions(code):
    """Check whether the character is part of IPAExtensions UCS
       Block """
    ret = libxml2mod.xmlUCSIsIPAExtensions(code)
    return ret

def uCSIsIdeographicDescriptionCharacters(code):
    """Check whether the character is part of
       IdeographicDescriptionCharacters UCS Block """
    ret = libxml2mod.xmlUCSIsIdeographicDescriptionCharacters(code)
    return ret

def uCSIsKanbun(code):
    """Check whether the character is part of Kanbun UCS Block """
    ret = libxml2mod.xmlUCSIsKanbun(code)
    return ret

def uCSIsKangxiRadicals(code):
    """Check whether the character is part of KangxiRadicals UCS
       Block """
    ret = libxml2mod.xmlUCSIsKangxiRadicals(code)
    return ret

def uCSIsKannada(code):
    """Check whether the character is part of Kannada UCS Block """
    ret = libxml2mod.xmlUCSIsKannada(code)
    return ret

def uCSIsKatakana(code):
    """Check whether the character is part of Katakana UCS Block """
    ret = libxml2mod.xmlUCSIsKatakana(code)
    return ret

def uCSIsKhmer(code):
    """Check whether the character is part of Khmer UCS Block """
    ret = libxml2mod.xmlUCSIsKhmer(code)
    return ret

def uCSIsLao(code):
    """Check whether the character is part of Lao UCS Block """
    ret = libxml2mod.xmlUCSIsLao(code)
    return ret

def uCSIsLatin1Supplement(code):
    """Check whether the character is part of Latin-1Supplement
       UCS Block """
    ret = libxml2mod.xmlUCSIsLatin1Supplement(code)
    return ret

def uCSIsLatinExtendedA(code):
    """Check whether the character is part of LatinExtended-A UCS
       Block """
    ret = libxml2mod.xmlUCSIsLatinExtendedA(code)
    return ret

def uCSIsLatinExtendedAdditional(code):
    """Check whether the character is part of
       LatinExtendedAdditional UCS Block """
    ret = libxml2mod.xmlUCSIsLatinExtendedAdditional(code)
    return ret

def uCSIsLatinExtendedB(code):
    """Check whether the character is part of LatinExtended-B UCS
       Block """
    ret = libxml2mod.xmlUCSIsLatinExtendedB(code)
    return ret

def uCSIsLetterlikeSymbols(code):
    """Check whether the character is part of LetterlikeSymbols
       UCS Block """
    ret = libxml2mod.xmlUCSIsLetterlikeSymbols(code)
    return ret

def uCSIsLowSurrogates(code):
    """Check whether the character is part of LowSurrogates UCS
       Block """
    ret = libxml2mod.xmlUCSIsLowSurrogates(code)
    return ret

def uCSIsMalayalam(code):
    """Check whether the character is part of Malayalam UCS Block """
    ret = libxml2mod.xmlUCSIsMalayalam(code)
    return ret

def uCSIsMathematicalAlphanumericSymbols(code):
    """Check whether the character is part of
       MathematicalAlphanumericSymbols UCS Block """
    ret = libxml2mod.xmlUCSIsMathematicalAlphanumericSymbols(code)
    return ret

def uCSIsMathematicalOperators(code):
    """Check whether the character is part of
       MathematicalOperators UCS Block """
    ret = libxml2mod.xmlUCSIsMathematicalOperators(code)
    return ret

def uCSIsMiscellaneousSymbols(code):
    """Check whether the character is part of MiscellaneousSymbols
       UCS Block """
    ret = libxml2mod.xmlUCSIsMiscellaneousSymbols(code)
    return ret

def uCSIsMiscellaneousTechnical(code):
    """Check whether the character is part of
       MiscellaneousTechnical UCS Block """
    ret = libxml2mod.xmlUCSIsMiscellaneousTechnical(code)
    return ret

def uCSIsMongolian(code):
    """Check whether the character is part of Mongolian UCS Block """
    ret = libxml2mod.xmlUCSIsMongolian(code)
    return ret

def uCSIsMusicalSymbols(code):
    """Check whether the character is part of MusicalSymbols UCS
       Block """
    ret = libxml2mod.xmlUCSIsMusicalSymbols(code)
    return ret

def uCSIsMyanmar(code):
    """Check whether the character is part of Myanmar UCS Block """
    ret = libxml2mod.xmlUCSIsMyanmar(code)
    return ret

def uCSIsNumberForms(code):
    """Check whether the character is part of NumberForms UCS Block """
    ret = libxml2mod.xmlUCSIsNumberForms(code)
    return ret

def uCSIsOgham(code):
    """Check whether the character is part of Ogham UCS Block """
    ret = libxml2mod.xmlUCSIsOgham(code)
    return ret

def uCSIsOldItalic(code):
    """Check whether the character is part of OldItalic UCS Block """
    ret = libxml2mod.xmlUCSIsOldItalic(code)
    return ret

def uCSIsOpticalCharacterRecognition(code):
    """Check whether the character is part of
       OpticalCharacterRecognition UCS Block """
    ret = libxml2mod.xmlUCSIsOpticalCharacterRecognition(code)
    return ret

def uCSIsOriya(code):
    """Check whether the character is part of Oriya UCS Block """
    ret = libxml2mod.xmlUCSIsOriya(code)
    return ret

def uCSIsPrivateUse(code):
    """Check whether the character is part of PrivateUse UCS Block """
    ret = libxml2mod.xmlUCSIsPrivateUse(code)
    return ret

def uCSIsRunic(code):
    """Check whether the character is part of Runic UCS Block """
    ret = libxml2mod.xmlUCSIsRunic(code)
    return ret

def uCSIsSinhala(code):
    """Check whether the character is part of Sinhala UCS Block """
    ret = libxml2mod.xmlUCSIsSinhala(code)
    return ret

def uCSIsSmallFormVariants(code):
    """Check whether the character is part of SmallFormVariants
       UCS Block """
    ret = libxml2mod.xmlUCSIsSmallFormVariants(code)
    return ret

def uCSIsSpacingModifierLetters(code):
    """Check whether the character is part of
       SpacingModifierLetters UCS Block """
    ret = libxml2mod.xmlUCSIsSpacingModifierLetters(code)
    return ret

def uCSIsSpecials(code):
    """Check whether the character is part of Specials UCS Block """
    ret = libxml2mod.xmlUCSIsSpecials(code)
    return ret

def uCSIsSuperscriptsandSubscripts(code):
    """Check whether the character is part of
       SuperscriptsandSubscripts UCS Block """
    ret = libxml2mod.xmlUCSIsSuperscriptsandSubscripts(code)
    return ret

def uCSIsSyriac(code):
    """Check whether the character is part of Syriac UCS Block """
    ret = libxml2mod.xmlUCSIsSyriac(code)
    return ret

def uCSIsTags(code):
    """Check whether the character is part of Tags UCS Block """
    ret = libxml2mod.xmlUCSIsTags(code)
    return ret

def uCSIsTamil(code):
    """Check whether the character is part of Tamil UCS Block """
    ret = libxml2mod.xmlUCSIsTamil(code)
    return ret

def uCSIsTelugu(code):
    """Check whether the character is part of Telugu UCS Block """
    ret = libxml2mod.xmlUCSIsTelugu(code)
    return ret

def uCSIsThaana(code):
    """Check whether the character is part of Thaana UCS Block """
    ret = libxml2mod.xmlUCSIsThaana(code)
    return ret

def uCSIsThai(code):
    """Check whether the character is part of Thai UCS Block """
    ret = libxml2mod.xmlUCSIsThai(code)
    return ret

def uCSIsTibetan(code):
    """Check whether the character is part of Tibetan UCS Block """
    ret = libxml2mod.xmlUCSIsTibetan(code)
    return ret

def uCSIsUnifiedCanadianAboriginalSyllabics(code):
    """Check whether the character is part of
       UnifiedCanadianAboriginalSyllabics UCS Block """
    ret = libxml2mod.xmlUCSIsUnifiedCanadianAboriginalSyllabics(code)
    return ret

def uCSIsYiRadicals(code):
    """Check whether the character is part of YiRadicals UCS Block """
    ret = libxml2mod.xmlUCSIsYiRadicals(code)
    return ret

def uCSIsYiSyllables(code):
    """Check whether the character is part of YiSyllables UCS Block """
    ret = libxml2mod.xmlUCSIsYiSyllables(code)
    return ret

#
# Functions from module xmlversion
#

def checkVersion(version):
    """check the compiled lib version against the include one.
       This can warn or immediately kill the application """
    libxml2mod.xmlCheckVersion(version)

#
# Functions from module xpathInternals
#

def valuePop(ctxt):
    """Pops the top XPath object from the value stack """
    if ctxt is None: ctxt__o = None
    else: ctxt__o = ctxt._o
    ret = libxml2mod.valuePop(ctxt__o)
    return ret

class xmlNode(xmlCore):
    def __init__(self, _obj=None):
        self._o = None
        xmlCore.__init__(self, _obj=_obj)

    def __repr__(self):
        return "<xmlNode (%s) object at 0x%x>" % (self.name, id (self))

    # accessors for xmlNode
    def ns(self):
        """Get the namespace of a node """
        ret = libxml2mod.xmlNodeGetNs(self._o)
        if ret is None:raise treeError('xmlNodeGetNs() failed')
        __tmp = xmlNs(_obj=ret)
        return __tmp

    def nsDefs(self):
        """Get the namespace of a node """
        ret = libxml2mod.xmlNodeGetNsDefs(self._o)
        if ret is None:raise treeError('xmlNodeGetNsDefs() failed')
        __tmp = xmlNs(_obj=ret)
        return __tmp

    #
    # xmlNode functions from module debugXML
    #

    def debugDumpNode(self, output, depth):
        """Dumps debug information for the element node, it is
           recursive """
        libxml2mod.xmlDebugDumpNode(output, self._o, depth)

    def debugDumpNodeList(self, output, depth):
        """Dumps debug information for the list of element node, it is
           recursive """
        libxml2mod.xmlDebugDumpNodeList(output, self._o, depth)

    def debugDumpOneNode(self, output, depth):
        """Dumps debug information for the element node, it is not
           recursive """
        libxml2mod.xmlDebugDumpOneNode(output, self._o, depth)

    def lsCountNode(self):
        """Count the children of @node. """
        ret = libxml2mod.xmlLsCountNode(self._o)
        return ret

    def lsOneNode(self, output):
        """Dump to @output the type and name of @node. """
        libxml2mod.xmlLsOneNode(output, self._o)

    def shellPrintNode(self):
        """Print node to the output FILE """
        libxml2mod.xmlShellPrintNode(self._o)

    #
    # xmlNode functions from module tree
    #

    def addChild(self, cur):
        """Add a new node to @parent, at the end of the child (or
           property) list merging adjacent TEXT nodes (in which case
           @cur is freed) If the new node is ATTRIBUTE, it is added
           into properties instead of children. If there is an
           attribute with equal name, it is first destroyed. """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        ret = libxml2mod.xmlAddChild(self._o, cur__o)
        if ret is None:raise treeError('xmlAddChild() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def addChildList(self, cur):
        """Add a list of node at the end of the child list of the
           parent merging adjacent TEXT nodes (@cur may be freed) """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        ret = libxml2mod.xmlAddChildList(self._o, cur__o)
        if ret is None:raise treeError('xmlAddChildList() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def addContent(self, content):
        """Append the extra substring to the node content. """
        libxml2mod.xmlNodeAddContent(self._o, content)

    def addContentLen(self, content, len):
        """Append the extra substring to the node content. """
        libxml2mod.xmlNodeAddContentLen(self._o, content, len)

    def addNextSibling(self, elem):
        """Add a new node @elem as the next sibling of @cur If the new
           node was already inserted in a document it is first
           unlinked from its existing context. As a result of text
           merging @elem may be freed. If the new node is ATTRIBUTE,
           it is added into properties instead of children. If there
           is an attribute with equal name, it is first destroyed. """
        if elem is None: elem__o = None
        else: elem__o = elem._o
        ret = libxml2mod.xmlAddNextSibling(self._o, elem__o)
        if ret is None:raise treeError('xmlAddNextSibling() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def addPrevSibling(self, elem):
        """Add a new node @elem as the previous sibling of @cur
           merging adjacent TEXT nodes (@elem may be freed) If the
           new node was already inserted in a document it is first
           unlinked from its existing context. If the new node is
           ATTRIBUTE, it is added into properties instead of
           children. If there is an attribute with equal name, it is
           first destroyed. """
        if elem is None: elem__o = None
        else: elem__o = elem._o
        ret = libxml2mod.xmlAddPrevSibling(self._o, elem__o)
        if ret is None:raise treeError('xmlAddPrevSibling() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def addSibling(self, elem):
        """Add a new element @elem to the list of siblings of @cur
           merging adjacent TEXT nodes (@elem may be freed) If the
           new element was already inserted in a document it is first
           unlinked from its existing context. """
        if elem is None: elem__o = None
        else: elem__o = elem._o
        ret = libxml2mod.xmlAddSibling(self._o, elem__o)
        if ret is None:raise treeError('xmlAddSibling() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def copyNode(self, recursive):
        """Do a copy of the node. """
        ret = libxml2mod.xmlCopyNode(self._o, recursive)
        if ret is None:raise treeError('xmlCopyNode() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def copyNodeList(self):
        """Do a recursive copy of the node list. """
        ret = libxml2mod.xmlCopyNodeList(self._o)
        if ret is None:raise treeError('xmlCopyNodeList() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def copyProp(self, cur):
        """Do a copy of the attribute. """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        ret = libxml2mod.xmlCopyProp(self._o, cur__o)
        if ret is None:raise treeError('xmlCopyProp() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def copyPropList(self, cur):
        """Do a copy of an attribute list. """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        ret = libxml2mod.xmlCopyPropList(self._o, cur__o)
        if ret is None:raise treeError('xmlCopyPropList() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def docCopyNode(self, doc, recursive):
        """Do a copy of the node to a given document. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlDocCopyNode(self._o, doc__o, recursive)
        if ret is None:raise treeError('xmlDocCopyNode() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def docSetRootElement(self, doc):
        """Set the root element of the document (doc->children is a
           list containing possibly comments, PIs, etc ...). """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlDocSetRootElement(doc__o, self._o)
        if ret is None:return None
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def freeNode(self):
        """Free a node, this is a recursive behaviour, all the
           children are freed too. This doesn't unlink the child from
           the list, use xmlUnlinkNode() first. """
        libxml2mod.xmlFreeNode(self._o)

    def freeNodeList(self):
        """Free a node and all its siblings, this is a recursive
           behaviour, all the children are freed too. """
        libxml2mod.xmlFreeNodeList(self._o)

    def getBase(self, doc):
        """Searches for the BASE URL. The code should work on both XML
           and HTML document even if base mechanisms are completely
           different. It returns the base as defined in RFC 2396
           sections 5.1.1. Base URI within Document Content and
           5.1.2. Base URI from the Encapsulating Entity However it
           does not return the document base (5.1.3), use
           xmlDocumentGetBase() for this """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlNodeGetBase(doc__o, self._o)
        return ret

    def getContent(self):
        """Read the value of a node, this can be either the text
           carried directly by this node if it's a TEXT node or the
           aggregate string of the values carried by this node
           child's (TEXT and ENTITY_REF). Entity references are
           substituted. """
        ret = libxml2mod.xmlNodeGetContent(self._o)
        return ret

    def getLang(self):
        """Searches the language of a node, i.e. the values of the
           xml:lang attribute or the one carried by the nearest
           ancestor. """
        ret = libxml2mod.xmlNodeGetLang(self._o)
        return ret

    def getSpacePreserve(self):
        """Searches the space preserving behaviour of a node, i.e. the
           values of the xml:space attribute or the one carried by
           the nearest ancestor. """
        ret = libxml2mod.xmlNodeGetSpacePreserve(self._o)
        return ret

    def hasNsProp(self, name, nameSpace):
        """Search for an attribute associated to a node This attribute
           has to be anchored in the namespace specified. This does
           the entity substitution. This function looks in DTD
           attribute declaration for #FIXED or default declaration
           values unless DTD use has been turned off. """
        ret = libxml2mod.xmlHasNsProp(self._o, name, nameSpace)
        if ret is None:return None
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def hasProp(self, name):
        """Search an attribute associated to a node This function also
           looks in DTD attribute declaration for #FIXED or default
           declaration values unless DTD use has been turned off. """
        ret = libxml2mod.xmlHasProp(self._o, name)
        if ret is None:return None
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def isBlankNode(self):
        """Checks whether this node is an empty or whitespace only
           (and possibly ignorable) text-node. """
        ret = libxml2mod.xmlIsBlankNode(self._o)
        return ret

    def isText(self):
        """Is this node a Text node ? """
        ret = libxml2mod.xmlNodeIsText(self._o)
        return ret

    def lastChild(self):
        """Search the last child of a node. """
        ret = libxml2mod.xmlGetLastChild(self._o)
        if ret is None:raise treeError('xmlGetLastChild() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def lineNo(self):
        """Get line number of node. this requires activation of this
           option before invoking the parser by calling
           xmlLineNumbersDefault(1) """
        ret = libxml2mod.xmlGetLineNo(self._o)
        return ret

    def listGetRawString(self, doc, inLine):
        """Builds the string equivalent to the text contained in the
           Node list made of TEXTs and ENTITY_REFs, contrary to
           xmlNodeListGetString() this function doesn't do any
           character encoding handling. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlNodeListGetRawString(doc__o, self._o, inLine)
        return ret

    def listGetString(self, doc, inLine):
        """Build the string equivalent to the text contained in the
           Node list made of TEXTs and ENTITY_REFs """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlNodeListGetString(doc__o, self._o, inLine)
        return ret

    def newChild(self, ns, name, content):
        """Creation of a new child element, added at the end of
           @parent children list. @ns and @content parameters are
           optional (None). If content is non None, a child list
           containing the TEXTs and ENTITY_REFs node will be created.
           NOTE: @content is supposed to be a piece of XML CDATA, so
           it allow entities references, but XML special chars need
           to be escaped first by using xmlEncodeEntitiesReentrant().
           Use xmlNewTextChild() if entities support is not needed. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlNewChild(self._o, ns__o, name, content)
        if ret is None:raise treeError('xmlNewChild() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newNs(self, href, prefix):
        """Creation of a new Namespace. This function will refuse to
           create a namespace with a similar prefix than an existing
           one present on this node. We use href==None in the case of
           an element creation where the namespace was not defined. """
        ret = libxml2mod.xmlNewNs(self._o, href, prefix)
        if ret is None:raise treeError('xmlNewNs() failed')
        __tmp = xmlNs(_obj=ret)
        return __tmp

    def newNsProp(self, ns, name, value):
        """Create a new property tagged with a namespace and carried
           by a node. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlNewNsProp(self._o, ns__o, name, value)
        if ret is None:raise treeError('xmlNewNsProp() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def newNsPropEatName(self, ns, name, value):
        """Create a new property tagged with a namespace and carried
           by a node. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlNewNsPropEatName(self._o, ns__o, name, value)
        if ret is None:raise treeError('xmlNewNsPropEatName() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def newProp(self, name, value):
        """Create a new property carried by a node. """
        ret = libxml2mod.xmlNewProp(self._o, name, value)
        if ret is None:raise treeError('xmlNewProp() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def newTextChild(self, ns, name, content):
        """Creation of a new child element, added at the end of
           @parent children list. @ns and @content parameters are
           optional (None). If content is non None, a child TEXT node
           will be created containing the string content. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlNewTextChild(self._o, ns__o, name, content)
        if ret is None:raise treeError('xmlNewTextChild() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def noNsProp(self, name):
        """Search and get the value of an attribute associated to a
           node This does the entity substitution. This function
           looks in DTD attribute declaration for #FIXED or default
           declaration values unless DTD use has been turned off.
           This function is similar to xmlGetProp except it will
           accept only an attribute in no namespace. """
        ret = libxml2mod.xmlGetNoNsProp(self._o, name)
        return ret

    def nodePath(self):
        """Build a structure based Path for the given node """
        ret = libxml2mod.xmlGetNodePath(self._o)
        return ret

    def nsProp(self, name, nameSpace):
        """Search and get the value of an attribute associated to a
           node This attribute has to be anchored in the namespace
           specified. This does the entity substitution. This
           function looks in DTD attribute declaration for #FIXED or
           default declaration values unless DTD use has been turned
           off. """
        ret = libxml2mod.xmlGetNsProp(self._o, name, nameSpace)
        return ret

    def prop(self, name):
        """Search and get the value of an attribute associated to a
           node This does the entity substitution. This function
           looks in DTD attribute declaration for #FIXED or default
           declaration values unless DTD use has been turned off.
           NOTE: this function acts independently of namespaces
           associated to the attribute. Use xmlGetNsProp() or
           xmlGetNoNsProp() for namespace aware processing. """
        ret = libxml2mod.xmlGetProp(self._o, name)
        return ret

    def reconciliateNs(self, doc):
        """This function checks that all the namespaces declared
           within the given tree are properly declared. This is
           needed for example after Copy or Cut and then paste
           operations. The subtree may still hold pointers to
           namespace declarations outside the subtree or
           invalid/masked. As much as possible the function try to
           reuse the existing namespaces found in the new
           environment. If not possible the new namespaces are
           redeclared on @tree at the top of the given subtree. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlReconciliateNs(doc__o, self._o)
        return ret

    def replaceNode(self, cur):
        """Unlink the old node from it's current context, prune the
           new one at the same place. If @cur was already inserted in
           a document it is first unlinked from its existing context. """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        ret = libxml2mod.xmlReplaceNode(self._o, cur__o)
        if ret is None:raise treeError('xmlReplaceNode() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def searchNs(self, doc, nameSpace):
        """Search a Ns registered under a given name space for a
           document. recurse on the parents until it finds the
           defined namespace or return None otherwise. @nameSpace can
           be None, this is a search for the default namespace. We
           don't allow to cross entities boundaries. If you don't
           declare the namespace within those you will be in troubles
           !!! A warning is generated to cover this case. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlSearchNs(doc__o, self._o, nameSpace)
        if ret is None:raise treeError('xmlSearchNs() failed')
        __tmp = xmlNs(_obj=ret)
        return __tmp

    def searchNsByHref(self, doc, href):
        """Search a Ns aliasing a given URI. Recurse on the parents
           until it finds the defined namespace or return None
           otherwise. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlSearchNsByHref(doc__o, self._o, href)
        if ret is None:raise treeError('xmlSearchNsByHref() failed')
        __tmp = xmlNs(_obj=ret)
        return __tmp

    def setBase(self, uri):
        """Set (or reset) the base URI of a node, i.e. the value of
           the xml:base attribute. """
        libxml2mod.xmlNodeSetBase(self._o, uri)

    def setContent(self, content):
        """Replace the content of a node. """
        libxml2mod.xmlNodeSetContent(self._o, content)

    def setContentLen(self, content, len):
        """Replace the content of a node. """
        libxml2mod.xmlNodeSetContentLen(self._o, content, len)

    def setLang(self, lang):
        """Set the language of a node, i.e. the values of the xml:lang
           attribute. """
        libxml2mod.xmlNodeSetLang(self._o, lang)

    def setListDoc(self, doc):
        """update all nodes in the list to point to the right document """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        libxml2mod.xmlSetListDoc(self._o, doc__o)

    def setName(self, name):
        """Set (or reset) the name of a node. """
        libxml2mod.xmlNodeSetName(self._o, name)

    def setNs(self, ns):
        """Associate a namespace to a node, a posteriori. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        libxml2mod.xmlSetNs(self._o, ns__o)

    def setNsProp(self, ns, name, value):
        """Set (or reset) an attribute carried by a node. The ns
           structure must be in scope, this is not checked. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlSetNsProp(self._o, ns__o, name, value)
        if ret is None:raise treeError('xmlSetNsProp() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def setProp(self, name, value):
        """Set (or reset) an attribute carried by a node. """
        ret = libxml2mod.xmlSetProp(self._o, name, value)
        if ret is None:raise treeError('xmlSetProp() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def setSpacePreserve(self, val):
        """Set (or reset) the space preserving behaviour of a node,
           i.e. the value of the xml:space attribute. """
        libxml2mod.xmlNodeSetSpacePreserve(self._o, val)

    def setTreeDoc(self, doc):
        """update all nodes under the tree to point to the right
           document """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        libxml2mod.xmlSetTreeDoc(self._o, doc__o)

    def textConcat(self, content, len):
        """Concat the given string at the end of the existing node
           content """
        libxml2mod.xmlTextConcat(self._o, content, len)

    def textMerge(self, second):
        """Merge two text nodes into one """
        if second is None: second__o = None
        else: second__o = second._o
        ret = libxml2mod.xmlTextMerge(self._o, second__o)
        if ret is None:raise treeError('xmlTextMerge() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def unlinkNode(self):
        """Unlink a node from it's current context, the node is not
           freed """
        libxml2mod.xmlUnlinkNode(self._o)

    def unsetNsProp(self, ns, name):
        """Remove an attribute carried by a node. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlUnsetNsProp(self._o, ns__o, name)
        return ret

    def unsetProp(self, name):
        """Remove an attribute carried by a node. """
        ret = libxml2mod.xmlUnsetProp(self._o, name)
        return ret

    #
    # xmlNode functions from module valid
    #

    def isID(self, doc, attr):
        """Determine whether an attribute is of type ID. In case we
           have DTD(s) then this is done if DTD loading has been
           requested. In the case of HTML documents parsed with the
           HTML parser, then ID detection is done systematically. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        if attr is None: attr__o = None
        else: attr__o = attr._o
        ret = libxml2mod.xmlIsID(doc__o, self._o, attr__o)
        return ret

    def isRef(self, doc, attr):
        """Determine whether an attribute is of type Ref. In case we
           have DTD(s) then this is simple, otherwise we use an
           heuristic: name Ref (upper or lowercase). """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        if attr is None: attr__o = None
        else: attr__o = attr._o
        ret = libxml2mod.xmlIsRef(doc__o, self._o, attr__o)
        return ret

    def validNormalizeAttributeValue(self, doc, name, value):
        """Does the validation related extra step of the normalization
           of attribute values:  If the declared value is not CDATA,
           then the XML processor must further process the normalized
           attribute value by discarding any leading and trailing
           space (#x20) characters, and by replacing sequences of
           space (#x20) characters by single space (#x20) character. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlValidNormalizeAttributeValue(doc__o, self._o, name, value)
        return ret

    #
    # xmlNode functions from module xpath
    #

    def xpathCastNodeToNumber(self):
        """Converts a node to its number value """
        ret = libxml2mod.xmlXPathCastNodeToNumber(self._o)
        return ret

    def xpathCastNodeToString(self):
        """Converts a node to its string value. """
        ret = libxml2mod.xmlXPathCastNodeToString(self._o)
        return ret

    def xpathCmpNodes(self, node2):
        """Compare two nodes w.r.t document order """
        if node2 is None: node2__o = None
        else: node2__o = node2._o
        ret = libxml2mod.xmlXPathCmpNodes(self._o, node2__o)
        return ret

    #
    # xmlNode functions from module xpathInternals
    #

    def xpathNewNodeSet(self):
        """Create a new xmlXPathObjectPtr of type NodeSet and
           initialize it with the single Node @val """
        ret = libxml2mod.xmlXPathNewNodeSet(self._o)
        if ret is None:raise xpathError('xmlXPathNewNodeSet() failed')
        return xpathObjectRet(ret)

    def xpathNewValueTree(self):
        """Create a new xmlXPathObjectPtr of type Value Tree (XSLT)
           and initialize it with the tree root @val """
        ret = libxml2mod.xmlXPathNewValueTree(self._o)
        if ret is None:raise xpathError('xmlXPathNewValueTree() failed')
        return xpathObjectRet(ret)

    def xpathNextAncestor(self, ctxt):
        """Traversal function for the "ancestor" direction the
           ancestor axis contains the ancestors of the context node;
           the ancestors of the context node consist of the parent of
           context node and the parent's parent and so on; the nodes
           are ordered in reverse document order; thus the parent is
           the first node on the axis, and the parent's parent is the
           second node on the axis """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextAncestor(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextAncestor() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextAncestorOrSelf(self, ctxt):
        """Traversal function for the "ancestor-or-self" direction he
           ancestor-or-self axis contains the context node and
           ancestors of the context node in reverse document order;
           thus the context node is the first node on the axis, and
           the context node's parent the second; parent here is
           defined the same as with the parent axis. """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextAncestorOrSelf(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextAncestorOrSelf() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextAttribute(self, ctxt):
        """Traversal function for the "attribute" direction TODO:
           support DTD inherited default attributes """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextAttribute(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextAttribute() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextChild(self, ctxt):
        """Traversal function for the "child" direction The child axis
           contains the children of the context node in document
           order. """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextChild(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextChild() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextDescendant(self, ctxt):
        """Traversal function for the "descendant" direction the
           descendant axis contains the descendants of the context
           node in document order; a descendant is a child or a child
           of a child and so on. """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextDescendant(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextDescendant() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextDescendantOrSelf(self, ctxt):
        """Traversal function for the "descendant-or-self" direction
           the descendant-or-self axis contains the context node and
           the descendants of the context node in document order;
           thus the context node is the first node on the axis, and
           the first child of the context node is the second node on
           the axis """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextDescendantOrSelf(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextDescendantOrSelf() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextFollowing(self, ctxt):
        """Traversal function for the "following" direction The
           following axis contains all nodes in the same document as
           the context node that are after the context node in
           document order, excluding any descendants and excluding
           attribute nodes and namespace nodes; the nodes are ordered
           in document order """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextFollowing(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextFollowing() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextFollowingSibling(self, ctxt):
        """Traversal function for the "following-sibling" direction
           The following-sibling axis contains the following siblings
           of the context node in document order. """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextFollowingSibling(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextFollowingSibling() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextNamespace(self, ctxt):
        """Traversal function for the "namespace" direction the
           namespace axis contains the namespace nodes of the context
           node; the order of nodes on this axis is
           implementation-defined; the axis will be empty unless the
           context node is an element  We keep the XML namespace node
           at the end of the list. """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextNamespace(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextNamespace() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextParent(self, ctxt):
        """Traversal function for the "parent" direction The parent
           axis contains the parent of the context node, if there is
           one. """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextParent(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextParent() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextPreceding(self, ctxt):
        """Traversal function for the "preceding" direction the
           preceding axis contains all nodes in the same document as
           the context node that are before the context node in
           document order, excluding any ancestors and excluding
           attribute nodes and namespace nodes; the nodes are ordered
           in reverse document order """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextPreceding(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextPreceding() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextPrecedingSibling(self, ctxt):
        """Traversal function for the "preceding-sibling" direction
           The preceding-sibling axis contains the preceding siblings
           of the context node in reverse document order; the first
           preceding sibling is first on the axis; the sibling
           preceding that node is the second on the axis and so on. """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextPrecedingSibling(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextPrecedingSibling() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def xpathNextSelf(self, ctxt):
        """Traversal function for the "self" direction The self axis
           contains just the context node itself """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlXPathNextSelf(ctxt__o, self._o)
        if ret is None:raise xpathError('xmlXPathNextSelf() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    #
    # xmlNode functions from module xpointer
    #

    def xpointerNewCollapsedRange(self):
        """Create a new xmlXPathObjectPtr of type range using a single
           nodes """
        ret = libxml2mod.xmlXPtrNewCollapsedRange(self._o)
        if ret is None:raise treeError('xmlXPtrNewCollapsedRange() failed')
        return xpathObjectRet(ret)

    def xpointerNewContext(self, doc, origin):
        """Create a new XPointer context """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        if origin is None: origin__o = None
        else: origin__o = origin._o
        ret = libxml2mod.xmlXPtrNewContext(doc__o, self._o, origin__o)
        if ret is None:raise treeError('xmlXPtrNewContext() failed')
        __tmp = xpathContext(_obj=ret)
        return __tmp

    def xpointerNewLocationSetNodes(self, end):
        """Create a new xmlXPathObjectPtr of type LocationSet and
           initialize it with the single range made of the two nodes
           @start and @end """
        if end is None: end__o = None
        else: end__o = end._o
        ret = libxml2mod.xmlXPtrNewLocationSetNodes(self._o, end__o)
        if ret is None:raise treeError('xmlXPtrNewLocationSetNodes() failed')
        return xpathObjectRet(ret)

    def xpointerNewRange(self, startindex, end, endindex):
        """Create a new xmlXPathObjectPtr of type range """
        if end is None: end__o = None
        else: end__o = end._o
        ret = libxml2mod.xmlXPtrNewRange(self._o, startindex, end__o, endindex)
        if ret is None:raise treeError('xmlXPtrNewRange() failed')
        return xpathObjectRet(ret)

    def xpointerNewRangeNodes(self, end):
        """Create a new xmlXPathObjectPtr of type range using 2 nodes """
        if end is None: end__o = None
        else: end__o = end._o
        ret = libxml2mod.xmlXPtrNewRangeNodes(self._o, end__o)
        if ret is None:raise treeError('xmlXPtrNewRangeNodes() failed')
        return xpathObjectRet(ret)

class xmlDoc(xmlNode):
    def __init__(self, _obj=None):
        self._o = None
        xmlNode.__init__(self, _obj=_obj)

    def __repr__(self):
        return "<xmlDoc (%s) object at 0x%x>" % (self.name, id (self))

    #
    # xmlDoc functions from module HTMLparser
    #

    def htmlAutoCloseTag(self, name, elem):
        """The HTML DTD allows a tag to implicitly close other tags.
           The list is kept in htmlStartClose array. This function
           checks if the element or one of it's children would
           autoclose the given tag. """
        ret = libxml2mod.htmlAutoCloseTag(self._o, name, elem)
        return ret

    def htmlIsAutoClosed(self, elem):
        """The HTML DTD allows a tag to implicitly close other tags.
           The list is kept in htmlStartClose array. This function
           checks if a tag is autoclosed by one of it's child """
        ret = libxml2mod.htmlIsAutoClosed(self._o, elem)
        return ret

    #
    # xmlDoc functions from module HTMLtree
    #

    def htmlDocContentDumpFormatOutput(self, buf, encoding, format):
        """Dump an HTML document. """
        if buf is None: buf__o = None
        else: buf__o = buf._o
        libxml2mod.htmlDocContentDumpFormatOutput(buf__o, self._o, encoding, format)

    def htmlDocContentDumpOutput(self, buf, encoding):
        """Dump an HTML document. Formating return/spaces are added. """
        if buf is None: buf__o = None
        else: buf__o = buf._o
        libxml2mod.htmlDocContentDumpOutput(buf__o, self._o, encoding)

    def htmlDocDump(self, f):
        """Dump an HTML document to an open FILE. """
        ret = libxml2mod.htmlDocDump(f, self._o)
        return ret

    def htmlGetMetaEncoding(self):
        """Encoding definition lookup in the Meta tags """
        ret = libxml2mod.htmlGetMetaEncoding(self._o)
        return ret

    def htmlNodeDumpFile(self, out, cur):
        """Dump an HTML node, recursive behaviour,children are printed
           too, and formatting returns are added. """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        libxml2mod.htmlNodeDumpFile(out, self._o, cur__o)

    def htmlNodeDumpFileFormat(self, out, cur, encoding, format):
        """Dump an HTML node, recursive behaviour,children are printed
           too.  TODO: if encoding == None try to save in the doc
           encoding """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        ret = libxml2mod.htmlNodeDumpFileFormat(out, self._o, cur__o, encoding, format)
        return ret

    def htmlNodeDumpFormatOutput(self, buf, cur, encoding, format):
        """Dump an HTML node, recursive behaviour,children are printed
           too. """
        if buf is None: buf__o = None
        else: buf__o = buf._o
        if cur is None: cur__o = None
        else: cur__o = cur._o
        libxml2mod.htmlNodeDumpFormatOutput(buf__o, self._o, cur__o, encoding, format)

    def htmlNodeDumpOutput(self, buf, cur, encoding):
        """Dump an HTML node, recursive behaviour,children are printed
           too, and formatting returns/spaces are added. """
        if buf is None: buf__o = None
        else: buf__o = buf._o
        if cur is None: cur__o = None
        else: cur__o = cur._o
        libxml2mod.htmlNodeDumpOutput(buf__o, self._o, cur__o, encoding)

    def htmlSaveFile(self, filename):
        """Dump an HTML document to a file. If @filename is "-" the
           stdout file is used. """
        ret = libxml2mod.htmlSaveFile(filename, self._o)
        return ret

    def htmlSaveFileEnc(self, filename, encoding):
        """Dump an HTML document to a file using a given encoding and
           formatting returns/spaces are added. """
        ret = libxml2mod.htmlSaveFileEnc(filename, self._o, encoding)
        return ret

    def htmlSaveFileFormat(self, filename, encoding, format):
        """Dump an HTML document to a file using a given encoding. """
        ret = libxml2mod.htmlSaveFileFormat(filename, self._o, encoding, format)
        return ret

    def htmlSetMetaEncoding(self, encoding):
        """Sets the current encoding in the Meta tags NOTE: this will
           not change the document content encoding, just the META
           flag associated. """
        ret = libxml2mod.htmlSetMetaEncoding(self._o, encoding)
        return ret

    #
    # xmlDoc functions from module debugXML
    #

    def debugDumpDocument(self, output):
        """Dumps debug information for the document, it's recursive """
        libxml2mod.xmlDebugDumpDocument(output, self._o)

    def debugDumpDocumentHead(self, output):
        """Dumps debug information cncerning the document, not
           recursive """
        libxml2mod.xmlDebugDumpDocumentHead(output, self._o)

    def debugDumpEntities(self, output):
        """Dumps debug information for all the entities in use by the
           document """
        libxml2mod.xmlDebugDumpEntities(output, self._o)

    #
    # xmlDoc functions from module entities
    #

    def addDocEntity(self, name, type, ExternalID, SystemID, content):
        """Register a new entity for this document. """
        ret = libxml2mod.xmlAddDocEntity(self._o, name, type, ExternalID, SystemID, content)
        if ret is None:raise treeError('xmlAddDocEntity() failed')
        __tmp = xmlEntity(_obj=ret)
        return __tmp

    def addDtdEntity(self, name, type, ExternalID, SystemID, content):
        """Register a new entity for this document DTD external subset. """
        ret = libxml2mod.xmlAddDtdEntity(self._o, name, type, ExternalID, SystemID, content)
        if ret is None:raise treeError('xmlAddDtdEntity() failed')
        __tmp = xmlEntity(_obj=ret)
        return __tmp

    def docEntity(self, name):
        """Do an entity lookup in the document entity hash table and """
        ret = libxml2mod.xmlGetDocEntity(self._o, name)
        if ret is None:raise treeError('xmlGetDocEntity() failed')
        __tmp = xmlEntity(_obj=ret)
        return __tmp

    def dtdEntity(self, name):
        """Do an entity lookup in the DTD entity hash table and """
        ret = libxml2mod.xmlGetDtdEntity(self._o, name)
        if ret is None:raise treeError('xmlGetDtdEntity() failed')
        __tmp = xmlEntity(_obj=ret)
        return __tmp

    def encodeEntities(self, input):
        """Do a global encoding of a string, replacing the predefined
           entities and non ASCII values with their entities and
           CharRef counterparts.  TODO: remove xmlEncodeEntities,
           once we are not afraid of breaking binary compatibility 
           People must migrate their code to
           xmlEncodeEntitiesReentrant ! This routine will issue a
           warning when encountered. """
        ret = libxml2mod.xmlEncodeEntities(self._o, input)
        return ret

    def encodeEntitiesReentrant(self, input):
        """Do a global encoding of a string, replacing the predefined
           entities and non ASCII values with their entities and
           CharRef counterparts. Contrary to xmlEncodeEntities, this
           routine is reentrant, and result must be deallocated. """
        ret = libxml2mod.xmlEncodeEntitiesReentrant(self._o, input)
        return ret

    def encodeSpecialChars(self, input):
        """Do a global encoding of a string, replacing the predefined
           entities this routine is reentrant, and result must be
           deallocated. """
        ret = libxml2mod.xmlEncodeSpecialChars(self._o, input)
        return ret

    def parameterEntity(self, name):
        """Do an entity lookup in the internal and external subsets and """
        ret = libxml2mod.xmlGetParameterEntity(self._o, name)
        if ret is None:raise treeError('xmlGetParameterEntity() failed')
        __tmp = xmlEntity(_obj=ret)
        return __tmp

    #
    # xmlDoc functions from module relaxng
    #

    def relaxNGValidateDoc(self, ctxt):
        """Validate a document tree in memory. """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        ret = libxml2mod.xmlRelaxNGValidateDoc(ctxt__o, self._o)
        return ret

    #
    # xmlDoc functions from module tree
    #

    def copyDoc(self, recursive):
        """Do a copy of the document info. If recursive, the content
           tree will be copied too as well as DTD, namespaces and
           entities. """
        ret = libxml2mod.xmlCopyDoc(self._o, recursive)
        if ret is None:raise treeError('xmlCopyDoc() failed')
        __tmp = xmlDoc(_obj=ret)
        return __tmp

    def createIntSubset(self, name, ExternalID, SystemID):
        """Create the internal subset of a document """
        ret = libxml2mod.xmlCreateIntSubset(self._o, name, ExternalID, SystemID)
        if ret is None:raise treeError('xmlCreateIntSubset() failed')
        __tmp = xmlDtd(_obj=ret)
        return __tmp

    def docCompressMode(self):
        """get the compression ratio for a document, ZLIB based """
        ret = libxml2mod.xmlGetDocCompressMode(self._o)
        return ret

    def dump(self, f):
        """Dump an XML document to an open FILE. """
        ret = libxml2mod.xmlDocDump(f, self._o)
        return ret

    def elemDump(self, f, cur):
        """Dump an XML/HTML node, recursive behaviour, children are
           printed too. """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        libxml2mod.xmlElemDump(f, self._o, cur__o)

    def formatDump(self, f, format):
        """Dump an XML document to an open FILE. """
        ret = libxml2mod.xmlDocFormatDump(f, self._o, format)
        return ret

    def freeDoc(self):
        """Free up all the structures used by a document, tree
           included. """
        libxml2mod.xmlFreeDoc(self._o)

    def getRootElement(self):
        """Get the root element of the document (doc->children is a
           list containing possibly comments, PIs, etc ...). """
        ret = libxml2mod.xmlDocGetRootElement(self._o)
        if ret is None:raise treeError('xmlDocGetRootElement() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def intSubset(self):
        """Get the internal subset of a document """
        ret = libxml2mod.xmlGetIntSubset(self._o)
        if ret is None:raise treeError('xmlGetIntSubset() failed')
        __tmp = xmlDtd(_obj=ret)
        return __tmp

    def newCDataBlock(self, content, len):
        """Creation of a new node containing a CDATA block. """
        ret = libxml2mod.xmlNewCDataBlock(self._o, content, len)
        if ret is None:raise treeError('xmlNewCDataBlock() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newCharRef(self, name):
        """Creation of a new character reference node. """
        ret = libxml2mod.xmlNewCharRef(self._o, name)
        if ret is None:raise treeError('xmlNewCharRef() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newDocComment(self, content):
        """Creation of a new node containing a comment within a
           document. """
        ret = libxml2mod.xmlNewDocComment(self._o, content)
        if ret is None:raise treeError('xmlNewDocComment() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newDocFragment(self):
        """Creation of a new Fragment node. """
        ret = libxml2mod.xmlNewDocFragment(self._o)
        if ret is None:raise treeError('xmlNewDocFragment() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newDocNode(self, ns, name, content):
        """Creation of a new node element within a document. @ns and
           @content are optional (None). NOTE: @content is supposed
           to be a piece of XML CDATA, so it allow entities
           references, but XML special chars need to be escaped first
           by using xmlEncodeEntitiesReentrant(). Use
           xmlNewDocRawNode() if you don't need entities support. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlNewDocNode(self._o, ns__o, name, content)
        if ret is None:raise treeError('xmlNewDocNode() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newDocNodeEatName(self, ns, name, content):
        """Creation of a new node element within a document. @ns and
           @content are optional (None). NOTE: @content is supposed
           to be a piece of XML CDATA, so it allow entities
           references, but XML special chars need to be escaped first
           by using xmlEncodeEntitiesReentrant(). Use
           xmlNewDocRawNode() if you don't need entities support. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlNewDocNodeEatName(self._o, ns__o, name, content)
        if ret is None:raise treeError('xmlNewDocNodeEatName() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newDocProp(self, name, value):
        """Create a new property carried by a document. """
        ret = libxml2mod.xmlNewDocProp(self._o, name, value)
        if ret is None:raise treeError('xmlNewDocProp() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def newDocRawNode(self, ns, name, content):
        """Creation of a new node element within a document. @ns and
           @content are optional (None). """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlNewDocRawNode(self._o, ns__o, name, content)
        if ret is None:raise treeError('xmlNewDocRawNode() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newDocText(self, content):
        """Creation of a new text node within a document. """
        ret = libxml2mod.xmlNewDocText(self._o, content)
        if ret is None:raise treeError('xmlNewDocText() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newDocTextLen(self, content, len):
        """Creation of a new text node with an extra content length
           parameter. The text node pertain to a given document. """
        ret = libxml2mod.xmlNewDocTextLen(self._o, content, len)
        if ret is None:raise treeError('xmlNewDocTextLen() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def newDtd(self, name, ExternalID, SystemID):
        """Creation of a new DTD for the external subset. To create an
           internal subset, use xmlCreateIntSubset(). """
        ret = libxml2mod.xmlNewDtd(self._o, name, ExternalID, SystemID)
        if ret is None:raise treeError('xmlNewDtd() failed')
        __tmp = xmlDtd(_obj=ret)
        return __tmp

    def newGlobalNs(self, href, prefix):
        """Creation of a Namespace, the old way using PI and without
           scoping DEPRECATED !!! It now create a namespace on the
           root element of the document if found. """
        ret = libxml2mod.xmlNewGlobalNs(self._o, href, prefix)
        if ret is None:raise treeError('xmlNewGlobalNs() failed')
        __tmp = xmlNs(_obj=ret)
        return __tmp

    def newReference(self, name):
        """Creation of a new reference node. """
        ret = libxml2mod.xmlNewReference(self._o, name)
        if ret is None:raise treeError('xmlNewReference() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def nodeDumpOutput(self, buf, cur, level, format, encoding):
        """Dump an XML node, recursive behaviour, children are printed
           too. Note that @format = 1 provide node indenting only if
           xmlIndentTreeOutput = 1 or xmlKeepBlanksDefault(0) was
           called """
        if buf is None: buf__o = None
        else: buf__o = buf._o
        if cur is None: cur__o = None
        else: cur__o = cur._o
        libxml2mod.xmlNodeDumpOutput(buf__o, self._o, cur__o, level, format, encoding)

    def saveFile(self, filename):
        """Dump an XML document to a file. Will use compression if
           compiled in and enabled. If @filename is "-" the stdout
           file is used. """
        ret = libxml2mod.xmlSaveFile(filename, self._o)
        return ret

    def saveFileEnc(self, filename, encoding):
        """Dump an XML document, converting it to the given encoding """
        ret = libxml2mod.xmlSaveFileEnc(filename, self._o, encoding)
        return ret

    def saveFileTo(self, buf, encoding):
        """Dump an XML document to an I/O buffer. """
        if buf is None: buf__o = None
        else: buf__o = buf._o
        ret = libxml2mod.xmlSaveFileTo(buf__o, self._o, encoding)
        return ret

    def saveFormatFile(self, filename, format):
        """Dump an XML document to a file. Will use compression if
           compiled in and enabled. If @filename is "-" the stdout
           file is used. If @format is set then the document will be
           indented on output. Note that @format = 1 provide node
           indenting only if xmlIndentTreeOutput = 1 or
           xmlKeepBlanksDefault(0) was called """
        ret = libxml2mod.xmlSaveFormatFile(filename, self._o, format)
        return ret

    def saveFormatFileEnc(self, filename, encoding, format):
        """Dump an XML document to a file or an URL. """
        ret = libxml2mod.xmlSaveFormatFileEnc(filename, self._o, encoding, format)
        return ret

    def saveFormatFileTo(self, buf, encoding, format):
        """Dump an XML document to an I/O buffer. """
        if buf is None: buf__o = None
        else: buf__o = buf._o
        ret = libxml2mod.xmlSaveFormatFileTo(buf__o, self._o, encoding, format)
        return ret

    def setDocCompressMode(self, mode):
        """set the compression ratio for a document, ZLIB based
           Correct values: 0 (uncompressed) to 9 (max compression) """
        libxml2mod.xmlSetDocCompressMode(self._o, mode)

    def stringGetNodeList(self, value):
        """Parse the value string and build the node list associated.
           Should produce a flat tree with only TEXTs and ENTITY_REFs. """
        ret = libxml2mod.xmlStringGetNodeList(self._o, value)
        if ret is None:raise treeError('xmlStringGetNodeList() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def stringLenGetNodeList(self, value, len):
        """Parse the value string and build the node list associated.
           Should produce a flat tree with only TEXTs and ENTITY_REFs. """
        ret = libxml2mod.xmlStringLenGetNodeList(self._o, value, len)
        if ret is None:raise treeError('xmlStringLenGetNodeList() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    #
    # xmlDoc functions from module valid
    #

    def ID(self, ID):
        """Search the attribute declaring the given ID """
        ret = libxml2mod.xmlGetID(self._o, ID)
        if ret is None:raise treeError('xmlGetID() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp

    def isMixedElement(self, name):
        """Search in the DtDs whether an element accept Mixed content
           (or ANY) basically if it is supposed to accept text childs """
        ret = libxml2mod.xmlIsMixedElement(self._o, name)
        return ret

    def removeID(self, attr):
        """Remove the given attribute from the ID table maintained
           internally. """
        if attr is None: attr__o = None
        else: attr__o = attr._o
        ret = libxml2mod.xmlRemoveID(self._o, attr__o)
        return ret

    def removeRef(self, attr):
        """Remove the given attribute from the Ref table maintained
           internally. """
        if attr is None: attr__o = None
        else: attr__o = attr._o
        ret = libxml2mod.xmlRemoveRef(self._o, attr__o)
        return ret

    #
    # xmlDoc functions from module xinclude
    #

    def xincludeProcess(self):
        """Implement the XInclude substitution on the XML document @doc """
        ret = libxml2mod.xmlXIncludeProcess(self._o)
        return ret

    #
    # xmlDoc functions from module xpath
    #

    def xpathNewContext(self):
        """Create a new xmlXPathContext """
        ret = libxml2mod.xmlXPathNewContext(self._o)
        if ret is None:raise xpathError('xmlXPathNewContext() failed')
        __tmp = xpathContext(_obj=ret)
        return __tmp

class xpathContext:
    def __init__(self, _obj=None):
        if _obj != None:self._o = _obj;return
        self._o = None

    # accessors for xpathContext
    def contextDoc(self):
        """Get the doc from an xpathContext """
        ret = libxml2mod.xmlXPathGetContextDoc(self._o)
        if ret is None:raise xpathError('xmlXPathGetContextDoc() failed')
        __tmp = xmlDoc(_obj=ret)
        return __tmp

    def contextNode(self):
        """Get the current node from an xpathContext """
        ret = libxml2mod.xmlXPathGetContextNode(self._o)
        if ret is None:raise xpathError('xmlXPathGetContextNode() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def contextPosition(self):
        """Get the current node from an xpathContext """
        ret = libxml2mod.xmlXPathGetContextPosition(self._o)
        return ret

    def contextSize(self):
        """Get the current node from an xpathContext """
        ret = libxml2mod.xmlXPathGetContextSize(self._o)
        return ret

    def function(self):
        """Get the current function name xpathContext """
        ret = libxml2mod.xmlXPathGetFunction(self._o)
        return ret

    def functionURI(self):
        """Get the current function name URI xpathContext """
        ret = libxml2mod.xmlXPathGetFunctionURI(self._o)
        return ret

    def setContextDoc(self, doc):
        """Set the doc of an xpathContext """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        libxml2mod.xmlXPathSetContextDoc(self._o, doc__o)

    def setContextNode(self, node):
        """Set the current node of an xpathContext """
        if node is None: node__o = None
        else: node__o = node._o
        libxml2mod.xmlXPathSetContextNode(self._o, node__o)

    #
    # xpathContext functions from module python
    #

    def registerXPathFunction(self, name, ns_uri, f):
        """Register a Python written function to the XPath interpreter """
        ret = libxml2mod.xmlRegisterXPathFunction(self._o, name, ns_uri, f)
        return ret

    #
    # xpathContext functions from module xpath
    #

    def xpathEval(self, str):
        """Evaluate the XPath Location Path in the given context. """
        ret = libxml2mod.xmlXPathEval(str, self._o)
        if ret is None:raise xpathError('xmlXPathEval() failed')
        return xpathObjectRet(ret)

    def xpathEvalExpression(self, str):
        """Evaluate the XPath expression in the given context. """
        ret = libxml2mod.xmlXPathEvalExpression(str, self._o)
        if ret is None:raise xpathError('xmlXPathEvalExpression() failed')
        return xpathObjectRet(ret)

    def xpathFreeContext(self):
        """Free up an xmlXPathContext """
        libxml2mod.xmlXPathFreeContext(self._o)

    #
    # xpathContext functions from module xpathInternals
    #

    def xpathNewParserContext(self, str):
        """Create a new xmlXPathParserContext """
        ret = libxml2mod.xmlXPathNewParserContext(str, self._o)
        if ret is None:raise xpathError('xmlXPathNewParserContext() failed')
        __tmp = xpathParserContext(_obj=ret)
        return __tmp

    def xpathNsLookup(self, prefix):
        """Search in the namespace declaration array of the context
           for the given namespace name associated to the given prefix """
        ret = libxml2mod.xmlXPathNsLookup(self._o, prefix)
        return ret

    def xpathRegisterAllFunctions(self):
        """Registers all default XPath functions in this context """
        libxml2mod.xmlXPathRegisterAllFunctions(self._o)

    def xpathRegisterNs(self, prefix, ns_uri):
        """Register a new namespace. If @ns_uri is None it unregisters
           the namespace """
        ret = libxml2mod.xmlXPathRegisterNs(self._o, prefix, ns_uri)
        return ret

    def xpathRegisteredFuncsCleanup(self):
        """Cleanup the XPath context data associated to registered
           functions """
        libxml2mod.xmlXPathRegisteredFuncsCleanup(self._o)

    def xpathRegisteredNsCleanup(self):
        """Cleanup the XPath context data associated to registered
           variables """
        libxml2mod.xmlXPathRegisteredNsCleanup(self._o)

    def xpathRegisteredVariablesCleanup(self):
        """Cleanup the XPath context data associated to registered
           variables """
        libxml2mod.xmlXPathRegisteredVariablesCleanup(self._o)

    def xpathVariableLookup(self, name):
        """Search in the Variable array of the context for the given
           variable value. """
        ret = libxml2mod.xmlXPathVariableLookup(self._o, name)
        if ret is None:raise xpathError('xmlXPathVariableLookup() failed')
        return xpathObjectRet(ret)

    def xpathVariableLookupNS(self, name, ns_uri):
        """Search in the Variable array of the context for the given
           variable value. """
        ret = libxml2mod.xmlXPathVariableLookupNS(self._o, name, ns_uri)
        if ret is None:raise xpathError('xmlXPathVariableLookupNS() failed')
        return xpathObjectRet(ret)

    #
    # xpathContext functions from module xpointer
    #

    def xpointerEval(self, str):
        """Evaluate the XPath Location Path in the given context. """
        ret = libxml2mod.xmlXPtrEval(str, self._o)
        if ret is None:raise treeError('xmlXPtrEval() failed')
        return xpathObjectRet(ret)

class xmlAttribute(xmlNode):
    def __init__(self, _obj=None):
        self._o = None
        xmlNode.__init__(self, _obj=_obj)

    def __repr__(self):
        return "<xmlAttribute (%s) object at 0x%x>" % (self.name, id (self))

class catalog:
    def __init__(self, _obj=None):
        if _obj != None:self._o = _obj;return
        self._o = None

    def __del__(self):
        if self._o != None:
            libxml2mod.xmlFreeCatalog(self._o)
        self._o = None

    #
    # catalog functions from module catalog
    #

    def add(self, type, orig, replace):
        """Add an entry in the catalog, it may overwrite existing but
           different entries. """
        ret = libxml2mod.xmlACatalogAdd(self._o, type, orig, replace)
        return ret

    def catalogIsEmpty(self):
        """Check is a catalog is empty """
        ret = libxml2mod.xmlCatalogIsEmpty(self._o)
        return ret

    def convertSGMLCatalog(self):
        """Convert all the SGML catalog entries as XML ones """
        ret = libxml2mod.xmlConvertSGMLCatalog(self._o)
        return ret

    def dump(self, out):
        """Free up all the memory associated with catalogs """
        libxml2mod.xmlACatalogDump(self._o, out)

    def freeCatalog(self):
        """Free the memory allocated to a Catalog """
        libxml2mod.xmlFreeCatalog(self._o)

    def remove(self, value):
        """Remove an entry from the catalog """
        ret = libxml2mod.xmlACatalogRemove(self._o, value)
        return ret

    def resolve(self, pubID, sysID):
        """Do a complete resolution lookup of an External Identifier """
        ret = libxml2mod.xmlACatalogResolve(self._o, pubID, sysID)
        return ret

    def resolvePublic(self, pubID):
        """Try to lookup the system ID associated to a public ID in
           that catalog """
        ret = libxml2mod.xmlACatalogResolvePublic(self._o, pubID)
        return ret

    def resolveSystem(self, sysID):
        """Try to lookup the catalog resource for a system ID """
        ret = libxml2mod.xmlACatalogResolveSystem(self._o, sysID)
        return ret

    def resolveURI(self, URI):
        """Do a complete resolution lookup of an URI """
        ret = libxml2mod.xmlACatalogResolveURI(self._o, URI)
        return ret

class xmlElement(xmlNode):
    def __init__(self, _obj=None):
        self._o = None
        xmlNode.__init__(self, _obj=_obj)

    def __repr__(self):
        return "<xmlElement (%s) object at 0x%x>" % (self.name, id (self))

class xmlAttr(xmlNode):
    def __init__(self, _obj=None):
        self._o = None
        xmlNode.__init__(self, _obj=_obj)

    def __repr__(self):
        return "<xmlAttr (%s) object at 0x%x>" % (self.name, id (self))

    #
    # xmlAttr functions from module debugXML
    #

    def debugDumpAttr(self, output, depth):
        """Dumps debug information for the attribute """
        libxml2mod.xmlDebugDumpAttr(output, self._o, depth)

    def debugDumpAttrList(self, output, depth):
        """Dumps debug information for the attribute list """
        libxml2mod.xmlDebugDumpAttrList(output, self._o, depth)

    #
    # xmlAttr functions from module tree
    #

    def freeProp(self):
        """Free one attribute, all the content is freed too """
        libxml2mod.xmlFreeProp(self._o)

    def freePropList(self):
        """Free a property and all its siblings, all the children are
           freed too. """
        libxml2mod.xmlFreePropList(self._o)

    def removeProp(self):
        """Unlink and free one attribute, all the content is freed too
           Note this doesn't work for namespace definition attributes """
        ret = libxml2mod.xmlRemoveProp(self._o)
        return ret

class xmlTextReader(xmlTextReaderCore):
    def __init__(self, _obj=None):
        self.input = None
        self._o = None
        xmlTextReaderCore.__init__(self, _obj=_obj)

    def __del__(self):
        if self._o != None:
            libxml2mod.xmlFreeTextReader(self._o)
        self._o = None

    #
    # xmlTextReader functions from module xmlreader
    #

    def AttributeCount(self):
        """Provides the number of attributes of the current node """
        ret = libxml2mod.xmlTextReaderAttributeCount(self._o)
        return ret

    def BaseUri(self):
        """The base URI of the node. """
        ret = libxml2mod.xmlTextReaderBaseUri(self._o)
        return ret

    def Close(self):
        """This method releases any resources allocated by the current
           instance changes the state to Closed and close any
           underlying input. """
        ret = libxml2mod.xmlTextReaderClose(self._o)
        return ret

    def CurrentDoc(self):
        """Hacking interface allowing to get the xmlDocPtr
           correponding to the current document being accessed by the
           xmlTextReader. This is dangerous because the associated
           node may be destroyed on the next Reads. """
        ret = libxml2mod.xmlTextReaderCurrentDoc(self._o)
        if ret is None:raise treeError('xmlTextReaderCurrentDoc() failed')
        __tmp = xmlDoc(_obj=ret)
        return __tmp

    def CurrentNode(self):
        """Hacking interface allowing to get the xmlNodePtr
           correponding to the current node being accessed by the
           xmlTextReader. This is dangerous because the underlying
           node may be destroyed on the next Reads. """
        ret = libxml2mod.xmlTextReaderCurrentNode(self._o)
        if ret is None:raise treeError('xmlTextReaderCurrentNode() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    def Depth(self):
        """The depth of the node in the tree. """
        ret = libxml2mod.xmlTextReaderDepth(self._o)
        return ret

    def GetAttribute(self, name):
        """Provides the value of the attribute with the specified
           qualified name. """
        ret = libxml2mod.xmlTextReaderGetAttribute(self._o, name)
        return ret

    def GetAttributeNo(self, no):
        """Provides the value of the attribute with the specified
           index relative to the containing element. """
        ret = libxml2mod.xmlTextReaderGetAttributeNo(self._o, no)
        return ret

    def GetAttributeNs(self, localName, namespaceURI):
        """Provides the value of the specified attribute """
        ret = libxml2mod.xmlTextReaderGetAttributeNs(self._o, localName, namespaceURI)
        return ret

    def GetParserProp(self, prop):
        """Read the parser internal property. """
        ret = libxml2mod.xmlTextReaderGetParserProp(self._o, prop)
        return ret

    def GetRemainder(self):
        """Method to get the remainder of the buffered XML. this
           method stops the parser, set its state to End Of File and
           return the input stream with what is left that the parser
           did not use. """
        ret = libxml2mod.xmlTextReaderGetRemainder(self._o)
        if ret is None:raise treeError('xmlTextReaderGetRemainder() failed')
        __tmp = inputBuffer(_obj=ret)
        return __tmp

    def HasAttributes(self):
        """Whether the node has attributes. """
        ret = libxml2mod.xmlTextReaderHasAttributes(self._o)
        return ret

    def HasValue(self):
        """Whether the node can have a text value. """
        ret = libxml2mod.xmlTextReaderHasValue(self._o)
        return ret

    def IsDefault(self):
        """Whether an Attribute  node was generated from the default
           value defined in the DTD or schema. """
        ret = libxml2mod.xmlTextReaderIsDefault(self._o)
        return ret

    def IsEmptyElement(self):
        """Check if the current node is empty """
        ret = libxml2mod.xmlTextReaderIsEmptyElement(self._o)
        return ret

    def LocalName(self):
        """The local name of the node. """
        ret = libxml2mod.xmlTextReaderLocalName(self._o)
        return ret

    def LookupNamespace(self, prefix):
        """Resolves a namespace prefix in the scope of the current
           element. """
        ret = libxml2mod.xmlTextReaderLookupNamespace(self._o, prefix)
        return ret

    def MoveToAttribute(self, name):
        """Moves the position of the current instance to the attribute
           with the specified qualified name. """
        ret = libxml2mod.xmlTextReaderMoveToAttribute(self._o, name)
        return ret

    def MoveToAttributeNo(self, no):
        """Moves the position of the current instance to the attribute
           with the specified index relative to the containing
           element. """
        ret = libxml2mod.xmlTextReaderMoveToAttributeNo(self._o, no)
        return ret

    def MoveToAttributeNs(self, localName, namespaceURI):
        """Moves the position of the current instance to the attribute
           with the specified local name and namespace URI. """
        ret = libxml2mod.xmlTextReaderMoveToAttributeNs(self._o, localName, namespaceURI)
        return ret

    def MoveToElement(self):
        """Moves the position of the current instance to the node that
           contains the current Attribute  node. """
        ret = libxml2mod.xmlTextReaderMoveToElement(self._o)
        return ret

    def MoveToFirstAttribute(self):
        """Moves the position of the current instance to the first
           attribute associated with the current node. """
        ret = libxml2mod.xmlTextReaderMoveToFirstAttribute(self._o)
        return ret

    def MoveToNextAttribute(self):
        """Moves the position of the current instance to the next
           attribute associated with the current node. """
        ret = libxml2mod.xmlTextReaderMoveToNextAttribute(self._o)
        return ret

    def Name(self):
        """The qualified name of the node, equal to Prefix :LocalName. """
        ret = libxml2mod.xmlTextReaderName(self._o)
        return ret

    def NamespaceUri(self):
        """The URI defining the namespace associated with the node. """
        ret = libxml2mod.xmlTextReaderNamespaceUri(self._o)
        return ret

    def NodeType(self):
        """Get the node type of the current node Reference:
           http://dotgnu.org/pnetlib-doc/System/Xml/XmlNodeType.html """
        ret = libxml2mod.xmlTextReaderNodeType(self._o)
        return ret

    def Normalization(self):
        """The value indicating whether to normalize white space and
           attribute values. Since attribute value and end of line
           normalizations are a MUST in the XML specification only
           the value true is accepted. The broken bahaviour of
           accepting out of range character entities like &#0; is of
           course not supported either. """
        ret = libxml2mod.xmlTextReaderNormalization(self._o)
        return ret

    def Prefix(self):
        """A shorthand reference to the namespace associated with the
           node. """
        ret = libxml2mod.xmlTextReaderPrefix(self._o)
        return ret

    def QuoteChar(self):
        """The quotation mark character used to enclose the value of
           an attribute. """
        ret = libxml2mod.xmlTextReaderQuoteChar(self._o)
        return ret

    def Read(self):
        """Moves the position of the current instance to the next node
           in the stream, exposing its properties. """
        ret = libxml2mod.xmlTextReaderRead(self._o)
        return ret

    def ReadAttributeValue(self):
        """Parses an attribute value into one or more Text and
           EntityReference nodes. """
        ret = libxml2mod.xmlTextReaderReadAttributeValue(self._o)
        return ret

    def ReadInnerXml(self):
        """Reads the contents of the current node, including child
           nodes and markup. """
        ret = libxml2mod.xmlTextReaderReadInnerXml(self._o)
        return ret

    def ReadOuterXml(self):
        """Reads the contents of the current node, including child
           nodes and markup. """
        ret = libxml2mod.xmlTextReaderReadOuterXml(self._o)
        return ret

    def ReadState(self):
        """Gets the read state of the reader. """
        ret = libxml2mod.xmlTextReaderReadState(self._o)
        return ret

    def ReadString(self):
        """Reads the contents of an element or a text node as a string. """
        ret = libxml2mod.xmlTextReaderReadString(self._o)
        return ret

    def SetParserProp(self, prop, value):
        """Change the parser processing behaviour by changing some of
           its internal properties. Note that some properties can
           only be changed before any read has been done. """
        ret = libxml2mod.xmlTextReaderSetParserProp(self._o, prop, value)
        return ret

    def Value(self):
        """Provides the text value of the node if present """
        ret = libxml2mod.xmlTextReaderValue(self._o)
        return ret

    def XmlLang(self):
        """The xml:lang scope within which the node resides. """
        ret = libxml2mod.xmlTextReaderXmlLang(self._o)
        return ret

class xmlReg:
    def __init__(self, _obj=None):
        if _obj != None:self._o = _obj;return
        self._o = None

    def __del__(self):
        if self._o != None:
            libxml2mod.xmlRegFreeRegexp(self._o)
        self._o = None

    #
    # xmlReg functions from module xmlregexp
    #

    def regexpExec(self, content):
        """Check if the regular expression generate the value """
        ret = libxml2mod.xmlRegexpExec(self._o, content)
        return ret

    def regexpFreeRegexp(self):
        """Free a regexp """
        libxml2mod.xmlRegFreeRegexp(self._o)

    def regexpIsDeterminist(self):
        """Check if the regular expression is determinist """
        ret = libxml2mod.xmlRegexpIsDeterminist(self._o)
        return ret

    def regexpPrint(self, output):
        """Print the content of the compiled regular expression """
        libxml2mod.xmlRegexpPrint(output, self._o)

class xmlEntity(xmlNode):
    def __init__(self, _obj=None):
        self._o = None
        xmlNode.__init__(self, _obj=_obj)

    def __repr__(self):
        return "<xmlEntity (%s) object at 0x%x>" % (self.name, id (self))

    #
    # xmlEntity functions from module parserInternals
    #

    def handleEntity(self, ctxt):
        """Default handling of defined entities, when should we define
           a new input stream ? When do we just handle that as a set
           of chars ?  OBSOLETE: to be removed at some point. """
        if ctxt is None: ctxt__o = None
        else: ctxt__o = ctxt._o
        libxml2mod.xmlHandleEntity(ctxt__o, self._o)

class relaxNgSchema:
    def __init__(self, _obj=None):
        if _obj != None:self._o = _obj;return
        self._o = None

    def __del__(self):
        if self._o != None:
            libxml2mod.xmlRelaxNGFree(self._o)
        self._o = None

    #
    # relaxNgSchema functions from module relaxng
    #

    def relaxNGDump(self, output):
        """Dump a RelaxNG structure back """
        libxml2mod.xmlRelaxNGDump(output, self._o)

    def relaxNGDumpTree(self, output):
        """Dump the transformed RelaxNG tree. """
        libxml2mod.xmlRelaxNGDumpTree(output, self._o)

    def relaxNGFree(self):
        """Deallocate a RelaxNG structure. """
        libxml2mod.xmlRelaxNGFree(self._o)

    def relaxNGNewValidCtxt(self):
        """Create an XML RelaxNGs validation context based on the
           given schema """
        ret = libxml2mod.xmlRelaxNGNewValidCtxt(self._o)
        if ret is None:raise treeError('xmlRelaxNGNewValidCtxt() failed')
        __tmp = relaxNgValidCtxt(_obj=ret)
        __tmp.schema = self
        return __tmp

class relaxNgValidCtxt:
    def __init__(self, _obj=None):
        self.schema = None
        if _obj != None:self._o = _obj;return
        self._o = None

    def __del__(self):
        if self._o != None:
            libxml2mod.xmlRelaxNGFreeValidCtxt(self._o)
        self._o = None

    #
    # relaxNgValidCtxt functions from module relaxng
    #

    def relaxNGFreeValidCtxt(self):
        """Free the resources associated to the schema validation
           context """
        libxml2mod.xmlRelaxNGFreeValidCtxt(self._o)

class xpathParserContext:
    def __init__(self, _obj=None):
        if _obj != None:self._o = _obj;return
        self._o = None

    # accessors for xpathParserContext
    def context(self):
        """Get the xpathContext from an xpathParserContext """
        ret = libxml2mod.xmlXPathParserGetContext(self._o)
        if ret is None:raise xpathError('xmlXPathParserGetContext() failed')
        __tmp = xpathContext(_obj=ret)
        return __tmp

    #
    # xpathParserContext functions from module xpathInternals
    #

    def xpathAddValues(self):
        """Implement the add operation on XPath objects: The numeric
           operators convert their operands to numbers as if by
           calling the number function. """
        libxml2mod.xmlXPathAddValues(self._o)

    def xpathBooleanFunction(self, nargs):
        """Implement the boolean() XPath function boolean
           boolean(object) he boolean function converts its argument
           to a boolean as follows: - a number is true if and only if
           it is neither positive or negative zero nor NaN - a
           node-set is true if and only if it is non-empty - a string
           is true if and only if its length is non-zero """
        libxml2mod.xmlXPathBooleanFunction(self._o, nargs)

    def xpathCeilingFunction(self, nargs):
        """Implement the ceiling() XPath function number
           ceiling(number) The ceiling function returns the smallest
           (closest to negative infinity) number that is not less
           than the argument and that is an integer. """
        libxml2mod.xmlXPathCeilingFunction(self._o, nargs)

    def xpathCompareValues(self, inf, strict):
        """Implement the compare operation on XPath objects: @arg1 <
           @arg2    (1, 1, ... @arg1 <= @arg2   (1, 0, ... @arg1 >
           @arg2    (0, 1, ... @arg1 >= @arg2   (0, 0, ...  When
           neither object to be compared is a node-set and the
           operator is <=, <, >=, >, then the objects are compared by
           converted both objects to numbers and comparing the
           numbers according to IEEE 754. The < comparison will be
           true if and only if the first number is less than the
           second number. The <= comparison will be true if and only
           if the first number is less than or equal to the second
           number. The > comparison will be true if and only if the
           first number is greater than the second number. The >=
           comparison will be true if and only if the first number is
           greater than or equal to the second number. """
        ret = libxml2mod.xmlXPathCompareValues(self._o, inf, strict)
        return ret

    def xpathConcatFunction(self, nargs):
        """Implement the concat() XPath function string concat(string,
           string, string*) The concat function returns the
           concatenation of its arguments. """
        libxml2mod.xmlXPathConcatFunction(self._o, nargs)

    def xpathContainsFunction(self, nargs):
        """Implement the contains() XPath function boolean
           contains(string, string) The contains function returns
           true if the first argument string contains the second
           argument string, and otherwise returns false. """
        libxml2mod.xmlXPathContainsFunction(self._o, nargs)

    def xpathCountFunction(self, nargs):
        """Implement the count() XPath function number count(node-set) """
        libxml2mod.xmlXPathCountFunction(self._o, nargs)

    def xpathDivValues(self):
        """Implement the div operation on XPath objects @arg1 / @arg2:
           The numeric operators convert their operands to numbers as
           if by calling the number function. """
        libxml2mod.xmlXPathDivValues(self._o)

    def xpathEqualValues(self):
        """Implement the equal operation on XPath objects content:
           @arg1 == @arg2 """
        ret = libxml2mod.xmlXPathEqualValues(self._o)
        return ret

    def xpathEvalExpr(self):
        """Parse and evaluate an XPath expression in the given
           context, then push the result on the context stack """
        libxml2mod.xmlXPathEvalExpr(self._o)

    def xpathFalseFunction(self, nargs):
        """Implement the false() XPath function boolean false() """
        libxml2mod.xmlXPathFalseFunction(self._o, nargs)

    def xpathFloorFunction(self, nargs):
        """Implement the floor() XPath function number floor(number)
           The floor function returns the largest (closest to
           positive infinity) number that is not greater than the
           argument and that is an integer. """
        libxml2mod.xmlXPathFloorFunction(self._o, nargs)

    def xpathFreeParserContext(self):
        """Free up an xmlXPathParserContext """
        libxml2mod.xmlXPathFreeParserContext(self._o)

    def xpathIdFunction(self, nargs):
        """Implement the id() XPath function node-set id(object) The
           id function selects elements by their unique ID (see
           [5.2.1 Unique IDs]). When the argument to id is of type
           node-set, then the result is the union of the result of
           applying id to the string value of each of the nodes in
           the argument node-set. When the argument to id is of any
           other type, the argument is converted to a string as if by
           a call to the string function; the string is split into a
           whitespace-separated list of tokens (whitespace is any
           sequence of characters matching the production S); the
           result is a node-set containing the elements in the same
           document as the context node that have a unique ID equal
           to any of the tokens in the list. """
        libxml2mod.xmlXPathIdFunction(self._o, nargs)

    def xpathLangFunction(self, nargs):
        """Implement the lang() XPath function boolean lang(string)
           The lang function returns true or false depending on
           whether the language of the context node as specified by
           xml:lang attributes is the same as or is a sublanguage of
           the language specified by the argument string. The
           language of the context node is determined by the value of
           the xml:lang attribute on the context node, or, if the
           context node has no xml:lang attribute, by the value of
           the xml:lang attribute on the nearest ancestor of the
           context node that has an xml:lang attribute. If there is
           no such attribute, then lang """
        libxml2mod.xmlXPathLangFunction(self._o, nargs)

    def xpathLastFunction(self, nargs):
        """Implement the last() XPath function number last() The last
           function returns the number of nodes in the context node
           list. """
        libxml2mod.xmlXPathLastFunction(self._o, nargs)

    def xpathLocalNameFunction(self, nargs):
        """Implement the local-name() XPath function string
           local-name(node-set?) The local-name function returns a
           string containing the local part of the name of the node
           in the argument node-set that is first in document order.
           If the node-set is empty or the first node has no name, an
           empty string is returned. If the argument is omitted it
           defaults to the context node. """
        libxml2mod.xmlXPathLocalNameFunction(self._o, nargs)

    def xpathModValues(self):
        """Implement the mod operation on XPath objects: @arg1 / @arg2
           The numeric operators convert their operands to numbers as
           if by calling the number function. """
        libxml2mod.xmlXPathModValues(self._o)

    def xpathMultValues(self):
        """Implement the multiply operation on XPath objects: The
           numeric operators convert their operands to numbers as if
           by calling the number function. """
        libxml2mod.xmlXPathMultValues(self._o)

    def xpathNamespaceURIFunction(self, nargs):
        """Implement the namespace-uri() XPath function string
           namespace-uri(node-set?) The namespace-uri function
           returns a string containing the namespace URI of the
           expanded name of the node in the argument node-set that is
           first in document order. If the node-set is empty, the
           first node has no name, or the expanded name has no
           namespace URI, an empty string is returned. If the
           argument is omitted it defaults to the context node. """
        libxml2mod.xmlXPathNamespaceURIFunction(self._o, nargs)

    def xpathNormalizeFunction(self, nargs):
        """Implement the normalize-space() XPath function string
           normalize-space(string?) The normalize-space function
           returns the argument string with white space normalized by
           stripping leading and trailing whitespace and replacing
           sequences of whitespace characters by a single space.
           Whitespace characters are the same allowed by the S
           production in XML. If the argument is omitted, it defaults
           to the context node converted to a string, in other words
           the value of the context node. """
        libxml2mod.xmlXPathNormalizeFunction(self._o, nargs)

    def xpathNotEqualValues(self):
        """Implement the equal operation on XPath objects content:
           @arg1 == @arg2 """
        ret = libxml2mod.xmlXPathNotEqualValues(self._o)
        return ret

    def xpathNotFunction(self, nargs):
        """Implement the not() XPath function boolean not(boolean) The
           not function returns true if its argument is false, and
           false otherwise. """
        libxml2mod.xmlXPathNotFunction(self._o, nargs)

    def xpathNumberFunction(self, nargs):
        """Implement the number() XPath function number number(object?) """
        libxml2mod.xmlXPathNumberFunction(self._o, nargs)

    def xpathParseNCName(self):
        """parse an XML namespace non qualified name.  [NS 3] NCName
           ::= (Letter | '_') (NCNameChar)*  [NS 4] NCNameChar ::=
           Letter | Digit | '.' | '-' | '_' | CombiningChar | Extender """
        ret = libxml2mod.xmlXPathParseNCName(self._o)
        return ret

    def xpathParseName(self):
        """parse an XML name  [4] NameChar ::= Letter | Digit | '.' |
           '-' | '_' | ':' | CombiningChar | Extender  [5] Name ::=
           (Letter | '_' | ':') (NameChar)* """
        ret = libxml2mod.xmlXPathParseName(self._o)
        return ret

    def xpathPopBoolean(self):
        """Pops a boolean from the stack, handling conversion if
           needed. Check error with #xmlXPathCheckError. """
        ret = libxml2mod.xmlXPathPopBoolean(self._o)
        return ret

    def xpathPopNumber(self):
        """Pops a number from the stack, handling conversion if
           needed. Check error with #xmlXPathCheckError. """
        ret = libxml2mod.xmlXPathPopNumber(self._o)
        return ret

    def xpathPopString(self):
        """Pops a string from the stack, handling conversion if
           needed. Check error with #xmlXPathCheckError. """
        ret = libxml2mod.xmlXPathPopString(self._o)
        return ret

    def xpathPositionFunction(self, nargs):
        """Implement the position() XPath function number position()
           The position function returns the position of the context
           node in the context node list. The first position is 1,
           and so the last position will be equal to last(). """
        libxml2mod.xmlXPathPositionFunction(self._o, nargs)

    def xpathRoot(self):
        """Initialize the context to the root of the document """
        libxml2mod.xmlXPathRoot(self._o)

    def xpathRoundFunction(self, nargs):
        """Implement the round() XPath function number round(number)
           The round function returns the number that is closest to
           the argument and that is an integer. If there are two such
           numbers, then the one that is even is returned. """
        libxml2mod.xmlXPathRoundFunction(self._o, nargs)

    def xpathStartsWithFunction(self, nargs):
        """Implement the starts-with() XPath function boolean
           starts-with(string, string) The starts-with function
           returns true if the first argument string starts with the
           second argument string, and otherwise returns false. """
        libxml2mod.xmlXPathStartsWithFunction(self._o, nargs)

    def xpathStringFunction(self, nargs):
        """Implement the string() XPath function string
           string(object?) he string function converts an object to a
           string as follows: - A node-set is converted to a string
           by returning the value of the node in the node-set that is
           first in document order. If the node-set is empty, an
           empty string is returned. - A number is converted to a
           string as follows + NaN is converted to the string NaN +
           positive zero is converted to the string 0 + negative zero
           is converted to the string 0 + positive infinity is
           converted to the string Infinity + negative infinity is
           converted to the string -Infinity + if the number is an
           integer, the number is represented in decimal form as a
           Number with no decimal point and no leading zeros,
           preceded by a minus sign (-) if the number is negative +
           otherwise, the number is represented in decimal form as a
           Number including a decimal point with at least one digit
           before the decimal point and at least one digit after the
           decimal point, preceded by a minus sign (-) if the number
           is negative; there must be no leading zeros before the
           decimal point apart possibly from the one required digit
           immediately before the decimal point; beyond the one
           required digit after the decimal point there must be as
           many, but only as many, more digits as are needed to
           uniquely distinguish the number from all other IEEE 754
           numeric values. - The boolean false value is converted to
           the string false. The boolean true value is converted to
           the string true.  If the argument is omitted, it defaults
           to a node-set with the context node as its only member. """
        libxml2mod.xmlXPathStringFunction(self._o, nargs)

    def xpathStringLengthFunction(self, nargs):
        """Implement the string-length() XPath function number
           string-length(string?) The string-length returns the
           number of characters in the string (see [3.6 Strings]). If
           the argument is omitted, it defaults to the context node
           converted to a string, in other words the value of the
           context node. """
        libxml2mod.xmlXPathStringLengthFunction(self._o, nargs)

    def xpathSubValues(self):
        """Implement the subtraction operation on XPath objects: The
           numeric operators convert their operands to numbers as if
           by calling the number function. """
        libxml2mod.xmlXPathSubValues(self._o)

    def xpathSubstringAfterFunction(self, nargs):
        """Implement the substring-after() XPath function string
           substring-after(string, string) The substring-after
           function returns the substring of the first argument
           string that follows the first occurrence of the second
           argument string in the first argument string, or the empty
           stringi if the first argument string does not contain the
           second argument string. For example,
           substring-after("1999/04/01","/") returns 04/01, and
           substring-after("1999/04/01","19") returns 99/04/01. """
        libxml2mod.xmlXPathSubstringAfterFunction(self._o, nargs)

    def xpathSubstringBeforeFunction(self, nargs):
        """Implement the substring-before() XPath function string
           substring-before(string, string) The substring-before
           function returns the substring of the first argument
           string that precedes the first occurrence of the second
           argument string in the first argument string, or the empty
           string if the first argument string does not contain the
           second argument string. For example,
           substring-before("1999/04/01","/") returns 1999. """
        libxml2mod.xmlXPathSubstringBeforeFunction(self._o, nargs)

    def xpathSubstringFunction(self, nargs):
        """Implement the substring() XPath function string
           substring(string, number, number?) The substring function
           returns the substring of the first argument starting at
           the position specified in the second argument with length
           specified in the third argument. For example,
           substring("12345",2,3) returns "234". If the third
           argument is not specified, it returns the substring
           starting at the position specified in the second argument
           and continuing to the end of the string. For example,
           substring("12345",2) returns "2345".  More precisely, each
           character in the string (see [3.6 Strings]) is considered
           to have a numeric position: the position of the first
           character is 1, the position of the second character is 2
           and so on. The returned substring contains those
           characters for which the position of the character is
           greater than or equal to the second argument and, if the
           third argument is specified, less than the sum of the
           second and third arguments; the comparisons and addition
           used for the above follow the standard IEEE 754 rules.
           Thus: - substring("12345", 1.5, 2.6) returns "234" -
           substring("12345", 0, 3) returns "12" - substring("12345",
           0 div 0, 3) returns "" - substring("12345", 1, 0 div 0)
           returns "" - substring("12345", -42, 1 div 0) returns
           "12345" - substring("12345", -1 div 0, 1 div 0) returns "" """
        libxml2mod.xmlXPathSubstringFunction(self._o, nargs)

    def xpathSumFunction(self, nargs):
        """Implement the sum() XPath function number sum(node-set) The
           sum function returns the sum of the values of the nodes in
           the argument node-set. """
        libxml2mod.xmlXPathSumFunction(self._o, nargs)

    def xpathTranslateFunction(self, nargs):
        """Implement the translate() XPath function string
           translate(string, string, string) The translate function
           returns the first argument string with occurrences of
           characters in the second argument string replaced by the
           character at the corresponding position in the third
           argument string. For example, translate("bar","abc","ABC")
           returns the string BAr. If there is a character in the
           second argument string with no character at a
           corresponding position in the third argument string
           (because the second argument string is longer than the
           third argument string), then occurrences of that character
           in the first argument string are removed. For example,
           translate("--aaa--","abc-","ABC") """
        libxml2mod.xmlXPathTranslateFunction(self._o, nargs)

    def xpathTrueFunction(self, nargs):
        """Implement the true() XPath function boolean true() """
        libxml2mod.xmlXPathTrueFunction(self._o, nargs)

    def xpathValueFlipSign(self):
        """Implement the unary - operation on an XPath object The
           numeric operators convert their operands to numbers as if
           by calling the number function. """
        libxml2mod.xmlXPathValueFlipSign(self._o)

    def xpatherror(self, file, line, no):
        """Formats an error message. """
        libxml2mod.xmlXPatherror(self._o, file, line, no)

    #
    # xpathParserContext functions from module xpointer
    #

    def xpointerEvalRangePredicate(self):
        """[8]   Predicate ::=   '[' PredicateExpr ']' [9]  
           PredicateExpr ::=   Expr  Evaluate a predicate as in
           xmlXPathEvalPredicate() but for a Location Set instead of
           a node set """
        libxml2mod.xmlXPtrEvalRangePredicate(self._o)

    def xpointerRangeToFunction(self, nargs):
        """Implement the range-to() XPointer function """
        libxml2mod.xmlXPtrRangeToFunction(self._o, nargs)

class parserCtxt(parserCtxtCore):
    def __init__(self, _obj=None):
        self._o = None
        parserCtxtCore.__init__(self, _obj=_obj)

    def __del__(self):
        if self._o != None:
            libxml2mod.xmlFreeParserCtxt(self._o)
        self._o = None

    # accessors for parserCtxt
    def doc(self):
        """Get the document tree from a parser context. """
        ret = libxml2mod.xmlParserGetDoc(self._o)
        if ret is None:raise parserError('xmlParserGetDoc() failed')
        __tmp = xmlDoc(_obj=ret)
        return __tmp

    def isValid(self):
        """Get the validity information from a parser context. """
        ret = libxml2mod.xmlParserGetIsValid(self._o)
        return ret

    def lineNumbers(self, linenumbers):
        """Switch on the generation of line number for elements nodes. """
        libxml2mod.xmlParserSetLineNumbers(self._o, linenumbers)

    def loadSubset(self, loadsubset):
        """Switch the parser to load the DTD without validating. """
        libxml2mod.xmlParserSetLoadSubset(self._o, loadsubset)

    def pedantic(self, pedantic):
        """Switch the parser to be pedantic. """
        libxml2mod.xmlParserSetPedantic(self._o, pedantic)

    def replaceEntities(self, replaceEntities):
        """Switch the parser to replace entities. """
        libxml2mod.xmlParserSetReplaceEntities(self._o, replaceEntities)

    def validate(self, validate):
        """Switch the parser to validation mode. """
        libxml2mod.xmlParserSetValidate(self._o, validate)

    def wellFormed(self):
        """Get the well formed information from a parser context. """
        ret = libxml2mod.xmlParserGetWellFormed(self._o)
        return ret

    #
    # parserCtxt functions from module HTMLparser
    #

    def htmlFreeParserCtxt(self):
        """Free all the memory used by a parser context. However the
           parsed document in ctxt->myDoc is not freed. """
        libxml2mod.htmlFreeParserCtxt(self._o)

    def htmlParseCharRef(self):
        """parse Reference declarations  [66] CharRef ::= '&#' [0-9]+
           ';' | '&#x' [0-9a-fA-F]+ ';' """
        ret = libxml2mod.htmlParseCharRef(self._o)
        return ret

    def htmlParseChunk(self, chunk, size, terminate):
        """Parse a Chunk of memory """
        ret = libxml2mod.htmlParseChunk(self._o, chunk, size, terminate)
        return ret

    def htmlParseDocument(self):
        """parse an HTML document (and build a tree if using the
           standard SAX interface). """
        ret = libxml2mod.htmlParseDocument(self._o)
        return ret

    def htmlParseElement(self):
        """parse an HTML element, this is highly recursive  [39]
           element ::= EmptyElemTag | STag content ETag  [41]
           Attribute ::= Name Eq AttValue """
        libxml2mod.htmlParseElement(self._o)

    #
    # parserCtxt functions from module parser
    #

    def clearParserCtxt(self):
        """Clear (release owned resources) and reinitialize a parser
           context """
        libxml2mod.xmlClearParserCtxt(self._o)

    def initParserCtxt(self):
        """Initialize a parser context """
        libxml2mod.xmlInitParserCtxt(self._o)

    def parseChunk(self, chunk, size, terminate):
        """Parse a Chunk of memory """
        ret = libxml2mod.xmlParseChunk(self._o, chunk, size, terminate)
        return ret

    def parseDocument(self):
        """parse an XML document (and build a tree if using the
           standard SAX interface).  [1] document ::= prolog element
           Misc*  [22] prolog ::= XMLDecl? Misc* (doctypedecl Misc*)? """
        ret = libxml2mod.xmlParseDocument(self._o)
        return ret

    def parseExtParsedEnt(self):
        """parse a general parsed entity An external general parsed
           entity is well-formed if it matches the production labeled
           extParsedEnt.  [78] extParsedEnt ::= TextDecl? content """
        ret = libxml2mod.xmlParseExtParsedEnt(self._o)
        return ret

    def setupParserForBuffer(self, buffer, filename):
        """Setup the parser context to parse a new buffer; Clears any
           prior contents from the parser context. The buffer
           parameter must not be None, but the filename parameter can
           be """
        libxml2mod.xmlSetupParserForBuffer(self._o, buffer, filename)

    def stopParser(self):
        """Blocks further parser processing """
        libxml2mod.xmlStopParser(self._o)

    #
    # parserCtxt functions from module parserInternals
    #

    def decodeEntities(self, len, what, end, end2, end3):
        """This function is deprecated, we now always process entities
           content through xmlStringDecodeEntities  TODO: remove it
           in next major release.  [67] Reference ::= EntityRef |
           CharRef  [69] PEReference ::= '%' Name ';' """
        ret = libxml2mod.xmlDecodeEntities(self._o, len, what, end, end2, end3)
        return ret

    def namespaceParseNCName(self):
        """parse an XML namespace name.  TODO: this seems not in use
           anymore, the namespace handling is done on top of the SAX
           interfaces, i.e. not on raw input.  [NS 3] NCName ::=
           (Letter | '_') (NCNameChar)*  [NS 4] NCNameChar ::= Letter
           | Digit | '.' | '-' | '_' | CombiningChar | Extender """
        ret = libxml2mod.xmlNamespaceParseNCName(self._o)
        return ret

    def namespaceParseNSDef(self):
        """parse a namespace prefix declaration  TODO: this seems not
           in use anymore, the namespace handling is done on top of
           the SAX interfaces, i.e. not on raw input.  [NS 1] NSDef
           ::= PrefixDef Eq SystemLiteral  [NS 2] PrefixDef ::=
           'xmlns' (':' NCName)? """
        ret = libxml2mod.xmlNamespaceParseNSDef(self._o)
        return ret

    def nextChar(self):
        """Skip to the next char input char. """
        libxml2mod.xmlNextChar(self._o)

    def parseAttValue(self):
        """parse a value for an attribute Note: the parser won't do
           substitution of entities here, this will be handled later
           in xmlStringGetNodeList  [10] AttValue ::= '"' ([^<&"] |
           Reference)* '"' | "'" ([^<&'] | Reference)* "'"  3.3.3
           Attribute-Value Normalization: Before the value of an
           attribute is passed to the application or checked for
           validity, the XML processor must normalize it as follows:
           - a character reference is processed by appending the
           referenced character to the attribute value - an entity
           reference is processed by recursively processing the
           replacement text of the entity - a whitespace character
           (#x20, #xD, #xA, #x9) is processed by appending #x20 to
           the normalized value, except that only a single #x20 is
           appended for a "#xD#xA" sequence that is part of an
           external parsed entity or the literal entity value of an
           internal parsed entity - other characters are processed by
           appending them to the normalized value If the declared
           value is not CDATA, then the XML processor must further
           process the normalized attribute value by discarding any
           leading and trailing space (#x20) characters, and by
           replacing sequences of space (#x20) characters by a single
           space (#x20) character. All attributes for which no
           declaration has been read should be treated by a
           non-validating parser as if declared CDATA. """
        ret = libxml2mod.xmlParseAttValue(self._o)
        return ret

    def parseAttributeListDecl(self):
        """: parse the Attribute list def for an element  [52]
           AttlistDecl ::= '<!ATTLIST' S Name AttDef* S? '>'  [53]
           AttDef ::= S Name S AttType S DefaultDecl """
        libxml2mod.xmlParseAttributeListDecl(self._o)

    def parseCDSect(self):
        """Parse escaped pure raw content.  [18] CDSect ::= CDStart
           CData CDEnd  [19] CDStart ::= '<![CDATA['  [20] Data ::=
           (Char* - (Char* ']]>' Char*))  [21] CDEnd ::= ']]>' """
        libxml2mod.xmlParseCDSect(self._o)

    def parseCharData(self, cdata):
        """parse a CharData section. if we are within a CDATA section
           ']]>' marks an end of section.  The right angle bracket
           (>) may be represented using the string "&gt;", and must,
           for compatibility, be escaped using "&gt;" or a character
           reference when it appears in the string "]]>" in content,
           when that string is not marking the end of a CDATA
           section.  [14] CharData ::= [^<&]* - ([^<&]* ']]>' [^<&]*) """
        libxml2mod.xmlParseCharData(self._o, cdata)

    def parseCharRef(self):
        """parse Reference declarations  [66] CharRef ::= '&#' [0-9]+
           ';' | '&#x' [0-9a-fA-F]+ ';'  [ WFC: Legal Character ]
           Characters referred to using character references must
           match the production for Char. """
        ret = libxml2mod.xmlParseCharRef(self._o)
        return ret

    def parseComment(self):
        """Skip an XML (SGML) comment <!-- .... --> The spec says that
           "For compatibility, the string "--" (double-hyphen) must
           not occur within comments. "  [15] Comment ::= '<!--'
           ((Char - '-') | ('-' (Char - '-')))* '-->' """
        libxml2mod.xmlParseComment(self._o)

    def parseContent(self):
        """Parse a content:  [43] content ::= (element | CharData |
           Reference | CDSect | PI | Comment)* """
        libxml2mod.xmlParseContent(self._o)

    def parseDocTypeDecl(self):
        """parse a DOCTYPE declaration  [28] doctypedecl ::=
           '<!DOCTYPE' S Name (S ExternalID)? S? ('[' (markupdecl |
           PEReference | S)* ']' S?)? '>'  [ VC: Root Element Type ]
           The Name in the document type declaration must match the
           element type of the root element. """
        libxml2mod.xmlParseDocTypeDecl(self._o)

    def parseElement(self):
        """parse an XML element, this is highly recursive  [39]
           element ::= EmptyElemTag | STag content ETag  [ WFC:
           Element Type Match ] The Name in an element's end-tag must
           match the element type in the start-tag.  [ VC: Element
           Valid ] An element is valid if there is a declaration
           matching elementdecl where the Name matches the element
           type and one of the following holds: - The declaration
           matches EMPTY and the element has no content. - The
           declaration matches children and the sequence of child
           elements belongs to the language generated by the regular
           expression in the content model, with optional white space
           (characters matching the nonterminal S) between each pair
           of child elements. - The declaration matches Mixed and the
           content consists of character data and child elements
           whose types match names in the content model. - The
           declaration matches ANY, and the types of any child
           elements have been declared. """
        libxml2mod.xmlParseElement(self._o)

    def parseElementDecl(self):
        """parse an Element declaration.  [45] elementdecl ::=
           '<!ELEMENT' S Name S contentspec S? '>'  [ VC: Unique
           Element Type Declaration ] No element type may be declared
           more than once """
        ret = libxml2mod.xmlParseElementDecl(self._o)
        return ret

    def parseEncName(self):
        """parse the XML encoding name  [81] EncName ::= [A-Za-z]
           ([A-Za-z0-9._] | '-')* """
        ret = libxml2mod.xmlParseEncName(self._o)
        return ret

    def parseEncodingDecl(self):
        """parse the XML encoding declaration  [80] EncodingDecl ::= S
           'encoding' Eq ('"' EncName '"' |  "'" EncName "'")  this
           setups the conversion filters. """
        ret = libxml2mod.xmlParseEncodingDecl(self._o)
        return ret

    def parseEndTag(self):
        """parse an end of tag  [42] ETag ::= '</' Name S? '>'  With
           namespace  [NS 9] ETag ::= '</' QName S? '>' """
        libxml2mod.xmlParseEndTag(self._o)

    def parseEntityDecl(self):
        """parse <!ENTITY declarations  [70] EntityDecl ::= GEDecl |
           PEDecl  [71] GEDecl ::= '<!ENTITY' S Name S EntityDef S?
           '>'  [72] PEDecl ::= '<!ENTITY' S '%' S Name S PEDef S?
           '>'  [73] EntityDef ::= EntityValue | (ExternalID
           NDataDecl?)  [74] PEDef ::= EntityValue | ExternalID  [76]
           NDataDecl ::= S 'NDATA' S Name  [ VC: Notation Declared ]
           The Name must match the declared name of a notation. """
        libxml2mod.xmlParseEntityDecl(self._o)

    def parseEntityRef(self):
        """parse ENTITY references declarations  [68] EntityRef ::=
           '&' Name ';'  [ WFC: Entity Declared ] In a document
           without any DTD, a document with only an internal DTD
           subset which contains no parameter entity references, or a
           document with "standalone='yes'", the Name given in the
           entity reference must match that in an entity declaration,
           except that well-formed documents need not declare any of
           the following entities: amp, lt, gt, apos, quot.  The
           declaration of a parameter entity must precede any
           reference to it.  Similarly, the declaration of a general
           entity must precede any reference to it which appears in a
           default value in an attribute-list declaration. Note that
           if entities are declared in the external subset or in
           external parameter entities, a non-validating processor is
           not obligated to read and process their declarations; for
           such documents, the rule that an entity must be declared
           is a well-formedness constraint only if standalone='yes'. 
           [ WFC: Parsed Entity ] An entity reference must not
           contain the name of an unparsed entity """
        ret = libxml2mod.xmlParseEntityRef(self._o)
        if ret is None:raise parserError('xmlParseEntityRef() failed')
        __tmp = xmlEntity(_obj=ret)
        return __tmp

    def parseExternalSubset(self, ExternalID, SystemID):
        """parse Markup declarations from an external subset  [30]
           extSubset ::= textDecl? extSubsetDecl  [31] extSubsetDecl
           ::= (markupdecl | conditionalSect | PEReference | S) * """
        libxml2mod.xmlParseExternalSubset(self._o, ExternalID, SystemID)

    def parseMarkupDecl(self):
        """parse Markup declarations  [29] markupdecl ::= elementdecl
           | AttlistDecl | EntityDecl | NotationDecl | PI | Comment 
           [ VC: Proper Declaration/PE Nesting ] Parameter-entity
           replacement text must be properly nested with markup
           declarations. That is to say, if either the first
           character or the last character of a markup declaration
           (markupdecl above) is contained in the replacement text
           for a parameter-entity reference, both must be contained
           in the same replacement text.  [ WFC: PEs in Internal
           Subset ] In the internal DTD subset, parameter-entity
           references can occur only where markup declarations can
           occur, not within markup declarations. (This does not
           apply to references that occur in external parameter
           entities or to the external subset.) """
        libxml2mod.xmlParseMarkupDecl(self._o)

    def parseMisc(self):
        """parse an XML Misc* optional field.  [27] Misc ::= Comment |
           PI |  S """
        libxml2mod.xmlParseMisc(self._o)

    def parseName(self):
        """parse an XML name.  [4] NameChar ::= Letter | Digit | '.' |
           '-' | '_' | ':' | CombiningChar | Extender  [5] Name ::=
           (Letter | '_' | ':') (NameChar)*  [6] Names ::= Name (S
           Name)* """
        ret = libxml2mod.xmlParseName(self._o)
        return ret

    def parseNamespace(self):
        """xmlParseNamespace: parse specific PI '<?namespace ...'
           constructs.  This is what the older xml-name Working Draft
           specified, a bunch of other stuff may still rely on it, so
           support is still here as if it was declared on the root of
           the Tree:-(  TODO: remove from library  To be removed at
           next drop of binary compatibility """
        libxml2mod.xmlParseNamespace(self._o)

    def parseNmtoken(self):
        """parse an XML Nmtoken.  [7] Nmtoken ::= (NameChar)+  [8]
           Nmtokens ::= Nmtoken (S Nmtoken)* """
        ret = libxml2mod.xmlParseNmtoken(self._o)
        return ret

    def parseNotationDecl(self):
        """parse a notation declaration  [82] NotationDecl ::=
           '<!NOTATION' S Name S (ExternalID |  PublicID) S? '>' 
           Hence there is actually 3 choices: 'PUBLIC' S PubidLiteral
           'PUBLIC' S PubidLiteral S SystemLiteral and 'SYSTEM' S
           SystemLiteral  See the NOTE on xmlParseExternalID(). """
        libxml2mod.xmlParseNotationDecl(self._o)

    def parsePEReference(self):
        """parse PEReference declarations The entity content is
           handled directly by pushing it's content as a new input
           stream.  [69] PEReference ::= '%' Name ';'  [ WFC: No
           Recursion ] A parsed entity must not contain a recursive
           reference to itself, either directly or indirectly.  [
           WFC: Entity Declared ] In a document without any DTD, a
           document with only an internal DTD subset which contains
           no parameter entity references, or a document with
           "standalone='yes'", ...  ... The declaration of a
           parameter entity must precede any reference to it...  [
           VC: Entity Declared ] In a document with an external
           subset or external parameter entities with
           "standalone='no'", ...  ... The declaration of a parameter
           entity must precede any reference to it...  [ WFC: In DTD
           ] Parameter-entity references may only appear in the DTD.
           NOTE: misleading but this is handled. """
        libxml2mod.xmlParsePEReference(self._o)

    def parsePI(self):
        """parse an XML Processing Instruction.  [16] PI ::= '<?'
           PITarget (S (Char* - (Char* '?>' Char*)))? '?>'  The
           processing is transfered to SAX once parsed. """
        libxml2mod.xmlParsePI(self._o)

    def parsePITarget(self):
        """parse the name of a PI  [17] PITarget ::= Name - (('X' |
           'x') ('M' | 'm') ('L' | 'l')) """
        ret = libxml2mod.xmlParsePITarget(self._o)
        return ret

    def parsePubidLiteral(self):
        """parse an XML public literal  [12] PubidLiteral ::= '"'
           PubidChar* '"' | "'" (PubidChar - "'")* "'" """
        ret = libxml2mod.xmlParsePubidLiteral(self._o)
        return ret

    def parseQuotedString(self):
        """Parse and return a string between quotes or doublequotes 
           TODO: Deprecated, to  be removed at next drop of binary
           compatibility """
        ret = libxml2mod.xmlParseQuotedString(self._o)
        return ret

    def parseReference(self):
        """parse and handle entity references in content, depending on
           the SAX interface, this may end-up in a call to
           character() if this is a CharRef, a predefined entity, if
           there is no reference() callback. or if the parser was
           asked to switch to that mode.  [67] Reference ::=
           EntityRef | CharRef """
        libxml2mod.xmlParseReference(self._o)

    def parseSDDecl(self):
        """parse the XML standalone declaration  [32] SDDecl ::= S
           'standalone' Eq (("'" ('yes' | 'no') "'") | ('"' ('yes' |
           'no')'"'))  [ VC: Standalone Document Declaration ] TODO
           The standalone document declaration must have the value
           "no" if any external markup declarations contain
           declarations of: - attributes with default values, if
           elements to which these attributes apply appear in the
           document without specifications of values for these
           attributes, or - entities (other than amp, lt, gt, apos,
           quot), if references to those entities appear in the
           document, or - attributes with values subject to
           normalization, where the attribute appears in the document
           with a value which will change as a result of
           normalization, or - element types with element content, if
           white space occurs directly within any instance of those
           types. """
        ret = libxml2mod.xmlParseSDDecl(self._o)
        return ret

    def parseStartTag(self):
        """parse a start of tag either for rule element or
           EmptyElement. In both case we don't parse the tag closing
           chars.  [40] STag ::= '<' Name (S Attribute)* S? '>'  [
           WFC: Unique Att Spec ] No attribute name may appear more
           than once in the same start-tag or empty-element tag. 
           [44] EmptyElemTag ::= '<' Name (S Attribute)* S? '/>'  [
           WFC: Unique Att Spec ] No attribute name may appear more
           than once in the same start-tag or empty-element tag. 
           With namespace:  [NS 8] STag ::= '<' QName (S Attribute)*
           S? '>'  [NS 10] EmptyElement ::= '<' QName (S Attribute)*
           S? '/>' """
        ret = libxml2mod.xmlParseStartTag(self._o)
        return ret

    def parseSystemLiteral(self):
        """parse an XML Literal  [11] SystemLiteral ::= ('"' [^"]*
           '"') | ("'" [^']* "'") """
        ret = libxml2mod.xmlParseSystemLiteral(self._o)
        return ret

    def parseTextDecl(self):
        """parse an XML declaration header for external entities  [77]
           TextDecl ::= '<?xml' VersionInfo? EncodingDecl S? '?>' 
           Question: Seems that EncodingDecl is mandatory ? Is that a
           typo ? """
        libxml2mod.xmlParseTextDecl(self._o)

    def parseVersionInfo(self):
        """parse the XML version.  [24] VersionInfo ::= S 'version' Eq
           (' VersionNum ' | " VersionNum ")  [25] Eq ::= S? '=' S? """
        ret = libxml2mod.xmlParseVersionInfo(self._o)
        return ret

    def parseVersionNum(self):
        """parse the XML version value.  [26] VersionNum ::=
           ([a-zA-Z0-9_.:] | '-')+ """
        ret = libxml2mod.xmlParseVersionNum(self._o)
        return ret

    def parseXMLDecl(self):
        """parse an XML declaration header  [23] XMLDecl ::= '<?xml'
           VersionInfo EncodingDecl? SDDecl? S? '?>' """
        libxml2mod.xmlParseXMLDecl(self._o)

    def parserHandlePEReference(self):
        """[69] PEReference ::= '%' Name ';'  [ WFC: No Recursion ] A
           parsed entity must not contain a recursive reference to
           itself, either directly or indirectly.  [ WFC: Entity
           Declared ] In a document without any DTD, a document with
           only an internal DTD subset which contains no parameter
           entity references, or a document with "standalone='yes'",
           ...  ... The declaration of a parameter entity must
           precede any reference to it...  [ VC: Entity Declared ] In
           a document with an external subset or external parameter
           entities with "standalone='no'", ...  ... The declaration
           of a parameter entity must precede any reference to it... 
           [ WFC: In DTD ] Parameter-entity references may only
           appear in the DTD. NOTE: misleading but this is handled. 
           A PEReference may have been detected in the current input
           stream the handling is done accordingly to
           http://www.w3.org/TR/REC-xml#entproc i.e. - Included in
           literal in entity values - Included as Parameter Entity
           reference within DTDs """
        libxml2mod.xmlParserHandlePEReference(self._o)

    def parserHandleReference(self):
        """TODO: Remove, now deprecated ... the test is done directly
           in the content parsing routines.  [67] Reference ::=
           EntityRef | CharRef  [68] EntityRef ::= '&' Name ';'  [
           WFC: Entity Declared ] the Name given in the entity
           reference must match that in an entity declaration, except
           that well-formed documents need not declare any of the
           following entities: amp, lt, gt, apos, quot.  [ WFC:
           Parsed Entity ] An entity reference must not contain the
           name of an unparsed entity  [66] CharRef ::= '&#' [0-9]+
           ';' | '&#x' [0-9a-fA-F]+ ';'  A PEReference may have been
           detected in the current input stream the handling is done
           accordingly to http://www.w3.org/TR/REC-xml#entproc """
        libxml2mod.xmlParserHandleReference(self._o)

    def popInput(self):
        """xmlPopInput: the current input pointed by ctxt->input came
           to an end pop it and return the next char. """
        ret = libxml2mod.xmlPopInput(self._o)
        return ret

    def scanName(self):
        """Trickery: parse an XML name but without consuming the input
           flow Needed for rollback cases. Used only when parsing
           entities references.  TODO: seems deprecated now, only
           used in the default part of xmlParserHandleReference  [4]
           NameChar ::= Letter | Digit | '.' | '-' | '_' | ':' |
           CombiningChar | Extender  [5] Name ::= (Letter | '_' |
           ':') (NameChar)*  [6] Names ::= Name (S Name)* """
        ret = libxml2mod.xmlScanName(self._o)
        return ret

    def skipBlankChars(self):
        """skip all blanks character found at that point in the input
           streams. It pops up finished entities in the process if
           allowable at that point. """
        ret = libxml2mod.xmlSkipBlankChars(self._o)
        return ret

    def stringDecodeEntities(self, str, what, end, end2, end3):
        """Takes a entity string content and process to do the
           adequate substitutions.  [67] Reference ::= EntityRef |
           CharRef  [69] PEReference ::= '%' Name ';' """
        ret = libxml2mod.xmlStringDecodeEntities(self._o, str, what, end, end2, end3)
        return ret

class xmlDtd(xmlNode):
    def __init__(self, _obj=None):
        self._o = None
        xmlNode.__init__(self, _obj=_obj)

    def __repr__(self):
        return "<xmlDtd (%s) object at 0x%x>" % (self.name, id (self))

    #
    # xmlDtd functions from module debugXML
    #

    def debugDumpDTD(self, output):
        """Dumps debug information for the DTD """
        libxml2mod.xmlDebugDumpDTD(output, self._o)

    #
    # xmlDtd functions from module tree
    #

    def copyDtd(self):
        """Do a copy of the dtd. """
        ret = libxml2mod.xmlCopyDtd(self._o)
        if ret is None:raise treeError('xmlCopyDtd() failed')
        __tmp = xmlDtd(_obj=ret)
        return __tmp

    def freeDtd(self):
        """Free a DTD structure. """
        libxml2mod.xmlFreeDtd(self._o)

    #
    # xmlDtd functions from module valid
    #

    def dtdAttrDesc(self, elem, name):
        """Search the DTD for the description of this attribute on
           this element. """
        ret = libxml2mod.xmlGetDtdAttrDesc(self._o, elem, name)
        if ret is None:raise treeError('xmlGetDtdAttrDesc() failed')
        __tmp = xmlAttribute(_obj=ret)
        return __tmp

    def dtdElementDesc(self, name):
        """Search the DTD for the description of this element """
        ret = libxml2mod.xmlGetDtdElementDesc(self._o, name)
        if ret is None:raise treeError('xmlGetDtdElementDesc() failed')
        __tmp = xmlElement(_obj=ret)
        return __tmp

    def dtdQAttrDesc(self, elem, name, prefix):
        """Search the DTD for the description of this qualified
           attribute on this element. """
        ret = libxml2mod.xmlGetDtdQAttrDesc(self._o, elem, name, prefix)
        if ret is None:raise treeError('xmlGetDtdQAttrDesc() failed')
        __tmp = xmlAttribute(_obj=ret)
        return __tmp

    def dtdQElementDesc(self, name, prefix):
        """Search the DTD for the description of this element """
        ret = libxml2mod.xmlGetDtdQElementDesc(self._o, name, prefix)
        if ret is None:raise treeError('xmlGetDtdQElementDesc() failed')
        __tmp = xmlElement(_obj=ret)
        return __tmp

class xmlNs(xmlNode):
    def __init__(self, _obj=None):
        self._o = None
        xmlNode.__init__(self, _obj=_obj)

    def __repr__(self):
        return "<xmlNs (%s) object at 0x%x>" % (self.name, id (self))

    #
    # xmlNs functions from module tree
    #

    def copyNamespace(self):
        """Do a copy of the namespace. """
        ret = libxml2mod.xmlCopyNamespace(self._o)
        if ret is None:raise treeError('xmlCopyNamespace() failed')
        __tmp = xmlNs(_obj=ret)
        return __tmp

    def copyNamespaceList(self):
        """Do a copy of an namespace list. """
        ret = libxml2mod.xmlCopyNamespaceList(self._o)
        if ret is None:raise treeError('xmlCopyNamespaceList() failed')
        __tmp = xmlNs(_obj=ret)
        return __tmp

    def freeNs(self):
        """Free up the structures associated to a namespace """
        libxml2mod.xmlFreeNs(self._o)

    def freeNsList(self):
        """Free up all the structures associated to the chained
           namespaces. """
        libxml2mod.xmlFreeNsList(self._o)

    def newNodeEatName(self, name):
        """Creation of a new node element. @ns is optional (None). """
        ret = libxml2mod.xmlNewNodeEatName(self._o, name)
        if ret is None:raise treeError('xmlNewNodeEatName() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp

    #
    # xmlNs functions from module xpathInternals
    #

    def xpathNodeSetFreeNs(self):
        """Namespace node in libxml don't match the XPath semantic. In
           a node set the namespace nodes are duplicated and the next
           pointer is set to the parent node in the XPath semantic.
           Check if such a node need to be freed """
        libxml2mod.xmlXPathNodeSetFreeNs(self._o)

class inputBuffer(ioReadWrapper):
    def __init__(self, _obj=None):
        self._o = None
        ioReadWrapper.__init__(self, _obj=_obj)

    def __del__(self):
        if self._o != None:
            libxml2mod.xmlFreeParserInputBuffer(self._o)
        self._o = None

    #
    # inputBuffer functions from module xmlIO
    #

    def freeParserInputBuffer(self):
        """Free up the memory used by a buffered parser input """
        libxml2mod.xmlFreeParserInputBuffer(self._o)

    def grow(self, len):
        """Grow up the content of the input buffer, the old data are
           preserved This routine handle the I18N transcoding to
           internal UTF-8 This routine is used when operating the
           parser in normal (pull) mode  TODO: one should be able to
           remove one extra copy by copying directly onto in->buffer
           or in->raw """
        ret = libxml2mod.xmlParserInputBufferGrow(self._o, len)
        return ret

    def push(self, len, buf):
        """Push the content of the arry in the input buffer This
           routine handle the I18N transcoding to internal UTF-8 This
           is used when operating the parser in progressive (push)
           mode. """
        ret = libxml2mod.xmlParserInputBufferPush(self._o, len, buf)
        return ret

    def read(self, len):
        """Refresh the content of the input buffer, the old data are
           considered consumed This routine handle the I18N
           transcoding to internal UTF-8 """
        ret = libxml2mod.xmlParserInputBufferRead(self._o, len)
        return ret

    #
    # inputBuffer functions from module xmlreader
    #

    def newTextReader(self, URI):
        """Create an xmlTextReader structure fed with @input """
        ret = libxml2mod.xmlNewTextReader(self._o, URI)
        if ret is None:raise treeError('xmlNewTextReader() failed')
        __tmp = xmlTextReader(_obj=ret)
        __tmp.input = self
        return __tmp

class relaxNgParserCtxt:
    def __init__(self, _obj=None):
        if _obj != None:self._o = _obj;return
        self._o = None

    def __del__(self):
        if self._o != None:
            libxml2mod.xmlRelaxNGFreeParserCtxt(self._o)
        self._o = None

    #
    # relaxNgParserCtxt functions from module relaxng
    #

    def relaxNGFreeParserCtxt(self):
        """Free the resources associated to the schema parser context """
        libxml2mod.xmlRelaxNGFreeParserCtxt(self._o)

    def relaxNGParse(self):
        """parse a schema definition resource and build an internal
           XML Shema struture which can be used to validate
           instances. *WARNING* this interface is highly subject to
           change """
        ret = libxml2mod.xmlRelaxNGParse(self._o)
        if ret is None:raise parserError('xmlRelaxNGParse() failed')
        __tmp = relaxNgSchema(_obj=ret)
        return __tmp

class outputBuffer(ioWriteWrapper):
    def __init__(self, _obj=None):
        self._o = None
        ioWriteWrapper.__init__(self, _obj=_obj)

    #
    # outputBuffer functions from module xmlIO
    #

    def close(self):
        """flushes and close the output I/O channel and free up all
           the associated resources """
        ret = libxml2mod.xmlOutputBufferClose(self._o)
        return ret

    def flush(self):
        """flushes the output I/O channel """
        ret = libxml2mod.xmlOutputBufferFlush(self._o)
        return ret

    def write(self, len, buf):
        """Write the content of the array in the output I/O buffer
           This routine handle the I18N transcoding from internal
           UTF-8 The buffer is lossless, i.e. will store in case of
           partial or delayed writes. """
        ret = libxml2mod.xmlOutputBufferWrite(self._o, len, buf)
        return ret

    def writeString(self, str):
        """Write the content of the string in the output I/O buffer
           This routine handle the I18N transcoding from internal
           UTF-8 The buffer is lossless, i.e. will store in case of
           partial or delayed writes. """
        ret = libxml2mod.xmlOutputBufferWriteString(self._o, str)
        return ret

class xmlTextReaderLocator:
    def __init__(self, _obj=None):
        if _obj != None:self._o = _obj;return
        self._o = None

    #
    # xmlTextReaderLocator functions from module xmlreader
    #

    def BaseURI(self):
        """Obtain the base URI for the given locator. """
        ret = libxml2mod.xmlTextReaderLocatorBaseURI(self._o)
        return ret

    def LineNumber(self):
        """Obtain the line number for the given locator. """
        ret = libxml2mod.xmlTextReaderLocatorLineNumber(self._o)
        return ret

class URI:
    def __init__(self, _obj=None):
        if _obj != None:self._o = _obj;return
        self._o = None

    def __del__(self):
        if self._o != None:
            libxml2mod.xmlFreeURI(self._o)
        self._o = None

    # accessors for URI
    def authority(self):
        """Get the authority part from an URI """
        ret = libxml2mod.xmlURIGetAuthority(self._o)
        return ret

    def fragment(self):
        """Get the fragment part from an URI """
        ret = libxml2mod.xmlURIGetFragment(self._o)
        return ret

    def opaque(self):
        """Get the opaque part from an URI """
        ret = libxml2mod.xmlURIGetOpaque(self._o)
        return ret

    def path(self):
        """Get the path part from an URI """
        ret = libxml2mod.xmlURIGetPath(self._o)
        return ret

    def port(self):
        """Get the port part from an URI """
        ret = libxml2mod.xmlURIGetPort(self._o)
        return ret

    def query(self):
        """Get the query part from an URI """
        ret = libxml2mod.xmlURIGetQuery(self._o)
        return ret

    def scheme(self):
        """Get the scheme part from an URI """
        ret = libxml2mod.xmlURIGetScheme(self._o)
        return ret

    def server(self):
        """Get the server part from an URI """
        ret = libxml2mod.xmlURIGetServer(self._o)
        return ret

    def setAuthority(self, authority):
        """Set the authority part of an URI. """
        libxml2mod.xmlURISetAuthority(self._o, authority)

    def setFragment(self, fragment):
        """Set the fragment part of an URI. """
        libxml2mod.xmlURISetFragment(self._o, fragment)

    def setOpaque(self, opaque):
        """Set the opaque part of an URI. """
        libxml2mod.xmlURISetOpaque(self._o, opaque)

    def setPath(self, path):
        """Set the path part of an URI. """
        libxml2mod.xmlURISetPath(self._o, path)

    def setPort(self, port):
        """Set the port part of an URI. """
        libxml2mod.xmlURISetPort(self._o, port)

    def setQuery(self, query):
        """Set the query part of an URI. """
        libxml2mod.xmlURISetQuery(self._o, query)

    def setScheme(self, scheme):
        """Set the scheme part of an URI. """
        libxml2mod.xmlURISetScheme(self._o, scheme)

    def setServer(self, server):
        """Set the server part of an URI. """
        libxml2mod.xmlURISetServer(self._o, server)

    def setUser(self, user):
        """Set the user part of an URI. """
        libxml2mod.xmlURISetUser(self._o, user)

    def user(self):
        """Get the user part from an URI """
        ret = libxml2mod.xmlURIGetUser(self._o)
        return ret

    #
    # URI functions from module uri
    #

    def freeURI(self):
        """Free up the xmlURI struct """
        libxml2mod.xmlFreeURI(self._o)

    def parseURIReference(self, str):
        """Parse an URI reference string and fills in the appropriate
           fields of the @uri structure  URI-reference = [
           absoluteURI | relativeURI ] [ "#" fragment ] """
        ret = libxml2mod.xmlParseURIReference(self._o, str)
        return ret

    def printURI(self, stream):
        """Prints the URI in the stream @steam. """
        libxml2mod.xmlPrintURI(stream, self._o)

    def saveUri(self):
        """Save the URI as an escaped string """
        ret = libxml2mod.xmlSaveUri(self._o)
        return ret

