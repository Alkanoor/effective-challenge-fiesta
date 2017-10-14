/*gcc game_of_life_execute.c -o game_of_life_execute -m32 -z execstack*/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>


#define W (24+8)
#define H (5+8)
#define BUF_LEN 100
#define NB_GENERATIONS 10


char convert_to_char(char buf[H][W], int i, int j)
{
    int k=0;
    char ret=0;
    for(; k<8; k++)
        if(buf[i][j+k] == 1)
            ret += (1<<(7-k));
    return ret;
}

int call_shellcode(char buf[H][W])
{
    char shellcode[((W-8)*(H-8))/8+2];

    int i, j;
    for(i=4; i<(H-4); i++)
        for(j=4; j<(W-4); j+=8)
            shellcode[(j-4)/8+(W-4)/8*(i-4)] = convert_to_char(buf,i,j);

    printf("[.] Your hex encoded shellcode of size %d:\n", ((W-8)*(H-8))/8);
    for(i=0; i<((W-8)*(H-8))/8; i++)
        printf("\\x%02x", (unsigned char)shellcode[i]);
    printf("\n");
    fflush(stdout);

    void (*call_shell)() = (void *)&shellcode;
    call_shell();
}

void print_grid(char grid[H][W])
{
    int i=0, j=0;
    for(; i<H; i++)
    {
        for(j=0; j<W; j++)
            printf("%d", grid[i][j]);
        printf("\n");
    }
}

int count_around_approx(char grid[H][W], int i, int j)
{
    int r = 0, k, l;
    for(k=-1; k<2 && r<4; k++)
        for(l=-1; l<2 && r<4; l++)
            if(grid[i+k][j+l])
                if(k!=0 || l!=0)
                    r++;
    return r;
}

void genere_next(char prev[H][W], char next[H][W])
{
    int i=1, j;
    for(; i<H-1; i++)
        for(j=1; j<W-1; j++)
        {
            int c = count_around_approx(prev, i, j);
            if(c==3)
                next[i][j] = 1;
            else if(c==2)
                next[i][j] = prev[i][j];
            else
                next[i][j] = 0;
        }
}

int main(int argc, char* argv[])
{
    char buf[BUF_LEN+1];
    char grid[H][W] = {0};
    char cpy_grid[H][W] = {0};
    memset(buf,0,sizeof(buf));

    if(argc<2)
    {
        printf("Usage %s <filename>\n",argv[0]);
        exit(1);
    }

    int i=0, j=0, l;
    FILE* f = fopen(argv[1],"r");
    while(fgets(buf,BUF_LEN,f) && i<H)
    {
        l = strlen(buf);
        for(j=0; j<W && j<l; j++)
            if(buf[j]=='1')
                grid[i][j] = 1;
        i++;
    }

    printf("[+] Initial grid :\n");
    print_grid(grid);
    printf("\n");

    for(i=0; i<NB_GENERATIONS; i++)
    {
        genere_next(grid, cpy_grid);
        for(j=0; j<H; j++)
            memcpy(grid[j], cpy_grid[j], W);
    }

    printf("[+] Final grid after %d game of life iterations :\n", NB_GENERATIONS);
    print_grid(grid);
    printf("\n");

    printf("[+] Executing shell\n");
    call_shellcode(grid);

    return 0;
}
