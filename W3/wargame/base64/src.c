#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>

#define OPEN_MODE       (O_RDONLY)
#define MMAP_MODE       (PROT_READ)
#define ARRAY_SIZE      65
#define MAGIC_KEY       0xcafebabe

char table[ ARRAY_SIZE + 1 ] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
int verbose = 0;

unsigned int rdtsc()
{
	unsigned int lo, hi;
	__asm__ __volatile__ ("rdtsc" : "=a" (lo), "=d" (hi));

	return lo ^ hi;
}

void init_rand( char * str )
{
	int key;

	if( str == NULL )
		key = rdtsc();
	else
		key = atoi( str ) ^ MAGIC_KEY;

	if( verbose )
		printf( "Key : %u\n", key );
	srand( key );
}

void shuffle()
{
	unsigned int i,j;
	char tmp;

	for( i=0; i<ARRAY_SIZE-1; i++ )
	{
		j = i + rand() / (RAND_MAX / (ARRAY_SIZE - i) + 1);
		tmp = table[j];
		table[j] = table[i];
		table[i] = tmp;
	}
}

int is_64( char * str )
{
	unsigned int i;
	for( i=0; i<strlen(str); i++ )
		if( !isalnum(str[i]) && str[i] != '+' && str[i] != '/' && str[i] != '=')
			return 0;
	return (strlen(str) % 4 == 0);
}

char indexof( char c )
{
	unsigned int i = 0;
	while( i < ARRAY_SIZE && table[i++] != c );
	return (char)i-1;
}

void encode( char * plain, char * ret )
{
	size_t i, j, rest;
	unsigned char c1, c2, c3, * cipher;

	if( ret != NULL )
		cipher = ret;
	shuffle();
	if( verbose )
		printf("Table : %s\n", table);

	for( i=0, rest=strlen( plain ), j=0; rest>=3; i+=3, rest-=3, j+=4 )
	{
		c1 = plain[i];
		c2 = plain[i+1];
		c3 = plain[i+2];

		cipher[j] 	= table[ c1 >> 2 ];
		cipher[j+1] = table[ ((c1 & 3) << 4) | (c2 >> 4) ];
		cipher[j+2] = table[ ((c2 & 0x0F) << 2) | (c3 >> 6) ];
		cipher[j+3] = table[ c3 & 0x3F ];
	}

	if( rest == 1 )
	{
		c1 = plain[i];

		cipher[j]	= table[ c1 >> 2 ];
		cipher[j+1]	= table[ (c1 & 3) << 4 ];
		cipher[j+2]	= table[ ARRAY_SIZE-1 ];
		cipher[j+3]	= table[ ARRAY_SIZE-1 ];
	}
	else if( rest == 2 )
	{
		c1 = plain[i];
		c2 = plain[i+1];

		cipher[j]	= table[ c1 >> 2 ];
		cipher[j+1]	= table[ ((c1 & 3) << 4) | (c2 >> 4) ];
		cipher[j+2]	= table[ (c2 & 0x0F) << 2 ];
		cipher[j+3]	= table[ ARRAY_SIZE-1 ];
	}
}

void decode( char * cipher, char * ret )
{
	size_t i, j, rest;
	unsigned char c1, c2, c3, c4, * plain;

	if( ret != NULL )
		plain = ret;
	shuffle();
	if( verbose )
		printf("Table : %s\n", table);

	if( !is_64( cipher ) )
	{
		puts("Invalid base64 encoded text");
		exit(1);
	}

	for( i=0, rest=strlen(cipher), j=0; rest>=4; i+=4, rest-=4, j+=3 )
	{
		c1 = indexof( cipher[i] );
		c2 = indexof( cipher[i+1] );
		c3 = indexof( cipher[i+2] );
		c4 = indexof( cipher[i+3] );

		plain[j]	= (c1 << 2) | (c2 >> 4) ;
		if( c3 < ARRAY_SIZE-1 )
		{
			plain[j+1]	= (c2 << 4) | (c3 >> 2) ;
			if( c4 < ARRAY_SIZE-1 )
				plain[j+2]	= (c3 << 6) | c4 ;
		}
	}
}

int main( int argc, char ** argv )
{
	int action, fd;
	char * buffer, * ret;
	struct stat stats;

	if( argc < 3 )
	{
		printf("Usage : %s <action> <file> [key] [verbose]\n", argv[0]);
		return 1;
	}

	action = atoi( argv[1] );

	if( (fd = open(argv[2], OPEN_MODE)) == -1 || fstat(fd, &stats) == -1 || stats.st_uid != getuid() || (buffer = (char *)mmap(0, (size_t)stats.st_size, MMAP_MODE, MAP_PRIVATE, fd, 0)) == MAP_FAILED )
	{
		printf("Error while opening file %s\n", argv[2]);
		return 1;
	}

	ret = malloc( stats.st_size*4/3 + 4 );
	verbose = argc > 4 && strcmp(argv[4], "-v") == 0 ? 1 : 0;
	init_rand( argc > 3 && strcmp(argv[3], "null") != 0 ? argv[3] : NULL );

	switch( action )
	{
		case 1:
			encode( buffer, ret );
			printf( verbose ? "Cipher : %s\n" : "%s", ret);
			break;

		case 2:
			decode( buffer, ret );
			printf( verbose ? "Plain : %s\n" : "%s", ret);
			break;

		default:
			puts("Invalid action");
	}

	free( ret );
	close( fd );
	munmap( buffer, stats.st_size );

	return 0;
}
