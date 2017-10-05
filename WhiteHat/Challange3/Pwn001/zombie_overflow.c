//----- (08048544) --------------------------------------------------------
signed int choice()
{
  bool v0; // cf
  bool v1; // zf
  signed int v2; // ecx
  char *v3; // esi
  const char *v4; // edi
  int v5; // eax
  bool v6; // cf
  bool v7; // zf
  bool v8; // cf
  bool v9; // zf
  signed int v10; // ecx
  int *v11; // esi
  const char *v12; // edi
  int v13; // eax
  signed int v14; // ecx
  char *v15; // esi
  const char *v16; // edi
  int v17; // eax
  bool v18; // cf
  bool v19; // zf
  bool v20; // cf
  bool v21; // zf
  signed int v22; // ecx
  int *v23; // esi
  const char *v24; // edi
  int v25; // eax
  signed int v26; // ecx
  char *v27; // esi
  const char *v28; // edi
  int v29; // eax
  bool v30; // cf
  bool v31; // zf
  bool v32; // cf
  bool v33; // zf
  signed int v34; // ecx
  int *v35; // esi
  const char *v36; // edi
  int v37; // eax
  signed int v38; // ecx
  char *v39; // esi
  const char *v40; // edi
  bool v41; // cf
  bool v42; // zf
  signed int v43; // ecx
  int *v44; // esi
  const char *v45; // edi
  char s; // [esp+18h] [ebp-210h]
  int v48; // [esp+118h] [ebp-110h]
  int v49; // [esp+11Ch] [ebp-10Ch]
  unsigned int v50; // [esp+21Ch] [ebp-Ch]

  v50 = __readgsdword(20u);
  v48 = 0xDEAD;
  printf("Your weapon : ");
  gets(&s);
  printf("Your action : ");
  gets((char *)&v49);
  v2 = 7;
  v3 = &s;
  v4 = "katana";
  do
  {
    if ( !v2 )
      break;
    v0 = (unsigned __int8)*v3 < *v4;
    v1 = *v3++ == *v4++;
    --v2;
  }
  while ( v1 );
  v5 = (char)((!v0 && !v1) - v0);
  v6 = 0;
  v7 = v5 == 0;
  if ( v5 )
    goto LABEL_40;
  v8 = __CFADD__(&s, 260);
  v9 = &v49 == 0;
  v10 = 12;
  v11 = &v49;
  v12 = "run away...";
  do
  {
    if ( !v10 )
      break;
    v8 = *(_BYTE *)v11 < (const unsigned __int8)*v12;
    v9 = *(_BYTE *)v11 == *v12;
    v11 = (int *)((char *)v11 + 1);
    ++v12;
    --v10;
  }
  while ( v9 );
  v13 = (char)((!v8 && !v9) - v8);
  v6 = 0;
  v7 = v13 == 0;
  if ( !v13 )
    return 60;
LABEL_40:
  v14 = 13;
  v15 = &s;
  v16 = "baseball bat";
  do
  {
    if ( !v14 )
      break;
    v6 = (unsigned __int8)*v15 < *v16;
    v7 = *v15++ == *v16++;
    --v14;
  }
  while ( v7 );
  v17 = (char)((!v6 && !v7) - v6);
  v18 = 0;
  v19 = v17 == 0;
  if ( v17 )
    goto LABEL_41;
  v20 = __CFADD__(&s, 260);
  v21 = &v49 == 0;
  v22 = 31;
  v23 = &v49;
  v24 = "make their head flying to sky~";
  do
  {
    if ( !v22 )
      break;
    v20 = *(_BYTE *)v23 < (const unsigned __int8)*v24;
    v21 = *(_BYTE *)v23 == *v24;
    v23 = (int *)((char *)v23 + 1);
    ++v24;
    --v22;
  }
  while ( v21 );
  v25 = (char)((!v20 && !v21) - v20);
  v18 = 0;
  v19 = v25 == 0;
  if ( !v25 )
    return 30;
LABEL_41:
  v26 = 7;
  v27 = &s;
  v28 = "shovel";
  do
  {
    if ( !v26 )
      break;
    v18 = (unsigned __int8)*v27 < *v28;
    v19 = *v27++ == *v28++;
    --v26;
  }
  while ( v19 );
  v29 = (char)((!v18 && !v19) - v18);
  v30 = 0;
  v31 = v29 == 0;
  if ( v29 )
    goto LABEL_42;
  v32 = __CFADD__(&s, 260);
  v33 = &v49 == 0;
  v34 = 30;
  v35 = &v49;
  v36 = "feed them some sweet metal <3";
  do
  {
    if ( !v34 )
      break;
    v32 = *(_BYTE *)v35 < (const unsigned __int8)*v36;
    v33 = *(_BYTE *)v35 == *v36;
    v35 = (int *)((char *)v35 + 1);
    ++v36;
    --v34;
  }
  while ( v33 );
  v37 = (char)((!v32 && !v33) - v32);
  v30 = 0;
  v31 = v37 == 0;
  if ( !v37 )
    return 40;
LABEL_42:
  v38 = 9;
  v39 = &s;
  v40 = "keyboard";
  do
  {
    if ( !v38 )
      break;
    v30 = (unsigned __int8)*v39 < *v40;
    v31 = *v39++ == *v40++;
    --v38;
  }
  while ( v31 );
  if ( (!v30 && !v31) == v30 )
  {
    v41 = __CFADD__(&s, 260);
    v42 = &v49 == 0;
    v43 = 25;
    v44 = &v49;
    v45 = "to be a keyboard hero!!!";
    do
    {
      if ( !v43 )
        break;
      v41 = *(_BYTE *)v44 < (const unsigned __int8)*v45;
      v42 = *(_BYTE *)v44 == *v45;
      v44 = (int *)((char *)v44 + 1);
      ++v45;
      --v43;
    }
    while ( v42 );
    if ( (!v41 && !v42) == v41 )
      v48 = 100;
  }
  return v48;
}

//----- (08048760) --------------------------------------------------------
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax
  signed int v4; // [esp+1Ch] [ebp-4h]

  setbuf(stdout, 0);
  printf("Zombie apocalypse!!!!");
  puts("What will you do now, little boy?");
  v4 = choice();
  result = printf("Your live percentage is: 0x%04x \n", v4);
  if ( v4 >= 0 && v4 <= 40 )
  {
    printf("Never watch a zombie series? Try again!");
    exit(10);
  }
  if ( v4 == 0xC0DE )
  {
    puts("My great survivor!");
    printf("Here is your prize: ");
    result = system("cat flag.txt");
  }
  else
  {
    if ( v4 > 40 && v4 <= 100 )
    {
      puts("Wow so good! Sadly, not enough :'(");
      exit(1);
    }
    if ( v4 == 57005 )
    {
      puts("You did it! Except some bite on your arm :O");
      exit(1);
    }
  }
  return result;
}

