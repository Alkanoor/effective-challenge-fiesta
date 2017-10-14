#define _POSIX_SOURCE
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define MAX_SIZE	150
#define MAX_CONNECT	5

void cleararray( char ** array )
{
	unsigned int i = 0;

	while( array[i] )
	{
		memset( array[i], 0, strlen(array[i])+1 );
		i++;
	}
}

void handle_client( int client )
{
	char sent[ MAX_SIZE + 1 ] = {0}, received[ MAX_SIZE + 1 ] = {0};
	int nb = -1;

	if( (nb = recv(client, received, MAX_SIZE, 0)) == -1 )
	{
		close(client);
		exit(1);
	}

	if( received[ strlen(received)-1 ] == '\n' )
		received[ strlen(received)-1 ] = '\0';

	sprintf(sent, "The string you just sent is : \"%s\"\n", received);
	memset(received, 0, MAX_SIZE+1);
	send(client, sent, MAX_SIZE, 0);

	close(client);
}

void handle_signal( int signal )
{
	signal = signal;
	waitpid( -1, NULL, WNOHANG );
}

int main( int argc, char ** argv, char ** envp )
{
	int server, client, port;
	unsigned int clientlen;
	struct sockaddr_in structserver, structclient;
	struct sigaction sig;

	if( argc != 2 )
	{
		printf("[-] Usage : %s <port>\n", argv[0]);
		exit(1);
	}

	if( (port = atoi(argv[1])) < 1024 )
	{
		puts("[-] Port must be > 1024");
		exit(1);
	}

	cleararray( argv );
	cleararray( envp );

	sig.sa_handler = handle_signal;
	sigemptyset(&sig.sa_mask);
	sig.sa_flags = SA_NOCLDSTOP;

	if( sigaction(SIGCHLD, &sig, NULL) == -1 )
	{
		perror("[-] Sigaction Fail ");
		exit(1);
	}

	if( (server = socket(PF_INET, SOCK_STREAM, 0)) == -1 )
	{
		perror("[-] Socket Fail ");
		exit(1);
	}

	puts("[+] Socket created.");

	memset(&structserver, 0, sizeof(structserver));
	structserver.sin_family = AF_INET;
	structserver.sin_addr.s_addr = inet_addr("127.0.0.1");
	structserver.sin_port = htons(port);

	if( bind(server, (struct sockaddr *)&structserver, sizeof(structserver)) == -1 )
	{
		perror("[-] Bind Fail ");
		exit(1);
	}

	if( listen(server, MAX_CONNECT) == -1 )
	{
		perror("[-] Listen Fail ");
		exit(1);
	}

	printf("[+] Listening on %d.\n", port);

	for(;;)
	{
		clientlen = sizeof(structclient);
		if( (client = accept(server, (struct sockaddr *)&structclient, &clientlen)) == -1 )
		{
			perror("[-] Accept Fail ");
			continue;
		}

		printf("[+] New client : %s\n", inet_ntoa(structclient.sin_addr));

		switch( fork() )
		{
			case -1:
				perror("[-] Fork Fail ");
				break;

			case 0:
				close(fileno(stdin));
				close(fileno(stdout));
				close(fileno(stderr));
				handle_client( client );
				exit(0);
		}
	}

	close( server );
	return 0;
}
