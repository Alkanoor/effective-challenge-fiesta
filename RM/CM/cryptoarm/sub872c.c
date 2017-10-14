int __fastcall sub_872C(int a1, int a2, int a3, int a4)
{
  int v4; // r6@2
  int v5; // r4@3
  int v6; // r5@3
  int v7; // r7@3

  if ( a4 )
  {
    v4 = 0;
    do
    {
      ++v4;
      v5 = ((*(_BYTE *)(a1 + 255))++ + 1) & 0xFF;
      v6 = (*(_BYTE *)(a1 + v5) + *(_BYTE *)(a1 + 256)) & 0xFF;
      *(_BYTE *)(a1 + 256) += *(_BYTE *)(a1 + v5);
      v7 = *(_BYTE *)(a1 + v5);
      *(_BYTE *)(a1 + v5) = *(_BYTE *)(a1 + v6);
      *(_BYTE *)(a1 + v6) = v7;
      *(_BYTE *)(a3 + v5) = *(_BYTE *)(a2 + v5) ^ *(_BYTE *)(a1 + v7 + *(_BYTE *)(a1 + v5));
    }
    while ( v4 != a4 );
  }
  return a3;
}