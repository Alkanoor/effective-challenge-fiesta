int sub_8798()
{
  int v0; // r8@1
  void *v1; // r6@1
  int result; // r0@1
  signed int v3; // [sp+0h] [bp-1Ch]@1
  signed int v4; // [sp+4h] [bp-18h]@1
  signed int v5; // [sp+8h] [bp-14h]@1
  signed int v6; // [sp+Ch] [bp-10h]@1
  signed int v7; // [sp+10h] [bp-Ch]@1
  signed int v8; // [sp+14h] [bp-8h]@1
  __int16 v9; // [sp+18h] [bp-4h]@1
  char v10; // [sp+1Ah] [bp-2h]@1
  signed int v11; // [sp+1Ch] [bp+0h]@1
  signed int v12; // [sp+20h] [bp+4h]@1
  signed int v13; // [sp+24h] [bp+8h]@1
  __int16 v14; // [sp+28h] [bp+Ch]@1
  int v15; // [sp+2Ch] [bp+10h]@1

  v15 = _stack_chk_guard;
  v3 = 737108310;
  v4 = 1824333979;
  v5 = -1172281516;
  v6 = 1585324202;
  v7 = 1008355505;
  v8 = 1328708234;
  v9 = unk_9E54;
  v10 = unk_9E56;
  v11 = 1668181869;
  v12 = 1936024687;
  v13 = 1701995365;
  v14 = *(_WORD *)"t";
  v0 = strlen((const char *)&v3);
  v1 = sub_8788();
  sub_86A0((int)v1, (int)&v11, 13);
  sub_872C((int)v1, (int)&v3, (int)&v3, v0);
  puts("Basic ARM Crypto challenge for Root-Me\nAuthor: koma\n\nFind the flag inside.\n");
  result = 0;
  if ( v15 != _stack_chk_guard )
    _stack_chk_fail(0);
  return result;
}

//~^NHv<uz20;T
