#include "victory.hpp"


int main()
{
  unsigned int y = 0xB0FF14a5;
  unsigned int x = 0x7340c00e;
  x=(y+=x-=y)-x;
  printf("%08x %08x\n",x,y);
  if(y==0x7340c00e && x==0xB0FF14a5) victory();
  return 0;
}

//swap9W4Pswap



// Your main objective is to call the victory function.
// You must put one line of your code:
// - Max 14 chars.
// - You can't use: "main", "victory", "asm", "#", "&", "*", "%", "/", "^".
// - You have only one semicolon.
