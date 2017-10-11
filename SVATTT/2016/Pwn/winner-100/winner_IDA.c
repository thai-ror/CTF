char *__cdecl READFILE(char *filename)
{
  FILE *f; // ST3C_4@1
  __int32 fsize; // ST38_4@1
  char *RESULT; // ST34_4@1

  f = fopen(filename, "rb");
  fseek(f, 0, 2);
  fsize = ftell(f);
  fseek(f, 0, 0);
  RESULT = (char *)malloc(fsize + 1);
  fread(RESULT, fsize, 1u, f);
  fclose(f);
  return RESULT;
}

//----- (080488A0) --------------------------------------------------------
void __cdecl choose(int **n)
{
  char c; // [sp+Fh] [bp-9h]@3
  int i; // [sp+10h] [bp-8h]@1

  i = 0;
  printf("Please choose winning numbers [1-9a-f] (type 0 if you're done)\n");
  while ( i < 256 )
  {
    c = getchar();
    if ( c == 48 )
      break;
    n[c] = (int *)((char *)n[c] + 1);
    ++i;
  }
}

//----- (08048920) --------------------------------------------------------
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax@1
  const char *v4; // eax@1
  unsigned int v5; // ST2C_4@3
  int result; // eax@4
  unsigned int point; // [sp+74h] [bp-434h]@1
  int numbers[256]; // [sp+78h] [bp-430h]@1
  int i; // [sp+478h] [bp-30h]@1
  int v10; // [sp+47Ch] [bp-2Ch]@1
  char s[22]; // [sp+482h] [bp-26h]@1
  int v12; // [sp+498h] [bp-10h]@1

  v12 = *MK_FP(__GS__, 20);
  v10 = 0;
  memset(numbers, 0, 0x400u);
  point = 0;
  memcpy(s, "123456789ABCDEFabcdef", 0x16u);
  alarm(0x1Eu);
  v3 = time(0);
  srand(v3);
  setvbuf(stdout, 0, 2, 0);
  v4 = READFILE("/home/winner/intro.txt");
  puts(v4);
  choose((int **)numbers);
  printf("Thank you! Let's see the winning numbers...\n");
  sleep(3u);
  puts(".");
  for ( i = 0; i < 4; ++i )
  {
    v5 = rand();
    point += numbers[s[v5 % strlen(s)]] << 10;
  }
  printf("You won: $%d\n", point);
  result = v10;
  if ( *MK_FP(__GS__, 20) == v12 )
    result = v10;
  return result;
}

