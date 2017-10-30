int __cdecl main(int argc, const char **argv, const char **envp)
{
  signed int i; // [esp+0h] [ebp-288h]
  int v5; // [esp+4h] [ebp-284h]
  signed int j; // [esp+8h] [ebp-280h]
  FILE *stream; // [esp+1Ch] [ebp-26Ch]
  int c; // [esp+20h] [ebp-268h]
  int v9[11]; // [esp+24h] [ebp-264h]
  int v10; // [esp+50h] [ebp-238h]
  int v11; // [esp+54h] [ebp-234h]
  int v12; // [esp+58h] [ebp-230h]
  char v13[5]; // [esp+1B4h] [ebp-D4h]
  char v14; // [esp+1B9h] [ebp-CFh]
  char v15; // [esp+1BAh] [ebp-CEh]
  char v16; // [esp+1BBh] [ebp-CDh]
  char v17[100]; // [esp+218h] [ebp-70h]
  unsigned int v18; // [esp+27Ch] [ebp-Ch]

  v18 = __readgsdword(20u);
  for ( i = 0; i <= 99; ++i )
    v17[i] = rand() % 90 + 33;
  puts("Hi friend!");
  puts("Are you good at Math ??");
  puts("If y0u'r3 g0d 3n0ugh! Plzzz wr1t3 s0meth1ng 4 me then we c4n ch3ck 1t. ");
  __isoc99_scanf("%s", v13);
  v5 = 0;
  for ( j = 0; j <= 4; ++j )
  {
    v9[j] = v17[j + 1];
    v5 += v9[j];
    v9[j + 5] = abs(v13[j + 6]);
  }
  v12 = 9;
  v11 = 9;
  v10 = 9;
  if ( 9
     * (v14 * v15 * (v5 - 0x15F)
      + v5 * 2 * v14 * v16
      + v5 * 3 * v16 * v15 
      - 0x2BE * v14 * v16 
      + 7 * v5 
      - 1053 * v16 * v15
      - 2457) )
  {
    printf("Nahhh !U may get the flag next time. But may be nerver !!");
  }
  else
  {
    stream = fopen("flag", "r");
    while ( 1 )
    {
      c = fgetc(stream);
      if ( feof(stream) )
        break;
      putchar(c);
    }
    fclose(stream);
  }
  return 1;
}
