
/*
 * This is an input file for the "Ragel" finite state machine compiler utility.
 * It produces output code which implements a tag scanner for XML data.
 * It is used for intelligent xml tag completion in an XML editor interface.
 * 
 * See the Ragel online documentation for additional
 * information about the format of this file.
 *
 * Written by Marc Liyanage <http://www.entropy.ch>
 *
 */
 
 
#include <CoreFoundation/CoreFoundation.h>
#include "ragel_xmldeclscanner.h"


%% XMLDeclScanner
	struct {
		char *mark_encodingstart;
		char *mark_encodingend;
	};

%%

%% XMLDeclScanner

	init {
		fsm->mark_encodingstart = fsm->mark_encodingend = NULL;
	}


	func encodingstart {
		DEBUG && fprintf(stderr, "encodingstart: %d %c\n", p - data, *p);
		fsm->mark_encodingstart = p;
	}
	
	func encodingend {
		fsm->mark_encodingend = p;
		DEBUG && fprintf(stderr, "encodingend: %d %c\n", p - data, *p);
		DEBUG && fprintf(stderr, "length: %d\n", fsm->mark_encodingend - fsm->mark_encodingstart);
	}



	BOM = 0xef 0xbb 0xbf;

#	Grammar taken straight from the XML 1.0 spec, except that EncodingDecl is not optional here

	Eq = '=';

	VersionNum = +(/[a-zA-Z0-9_.:]/ | '-');
	VersionInfo = space 'version' Eq ("'" VersionNum "'" | '"' VersionNum '"');

	EncName = (/[A-Za-z]/ *(/[A-Za-z0-9._]/ | '-')) >encodingstart %encodingend;
	EncodingDecl = space 'encoding' Eq ('"' EncName '"' | "'" EncName "'" );

	SDDecl = space 'standalone' Eq (("'" ('yes' | 'no') "'") | ('"' ('yes' | 'no') '"'));
	
	XMLDecl = '<?xml' VersionInfo EncodingDecl ?SDDecl ?space '?>';


	main = ?BOM XMLDecl /.*/;

%%




unsigned int getEncodingFromXmlDecl(char *data, int len) {

	int encodinglength, result;
	CFStringRef encodingString;
	
	XMLDeclScanner scanner, *machine = &scanner;

	XMLDeclScannerInit(machine);
	XMLDeclScannerExecute(machine, data, len > 512 ? 512 : len);
	XMLDeclScannerFinish(machine);

	if (!XMLDeclScannerAccept(machine)) {
		return 0;
	}

	encodinglength = machine->mark_encodingend - machine->mark_encodingstart;


	encodingString = CFStringCreateWithBytes (
		NULL,
		machine->mark_encodingstart,
		(CFIndex)encodinglength,
		kCFStringEncodingASCII,
		0
	);

	result = CFStringConvertIANACharSetNameToEncoding(encodingString);
	CFRelease(encodingString);

	if (result == kCFStringEncodingInvalidId)
		return 0;
		
	result = CFStringConvertEncodingToNSStringEncoding(result);
	
	if (result == kCFStringEncodingInvalidId)
		return 0;

	return result;
	
}


unsigned int getIANACharSetName(char *data, int len, char *destbuffer, int destbufferlen) {
	
	int encodinglength, result;
	CFStringRef encodingString;
	
	XMLDeclScanner scanner, *machine = &scanner;
	
	XMLDeclScannerInit(machine);
	XMLDeclScannerExecute(machine, data, len > 512 ? 512 : len);
	XMLDeclScannerFinish(machine);
	
	if (!XMLDeclScannerAccept(machine)) {
		return 0;
	}
	
	encodinglength = machine->mark_encodingend - machine->mark_encodingstart;
	
	bzero(dstbuffer, dstbufferlen);
	strncpy(dstbuffer, machine->mark_encodingstart, dstbufferlen-1 > encodinglength ? dstbufferlen-1 : encodinglength);
	
	
	encodingString = CFStringCreateWithBytes (
										   NULL,
										   machine->mark_encodingstart,
										   (CFIndex)encodinglength,
										   kCFStringEncodingASCII,
										   0
										   );
	
	result = CFStringConvertIANACharSetNameToEncoding(encodingString);
	CFRelease(encodingString);
	
	if (result == kCFStringEncodingInvalidId)
		return 0;
	
	result = CFStringConvertEncodingToNSStringEncoding(result);
	
	if (result == kCFStringEncodingInvalidId)
		return 0;
	
	return result;
	
}



/*	No longer used, now using CoreFoundation 

	struct encodingPair {
		int encoding;
		char *matchstring;
	};

	struct encodingPair encodingPairs[] = {
		{NSUTF8StringEncoding, "UTF-8"},
		{NSISOLatin1StringEncoding, "ISO-8859-1"},
		{0, NULL},
	};



	for (i = 0; encodingPairs[i].matchstring; i++) {

		testlength = strlen(encodingPairs[i].matchstring);
		if (!strncasecmp(machine->mark_encodingstart, encodingPairs[i].matchstring, encodinglength < testlength ? encodinglength : testlength)) {
			return encodingPairs[i].encoding;
		}
		
	}

	return 0;

*/
	
