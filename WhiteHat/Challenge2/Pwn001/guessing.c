#include <stdio.h>
#include <time.h>

//----- (0804863D) --------------------------------------------------------
int  main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  signed int i; // [esp+18h] [ebp-18h]
  signed int j; // [esp+18h] [ebp-18h]
  signed int k; // [esp+18h] [ebp-18h]
  int v8; // [esp+1Ch] [ebp-14h]
  int v9; // [esp+20h] [ebp-10h]
  int v10; // [esp+2Ch] [ebp-4h]

  setvbuf(stdout, 0, 2, 0);
  v8 = 0;
  puts("-------- Guessing Game --------");
  puts("You must guess 3 random number in range 1-100 to win the game!");
  printf("Let's start");
  for ( i = 0; i <= 2; ++i )
  {
    putchar(46);
    sleep(1u);
  }
  v3 = time(0);
  srand(v3);
  for ( j = 0; j <= 2; ++j )
    *(&v9 + j) = rand() % 100 + 1;
  puts(&byte_80488DB);
  for ( k = 0; k <= 2; ++k )
  {
    printf("Round %d: ", k + 1);
    __isoc99_scanf("%s", &v10);
    if ( atoi((const char *)&v10) == *(&v9 + k) )
      ++v8;
  }
  if ( v8 != 3 )
    return printf(":(. You just win %d/3 game. Good bye!\n", v8);
  printf("Congrast! You win the game ");
  return flag();
}

//----- (080487C5) --------------------------------------------------------
int flag()
{
  return system("/bin/cat flag.txt");
}

