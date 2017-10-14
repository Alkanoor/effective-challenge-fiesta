#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>


void sub_400786()
{
    printf("Exiting\n");
    exit(1);
}

int sub_40079E(int a1, uint64_t a2)
{
  char **v2; // ST00_8@4
  int result; // eax@30
  char s; // [sp+10h] [bp-D0h]@4
  int v5; // [sp+94h] [bp-4Ch]@10
  int v6; // [sp+98h] [bp-48h]@10
  int v7; // [sp+9Ch] [bp-44h]@10
  char *v8; // [sp+A0h] [bp-40h]@4
  FILE *stream; // [sp+A8h] [bp-38h]@4
  int v10; // [sp+B4h] [bp-2Ch]@1
  char *v11; // [sp+B8h] [bp-28h]@1
  char *v12; // [sp+C0h] [bp-20h]@1
  size_t v13; // [sp+CCh] [bp-14h]@1
  int i; // [sp+D0h] [bp-10h]@20
  int v15; // [sp+D4h] [bp-Ch]@1
  int v16; // [sp+D8h] [bp-8h]@1
  int32_t v17; // [sp+DCh] [bp-4h]@1

  v13 = 0;
  v17 = 1;
  v12 = "BAD PASSWORD";
  v11 = "21232f297a57a5a743894a0e4a801fc3";
  v10 = 0;
  v16 = -1;
  v15 = -1;
  puts("Are you ready for crackme?");
  if ( a1 != 2 )
  {
    puts("No password given. Exiting cowardly...");
    puts("But the password is not always where you think...");
    exit(1);
  }
  v12 = *(char **)(a2);
  sprintf(&s, "echo -n %s | cut -c-9 | md5sum ", v12, a2);
  //v11 = &s;
  v11 = "f6674e62795f798fe2b01b08580c3f";
  //stream = popen(&s, "r");
  //fgets(v11, 31, stream);
  //pclose(stream);
  printf("%s\n",v11);
  fflush(stdout);
  //v12 = *v2;
  v13 = strlen(v12);
  printf("Validating a %d char password (%s) ...\n", v13, v11);
  v8 = strchr(v11, 48);
  if ( !v8 )
    sub_400786();
  printf("%d\n",v8);
  fflush(stdout);
  v16 = *v8 - 48;
  printf("%d\n",v16);
  fflush(stdout);
  v8 = strchr(v11, 49);
  printf("%d\n",v8);
  fflush(stdout);
  if ( !v8 )
    sub_400786();
  v15 = *v8 - 48;
  printf("v15 %d\n",v15);
  fflush(stdout);
  v17 = ptrace(0, 0LL, 0LL, 0LL);
  if ( v17 == -1 )
    sub_400786();
  printf("v17 %d\n",v17);
  fflush(stdout);
  printf("v7 %08x\n",v7);
  fflush(stdout);
  v7 += -3 * ptrace(0, 0LL, 0LL, 0LL);
  printf("v7 %08x\n",v7);
  fflush(stdout);
  v6 = *v12 - v12[1];
  v5 = *v12 - v12[2];
  printf("v6 v5 %d %d\n",v6,v5);
  fflush(stdout);
  v10 = v12[2] - v12[3];
  printf("v10 %d\n",v10);
  fflush(stdout);
  if ( v7 + v7 + v12[2] + -2 * v5 + v6 * v7 - v12[3] + v15 )
    ++v17;
  if ( (signed int)v13 > 14 )
    sub_400786();
  if ( 222 * v5 + 51 * v6 - v12[2] + v12[3] != -8985 )
    ++v17;
  if ( (signed int)v13 <= 3 )
    sub_400786();
  if ( 100 * v10 - v5 + -22 * v6 != 1550 )
    ++v17;
  v6 = v12[4];
  v17 += 1341 * (v6 >> 7);
  v6 = ~(uint8_t)v6 & 0x7F ^ 0x4C;
  for ( i = v16; i < v15; ++i )
    v17 += v6 + 700;
  v6 = v12[5];
  v17 += (uint8_t)(~(uint8_t)v6 ^ 0x9B) + -700 * v15;
  v6 = v12[8] + 2;
  if ( v15 == 2 )
    sub_400786();
  v5 = v12[7];
  v10 = v12[6];
  v17 += 1670 * (v6 ^ 0x22 | v10 ^ 0x36 | v5 ^ 0x65);
  if ( v17 < -2 )
    sub_400786();
  if ( (uint8_t)~(2 * *v12) != 89 )
    sub_400786();
  v6 = ptrace(0, 0LL, 0LL, 0LL);
  v17 += v15 + v16 + v6;
  if ( v17 )
  {
    result = puts("You loose. Try harder.");
  }
  else
  {
    puts("You WON! Congratulations!!");
    result = printf("Use %s to validate.\n", v12);
  }
  return result;
}

int main()
{
    char* argv = "ABCDEF";
    sub_40079E(2,&argv);
}
