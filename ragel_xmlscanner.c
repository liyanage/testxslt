
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
 
 
#include "ragel_xmlscanner.h"


/* modes for the scan, before or after cursor position */
enum {
	BEFORE = 1,
	AFTER
};


%% XMLScanner
	struct {
		char *data;
		char *stack[STACKDEPTH];
		char *stack_e[STACKDEPTH];
		int sp;
		int sp_e;
		char *mark_namestart;
		char *mark_nameend;
		char *mark_attrstart;
		char *mark_attrend;
		char *before_toptag;
		int cursor;
		int in_comment;
		int in_cdata;
		int in_tag;
		int mode;
	};
%%



void checkETag(XMLScanner *fsm);
void popTag(XMLScanner *fsm);
void pushTag(XMLScanner *fsm);

%% XMLScanner

	init {
		fsm->sp = 0;
		fsm->sp_e = 0;
		fsm->mode = BEFORE;
		fsm->in_comment = 0;
		fsm->in_cdata = 0;
		fsm->in_tag = 0;
	}


	func commentstart {
		DEBUG && fprintf(stderr, "commentstart: %d %c\n", p - data, *p);
		fsm->in_comment = 1;
	}

	func commentend {
		DEBUG && fprintf(stderr, "commentend: %d %c\n", p - data, *p);
		fsm->in_comment = 0;
		fsm->in_tag = 0;
	}

	func cdatastart {
		fsm->in_cdata = 1;
	}

	func cdataend {
		fsm->in_cdata = 0;
		fsm->in_tag = 0;
	}

	func enter_tag {
		DEBUG && fprintf(stderr, "enter tag at %d\n", p - data);
		fsm->in_tag = 1;
	}

	func exit_tag {
		DEBUG && fprintf(stderr, "exit tag at %d\n", p - data);
		fsm->in_tag = 0;
	}

	func name {
//		fprintf(stderr, "name: %d %c\n", p - data, *p);
	}

	func stag {
		DEBUG && fprintf(stderr, "stag\n");
		pushTag(fsm);
	}

	func etag {
		DEBUG && fprintf(stderr, "stag: start: %d end: %d %c\n", fsm->mark_namestart - data, fsm->mark_nameend - data, *p);
		checkETag(fsm);
	}

	func mark_namestart {
		DEBUG && fprintf(stderr, "markstart: %d %c\n", p - data, *p);
		fsm->mark_namestart = p;
	}

	func mark_nameend {
		DEBUG && fprintf(stderr, "markend: %d %c\n", (p - 1) - data, *(p-1));
		fsm->mark_nameend = p;
	}

	func mark_attrstart {
//		fprintf(stderr, "attrstart: %d %c\n", p - data, *p);
		fsm->mark_attrstart = p;
	}

	func mark_attrend {
//		fprintf(stderr, "attrend: %d %c\n", (p - 1) - data, *(p - 1));
		fsm->mark_attrend = p;
	}


func attr {
	//		fprintf(stderr, "attr: start: %d end: %d %c\n", fsm->mark_attrstart - data, fsm->mark_attrend - data, *p);
}

func pi {
	DEBUG && fprintf(stderr, "pi: %d\n", p - data);
}



