#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE	150
#define SERIALIZE	1
#define UNSERIALIZE	2

void serialize( char * serialized, int * tab, unsigned int size )
{
	unsigned int i;
	char buffer[26] = {0}; /* strlen(max(unsigned int)) + strlen(max(int)) + strlen(": ,") + null byte = 11+11+3+1 = 26 */

	serialized[0] = '[';

	for( i=0; i<size; i++ )
	{
		printf("%d:%d\n", i, tab[i] );
		sprintf(buffer, "%d:%d, ", i, tab[i] );
		if( strlen(serialized)+strlen(buffer) > MAX_SIZE )
		{
			printf("Serialization failed.\n");
			break;
		}
		strcat( serialized, buffer );
	}

	serialized[strlen(serialized)-2] = ']';
	serialized[strlen(serialized)-1] = '\0';
}

void unserialize( int * unserialized, char * str, int * n )
{
	char * buffer;
	int index, value;

	*n = 0;

	if( str[0] != '[' || str[strlen(str)-1] != ']' )
	{
		printf("Invalid format.\n");
	}
	else
	{
		str++;
		while( sscanf(str, "%d:%d", &index, &value) == 2 )
		{
			unserialized[index] = value;
			*n = index+1 > *n ? index+1 : *n;
			buffer = strstr(str, ", ");
			if( buffer != NULL )
			{
				str = buffer + 2;
			}
			else
			{
				break;
			}
		}
	}
}

int main( int argc, char ** argv )
{
	int i,n;
	int intTab[MAX_SIZE] = {0};
	char serialized[MAX_SIZE + 1] = {0};

	if( argc < 3 )
	{
		printf( "Usage : %s <action> <arg1> [ ... <argN>]\n", argv[0] );
		printf( "\t-> <action>=1 : serialization of all argv[]\n" );
		printf( "\t-> <action>=2 : unserialization of argv[2]\n" );
		exit(1);
	}

	switch( atoi(argv[1]) )
	{
		case SERIALIZE :
			for( i=2; i<argc; i++ )
			{
				intTab[i-2] = atoi(argv[i]);
			}
			serialize( serialized, intTab, argc-2 );
			printf("Serialized array : %s\n", serialized);
			break;

		case UNSERIALIZE :
			unserialize( intTab, argv[2], &n );
			printf("Array \"%s\" has %d elements :\n", argv[2], n);
			for( i=0; i<n; i++ )
			{
				printf("\t%d->%d\n", i, intTab[i] );
			}
			break;

		default:
			printf("Unknown action.\n");
			break;
	}

	return 0;
}
