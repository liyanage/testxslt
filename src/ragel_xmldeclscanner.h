
/*
 * This is an input file for the "Ragel" finite state machine compiler utility.
 *
 * Written by Marc Liyanage <http://www.entropy.ch>
 *
 */

/*
 * ragel -o ragel_xmldeclscanner_out.c ragel_xmldeclscanner.c && env CFLAGS='-framework CoreFoundation' make ragel_xmldeclscanner_out
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <strings.h>


#define DEBUG 0

unsigned int getEncodingFromXmlDecl(char *data, int len);


/*
int main() {

	char *data, *pos;

	pos = data = (char *)malloc(40000);
	int readlen = 0, i;
	unsigned int result;


	while ((readlen = read(0, pos, 40000)) > 0) {
		pos += readlen;
	}


	result = getEncodingFromXmlDecl(data, pos - data);


	printf("result: %d\n", result); 
}
*/