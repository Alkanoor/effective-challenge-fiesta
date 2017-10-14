#include <stdlib.h>
#include <unistd.h>


int main()
{
	setreuid(geteuid(),geteuid());
	char* args[] = {"/bin/sh",NULL};
	execv("/bin/sh",args);
}