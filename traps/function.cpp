#include "victory.hpp"


int f(int x=0)
{
  if(x==1337)
    return true;
  return false;
}

int main()
{
  if(1)
  if(f()) victory();
}


// Your main objective is to call the victory function.
// You must put one line of your code:
// - Max 18 chars.
// - You can't use: "main", "victory", "asm", "#", "&", "*", "%", "/".
// - You have only one semicolon.
