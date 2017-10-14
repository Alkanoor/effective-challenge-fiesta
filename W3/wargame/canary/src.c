#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <openssl/sha.h>

#define SHA1_SIZE	20
#define MAX_SIZE	30
#define HASH_LOGIN	"22ced300842e468ad2d5449158708b18dc1f6d66"
#define HASH_PASS	"7280ffe5d72b47186f62ef575bfc4dd42c92d053"

int stackguard;

int boundedrand( int min, int max )
{
	return min + (int)((float)max * (rand() / (RAND_MAX + (float)min)));
}

int check(const char * login, const char * password)
{
	char hashlog[SHA1_SIZE + 1] = {0}, hashpass[SHA1_SIZE + 1] = {0}, goodlog[] = HASH_LOGIN, goodpass[] = HASH_PASS;
	SHA1(login, strlen((char *)login), hashlog);
	SHA1(password, strlen((char *)password), hashpass);

	return (strcmp(hashlog, goodlog) == 0 && strcmp(hashpass, goodpass) == 0);
}

int init_stackguard()
{
	srand( getpid() );
	stackguard = rand();
	*( (char *)&stackguard + boundedrand(0,3) ) = '\x00';

	return stackguard;
}

int main( int argc, char ** argv )
{
	int canary = init_stackguard();
	char login[ MAX_SIZE + 1 ], password[ MAX_SIZE + 1 ];

	if( argc != 3 )
	{
		printf("Usage : %s <login> <pass>\n", argv[0]);
		exit(1);
	}

	strcpy(login, argv[1]);
	strcpy(password, argv[2]);

	if( check(login, password) )
		puts("Good Boy =)");
	else
		puts("Bad Boy =(");

	if( canary != stackguard )
	{
		puts("Stack Smashing detected !");
		exit(1);
	}

	return 0;
}
