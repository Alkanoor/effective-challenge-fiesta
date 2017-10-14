signed int __fastcall sub_88F4(int a1, unsigned int a2, unsigned int a3, int a4, _DWORD *a5)
{
  bool v6; // zf@5

  if ( a2 )
  {
    if ( a2 <= 4 )
      return 1;
  }
  else
  {
    v6 = a3 == 15;
    if ( a3 <= 0xF )
      v6 = a4 == 0;
    if ( v6 )
    {
      *a5 = *(_DWORD *)(a1 + 4 * a3 + 4);
      return 0;
    }
  }
  return 2;
}