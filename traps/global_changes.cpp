#include "victory.hpp"


int b=0;

void f(int x)
{
  for(int
  &i=b
  ;i<x;++i);
}

int main()
{
  int d=982398;
  f(d);
  if(b==d)
    victory();
}


// Your main objective is to call the victory function.
// You must put one line of your code:
// - Max 6 chars.
// - You can't use: "main", "victory", "asm", "#", "x".
// - You have only one semicolon.
