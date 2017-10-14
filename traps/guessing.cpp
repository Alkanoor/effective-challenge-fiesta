#include "victory.hpp"


int f(int x)
{
    printf("%08x\n",&x);
    for(int i=0;i<20;i++)
        printf("%d\n",*(&x+i));
    printf("\n");
    return *(&x+17);
}

int main()
{
  int a[3] = {9,4,5};
  int b[3] = {9,8,0};
  for(int i=0;i<3;i++)
    if(f(a[i])!=b[i]) return 0;
  victory();
  return 0;
}

// Your main objective is to call the victory function.
// You must put your code:
// - Max 12 chars.
// - You can't use: "main", "victory", "asm", "#", "_".
