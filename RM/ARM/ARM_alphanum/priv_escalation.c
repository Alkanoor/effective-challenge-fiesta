#include <stdio.h>
#include <unistd.h>


int main()
{
    setreuid(geteuid(), geteuid());
    setregid(getegid(), getegid());
    char* args[] = {"/bin/sh", NULL};
    execv("/bin/sh", args);
}
