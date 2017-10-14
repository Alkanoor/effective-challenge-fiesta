#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>

int main()
{
    //char filename[] = "/tmp/b/self_modified";
    char filename[] = "crash";
    //char prog[] = "/home/classic8/xbase64";
    char prog[] = "to_exploit";

    int id = fork();

    if(id<0)
    {
        printf("Error forking\n");
        return -1;
    }
    else if(id)
    {
        FILE* f = fopen(filename,"w+");
        char buf[100001];
        buf[100000] = 0;
        memset(buf,'A',100000);
        fwrite(buf,1,4096,f);
        fflush(f);
        fclose(f);

        int fd;
    	struct stat stats;
        if((fd = open(filename, O_RDONLY)) == -1 || fstat(fd, &stats) == -1)
    	{
    		printf("Error while opening file\n");
    		return 1;
    	}
        else
            printf("Size of %d\n",stats.st_size);

        wait(NULL);
    }
    else
    {
        char* argv[] = {prog,"1",filename,NULL};
        if(execve(prog,argv,NULL)<0)
        {
            printf("Error exec\n");
            return -1;
        }
    }

    return 0;
}
