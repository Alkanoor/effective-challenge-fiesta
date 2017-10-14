#include "victory.hpp"


int in, out;

int g(int a, int b)
{
 return (a == b ? 1337 : -1);
}

void f()
{
    printf("%d %08x %08x\n",in,(&f)[in],*((&f)[in]));
}

int main()
{
 const int N = 6;
 int values[N] = {1100, 1101, 1104, 1109, 1116, 1125};
 for (int i = 0; i < N; i++)
 {
   in = i; f();
   if (g(out, values[i]) != 1337) return 0;
 }
 victory();
 return 0;
}

// Your main objective is to call the victory function.
// You must put your code:
// - Max 14 chars.
// - You can't use: "main", "victory", "asm", "#", "_", "(".
