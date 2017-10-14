#include <string.h>
#include <stdio.h>

#define MAX_SIZE 	1024

void mystrncpy( char * dest, char * src, size_t max_size )
{
	memset( (void *)dest, 0, max_size+1 );
	while( strlen(dest) <= max_size && *src != '\0' )
	{
		*dest++ = *src++;
	}
}

int main( int argv, char ** argc )
{
	char buff[ MAX_SIZE + 1 ];

	if( argv != 2 )
	{
		printf("Usage : %s <string>\n", argc[0]);
		return 1;
	}

	mystrncpy( buff, argc[1], MAX_SIZE );
	printf("buff is \"%s\"\n", buff);

	return 0;
}
