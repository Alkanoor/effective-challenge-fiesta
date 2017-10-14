int __fastcall sub_86A0(int a1, int a2, int a3)
{
  int v3; // r8@1
  int v4; // r2@1
  int v5; // r4@1
  int v6; // r9@1
  int v7; // r3@1
  int v8; // r5@3
  int v9; // r6@3
  unsigned __int8 v10; // r1@4
  int v11; // r2@4
  char v12; // r1@4

  v3 = a3;
  v4 = 0;
  *(_BYTE *)(a1 + 255) = 0;
  v5 = a1;
  v6 = a2;
  v7 = 1;
  do
  {
    *(_BYTE *)(a1 + v4) = v4;
    v4 = v7;
    v7 = (v7 + 1) & 0xFF;
  }
  while ( v7 != 1 );
  *(_BYTE *)(a1 + 256) = 0;
  v8 = 0;
  *(_BYTE *)(a1 + 255) = 0;
  v9 = 0;
  do
  {
    sub_88CC(v8, v3);
    v9 = (((*(_BYTE *)(v5 + v8) + *(_BYTE *)(v6 + v10)) & 0xFF) + v9) & 0xFF;
    *(_BYTE *)(v5 + 256) = v9;
    v11 = *(_BYTE *)(v5 + 255);
    v12 = *(_BYTE *)(v5 + v11);
    *(_BYTE *)(v5 + v11) = *(_BYTE *)(v5 + v9);
    *(_BYTE *)(v5 + v9) = v12;
    v8 = ((*(_BYTE *)(v5 + 255))++ + 1) & 0xFF;
  }
  while ( v8 );
  *(_BYTE *)(v5 + 256) = 0;
  *(_BYTE *)(v5 + 255) = 0;
  return v5;
}
