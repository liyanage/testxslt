
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


#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <strings.h>

#define STACKDEPTH 600
#define MAXTAGLENGTH 100
#define DEBUG 0


/* bit field flags for the return value, to indicate state to the caller */
enum {
	ERROR_IN_TAG = 1,
	ERROR_IN_COMMENT = 2,
	ERROR_IN_CDATA = 4,
	ERROR_NO_TAG = 8,
	ERROR_ALREADY_BALANCED_HERE = 16
};

char (*findCompletion(char *data, int len, int cursor, int *result, int tagpositions[]))[];


/*

int main() {

	char *data, *pos;

	pos = data = (char *)malloc(40000);
	int readlen = 0, i;
	unsigned int result;
	char (*resultstack)[MAXTAGLENGTH];

	while ((readlen = read(0, pos, 40000)) > 0) {
		pos += readlen;
	}


	resultstack = findCompletion(data, pos - data, 1382, &result);
	for (i = 0; resultstack && *(resultstack[i]); i++) {
		fprintf(stderr, "tag main (%p): '%s'\n", resultstack[i], resultstack[i]);
	}

	if (resultstack)
		free(resultstack);

	exit(0);

}


*/

