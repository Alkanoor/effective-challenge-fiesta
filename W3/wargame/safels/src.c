#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE        100
#define COMMAND         "/bin/ls -lah "

char * escapeshell( char * str )
{
        char dangerous[] = "#&;`'\"|*?~<>^()[]{}$\\,\x0a ";
        unsigned int i = 0, j = 0, count = 0;
        char * buffer = (char *) malloc( MAX_SIZE + 1 );

        while( i<strlen(str) && count<MAX_SIZE )
        {
                for( j=0; j<strlen(dangerous); j++ )
                {
                        if( str[i] == dangerous[j] )
                        {
                                buffer[count++] = '\\';
                                break;
                        }
                }

                buffer[count++] = str[i++];
        }

	return buffer;
}

int main( int argc, char ** argv )
{
	char safe[ sizeof(COMMAND) + MAX_SIZE + 1] = {'\0'};

	if( argc != 2 )
	{
		printf( "Usage : %s <file or dir>\n", argv[0] );
		exit(1);
	}

	strcat( safe, COMMAND );
	strcat( safe, escapeshell( argv[1] ) );

	printf("Command : \"%s\"\n", safe );
	system( safe );

	return 0;
}
