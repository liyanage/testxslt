
#include "ragel_xmlscanner.h"



int main() {

	char *data, *pos;

	pos = data = (char *)malloc(40000);
	int readlen = 0, i;
	unsigned int result;
	char (*resultstack)[MAXTAGLENGTH];

	while ((readlen = read(0, pos, 40000)) > 0) {
		pos += readlen;
	}


	resultstack = findCompletion(data, pos - data, 184, &result, NULL);
	for (i = 0; resultstack && *(resultstack[i]); i++) {
		fprintf(stderr, "tag main (%p): '%s'\n", resultstack[i], resultstack[i]);
	}

	if (resultstack)
		free(resultstack);

	exit(0);

}