#	// This is the actual grammar used by the scanner. It calls into the 
#	// functions above at certain state transitions.
	
	lt = '<' %enter_tag;
	gt = '>' %exit_tag;

	namechar = alpha | digit | '.' | '-' | '_' | ':';
	nmtoken = +namechar;
	name = (alpha | '_' | ':') *namechar;

	attr = name >mark_attrstart '=' ((/'[^']*'/ | /"[^"]*"/) %mark_attrend) %attr;
	stag = (lt (name >mark_namestart %mark_nameend) *(space | attr) gt) %stag;
	etag = lt '/' (name >mark_namestart %mark_nameend) gt %etag;
	emptytag = lt name *(space | attr) '/' gt;
	
	commentstart = '<!--' %commentstart;
	commentend = '-->' %commentend;
	comment = commentstart ((!commentend commentend) | commentend);

	cdatastart = '<![CDATA[[' %cdatastart;
	cdataend = ']]>' %cdataend;
	cdata = cdatastart ((!cdataend cdataend) | cdataend);
	
	nonlt = /[^<]/;
	
	main = *(comment %+1 | cdata %+1 | lt | stag | emptytag | etag | nonlt %-1);

%%


/* 
 * findCompletion does the actual work of driving the state machine
 *
 * Input:
 *  data   - pointer to the buffer containing the XML data
 *  len    - length of the data to analyze
 *  cursor - logical position of the editing cursor in the data buffer
 *  result - pointer to integer, which will contain a bit field with
 *           additional status information after completion:
 *           
 * Completion rules:
 *
 * - The system builds a stack of tags which are open at the indicated cursor
 *   position in the XML data.
 * - If completion is possible at that cursor position, the integer
 *   result will be 0. The caller should insert a closing tag for the
 *   topmost tag name on the stack.
 * - It can use the other elements of the
 *   stack for GUI goodies, like display of a stack of currently open tags
 *   in the editor. However, it should not assume that the tag stack can be
 *   used to close all opening tags. Instead, it should re-evaluate
 *   the document with this routine after the tag has been inserted and the
 *   cursor position might have moved as a result.
 * 
 * - There are a few cases where completion should not be performed, this
 *   will be indicated by the bitfield in the result int parameter:
 *   - ERROR_IN_TAG: The cursor is in the middle of a tag. No useful completion
 *                   is possible (maybe look at the prefix and complete
 *                   accordingly, sometime in the future...)
 *   - ERROR_IN_COMMENT: The cursor is inside a comment block.
 *   - ERROR_IN_CDATA: The cursor is inside a cdata section.
 *   - ERROR_NO_TAG: There's no unmatched opening tag to the left of the cursor
 *   - ERROR_ALREADY_BALANCED_HERE: The currently open tags to the left of the
 *                                  cursor are already balanced with an equal amount
 *                                  of closing tags to the right of the cursor.
 *
 * Results:
 * 
 * Returns a pointer to an array of pointers to chars.
 * Each array entry contains one tag from the stack
 * tags open at the cursor position.
 *
 */
char (*findCompletion(char *data, int len, int cursor, int *result, int tagpositions[STACKDEPTH]))[] {

	XMLScanner scanner, *machine = &scanner;
	char toptag[MAXTAGLENGTH];
	unsigned int i, lower, upper, openingcount, closingcount, identical_opening, identical_closing;

	char (*resultstack)[MAXTAGLENGTH] = NULL;
	char (*resultstack_e)[MAXTAGLENGTH] = NULL;
	
	*result = 0;

	bzero(toptag, MAXTAGLENGTH);


	// ------------ analyze data before cursor position ------------------

	XMLScannerInit(machine);

	machine->mode = BEFORE;
	machine->cursor = cursor;
	
	XMLScannerExecute(machine, data, cursor);
	XMLScannerFinish(machine);


	/* Any unbalanced open tags on the stack at all? If so, allocate memory
	 * and copy the tags over to a newly allocated buffer, into a stack.
	 */
	if (machine->sp) {
		resultstack = malloc(MAXTAGLENGTH * ((machine->sp/2) + 1));
	} else {
		/* Nothing useful to return to caller */
		*result |= ERROR_NO_TAG;
		return NULL;
	}
	
	openingcount = (machine->sp / 2);
	
	for (i = 0; i < openingcount; i++) {
		lower = i * 2;
		upper = lower + 1;
		bzero(resultstack[i], MAXTAGLENGTH);
		strncpy(resultstack[i], machine->stack[lower], machine->stack[upper] - machine->stack[lower]);
		if (tagpositions) {
			tagpositions[lower] = machine->stack[lower] - data;
			tagpositions[upper] = machine->stack[upper] - data;
		}
	}
	
	/* make sure the slot after the topmost tag is zeroed out, so the
	 * calling code can use that as an end of stack marker.
	 */
	bzero(resultstack[openingcount], MAXTAGLENGTH);

	strncpy(toptag, resultstack[openingcount - 1], MAXTAGLENGTH);
	
	if (machine->in_tag)
		*result |= ERROR_IN_TAG;
	if (machine->in_comment)
		*result |= ERROR_IN_COMMENT;
	if (machine->in_cdata)
		*result |= ERROR_IN_CDATA;

	if (*result) {
		return resultstack;
	}

	// count identical opening tags on the top of the stack.
	identical_opening = 1;
	for (i = (openingcount - 2); i >= 0; i--) {
		if (!strcmp(resultstack[i], resultstack[i + 1])) {
			identical_opening++;
		} else {
			break;
		}
	}


	// ------------ analyze data after cursor position ------------------
	
//	fprintf(stderr, "accept: %d\n", XMLScannerAccept(machine)); 


	/* Reinitialize and reconfigure the scanner, and run it again, but this time with
	 * the data from the cursor position until the end.
	 */
	XMLScannerInit(machine);
	machine->mode = AFTER;
	machine->cursor = cursor;
	XMLScannerExecute(machine, data + cursor, len - cursor);
	XMLScannerFinish(machine);

	/* If there are no closing tags, we don't need to check if
	 * the topmost opening tags on the stacks are already balanced
	 */
	closingcount = (machine->sp_e / 2);
	if (!closingcount) {
		return resultstack;
	}

	resultstack_e = malloc(MAXTAGLENGTH * ((machine->sp_e/2) + 1));

	for (i = 0; i < closingcount; i++) {
		lower = i * 2;
		upper = lower + 1;
		
		bzero(resultstack_e[i], MAXTAGLENGTH);
		strncpy(resultstack_e[i], machine->stack_e[lower], machine->stack_e[upper] - machine->stack_e[lower]);

	}
	
	DEBUG && fprintf(stderr, "closing count %d\n", closingcount);

	identical_closing = closingcount ? 1 : 0;
	for (i = 0; i < closingcount - 1; i++) {
		if (!strcmp(resultstack_e[i], resultstack_e[i + 1])) {
			identical_closing++;
		} else {
			break;
		}
	}

	DEBUG && fprintf(stderr, "identical_closing %d\n", identical_closing);

	/* last opening tag before cursor and first closing tag after
	 * cursor have to be identical, otherwise we are not interested
	 * if they are balanced
	 */
	if (strcmp(resultstack[openingcount - 1], resultstack_e[0])) {
		free(resultstack_e);
		return resultstack;
	}
	
	/* ok, the adjacent opening and closing tags are identical, so we
	 * need to know if there are less closing tags than opening tags,
	 * because only then does tag completion make any sense at this location
	 */
	
	if (identical_opening <= identical_closing) {
		*result |= ERROR_ALREADY_BALANCED_HERE;
	}
	
	free(resultstack_e);
	
	// caller needs to free() this...
	return resultstack;

}





/*
 * Push the current start and end buffer position markers onto our 
 * stack of currently open tags. We're operating with position numbers
 * only at this point, later there will be actual copies out of the buffer
 */
void pushTag(XMLScanner *fsm) {

	char buffer[MAXTAGLENGTH];
	bzero(buffer, sizeof(buffer));

	if (fsm->sp + 2 >= (STACKDEPTH - 1)) {
		fprintf(stderr, "pushTag: stack overflow at %d, can't push more!\n", STACKDEPTH);
		return;
	}

	fsm->stack[fsm->sp++] = fsm->mark_namestart;
	fsm->stack[fsm->sp++] = fsm->mark_nameend;
	
	DEBUG && strncpy(buffer, fsm->stack[fsm->sp - 2], fsm->stack[fsm->sp - 1] - fsm->stack[fsm->sp - 2]);
	DEBUG && fprintf(stderr, "pushTag: pushing '%s'\n", buffer);

}



/*
 * Push the current start and end buffer position markers for
 * *end* tags onto the stack.
 */
void pushETag(XMLScanner *fsm) {

	char buffer[MAXTAGLENGTH];
	bzero(buffer, sizeof(buffer));

	if (fsm->sp_e + 2 >= (STACKDEPTH - 1)) {
		fprintf(stderr, "pushETag: stack overflow at %d, can't push more!\n", STACKDEPTH);
		return;
	}
	
	fsm->stack_e[fsm->sp_e++] = fsm->mark_namestart;
	fsm->stack_e[fsm->sp_e++] = fsm->mark_nameend;
	
	DEBUG && strncpy(buffer, fsm->stack_e[fsm->sp_e - 2], fsm->stack_e[fsm->sp_e - 1] - fsm->stack_e[fsm->sp_e - 2]);
	DEBUG && fprintf(stderr, "pushETag: pushing '%s'\n", buffer);
}



/* 
 * pop the topmost element
 */
void popTag(XMLScanner *fsm) {

	char buffer[MAXTAGLENGTH];
	bzero(buffer, sizeof(buffer));

	if (fsm->sp < 2) {
		fprintf(stderr, "popTag: stack underflow, can't pop more!\n");
		return;
	}

	fsm->sp -= 2;
	
	DEBUG && strncpy(buffer, fsm->stack[fsm->sp], fsm->stack[fsm->sp + 1] - fsm->stack[fsm->sp]);
	DEBUG && fprintf(stderr, "popTag: popping '%s'\n", buffer);
}


/*
 * check out the end tag we just stumbled upon.
 * the behavior is different here, according to the scan mode
 * (before or after cursor position).
 */
void checkETag(XMLScanner *fsm) {

	char buffer[MAXTAGLENGTH];
	bzero(buffer, sizeof(buffer));
	int len;

	/* return if the stack is empty in BEFORE mode, we can't do anything interesting */
	if (!fsm->sp && fsm->mode == BEFORE) {
		return;
	}

	len = fsm->mark_nameend - fsm->mark_namestart;

	strncpy(buffer, fsm->mark_namestart, len);

	/* if topmost tag on stack is identical to current end tag, pop it */
	if(fsm->sp && !strncmp(fsm->stack[fsm->sp - 2], buffer, len)) {
//		fprintf(stderr, "checkETag: popping, len = %d, etag = '%s'\n", len, buffer);
		popTag(fsm);			
	} else {
		pushETag(fsm);	
	}


}

