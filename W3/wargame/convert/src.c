#define _BSD_SOURCE
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE	50

int main( int argc, char ** argv )
{
	int type, data;
	char result[ MAX_SIZE + 1 ];
	char * format[] = { "%d", "%x", "%#010x", "%o" };

	if( argc < 3 )
	{
		printf("Usage : %s <value> <type>\n", argv[0]);
		puts("type 0 : no conversion");
		puts("type 1 : hexadecimal (number only)");
		puts("type 2 : hexadecimal (0x....)");
		puts("type 3 : octal");
		return 1;
	}

	data = atoi( argv[1] );
	type = atoi( argv[2] );

	printf("Format : %s\n", format[type]);
	snprintf(result, MAX_SIZE, "Result : %s\n", format[type]);
	printf(result, data);

	return 0;
}
