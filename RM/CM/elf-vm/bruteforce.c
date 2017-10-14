#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>


#define TARGET "/home/alka/Documents/git/challs/all/RM/CM/elf-vm/ch18.bin"
#define LEN 1024

char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!_0123456789=";


int test_pass(char pass[])
{
    int fd1[2];
    int fd2[2];
    pipe(fd1);
    pipe(fd2);

    int id = fork();
    if(id<0)
    {
        perror("Fork failed");
        exit(1);
    }
    else if(!id)
    {
        close(fd1[0]);
        close(fd2[1]);

        dup2(fd1[1], STDOUT_FILENO);
        close(fd1[1]);

        dup2(fd2[0], STDIN_FILENO);
        close(fd2[0]);

        execlp(TARGET,NULL);
    }
    else
    {
        char buf[LEN+1];
        buf[LEN] = 0;

        close(fd1[1]);
        close(fd2[0]);

        usleep(100000);

        int n = read(fd1[0],buf,LEN);
        buf[n] = 0;
        printf("%d bytes read : %s\n",n,buf);
        write(fd2[1],pass,strlen(pass));
        n = read(fd1[0],v   buf,LEN);
        buf[n] = 0;
        printf("%d bytes read : %s\n",n,buf);
        wait(NULL);

        close(fd1[0]);
        close(fd2[1]);
    }
}

int main()
{
    test_pass("bonjour\n");
}
