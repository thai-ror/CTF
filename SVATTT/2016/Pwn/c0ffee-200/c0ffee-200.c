#include <stdio.h>
#include <string.h>

int  main()
{
  unsigned int v0; // eax@1
  const char *v1; // eax@1
  ssize_t v2; // eax@10
  char nptr; // [sp+78h] [bp-550h]@2
  unsigned int count; // [sp+80h] [bp-548h]@1
  unsigned int v6; // [sp+84h] [bp-544h]@1
  unsigned int i; // [sp+88h] [bp-540h]@1
  void *s; // [sp+8Ch] [bp-53Ch]@1
  char buff[1320]; // [sp+90h] [bp-538h]@1
  unsigned int limit; // [sp+5B8h] [bp-10h]@1
  int v11; // [sp+5BCh] [bp-Ch]@1

  v11 = 0;
  v0 = time(0);
  srand(v0);
  //alarm(30u);
  limit = rand() % 6 + 5;
  s = buff;
  i = 0;
  v6 = 0;
  count = 0;
  setvbuf(stdout, 0, 2, 0);

  printf("Hi sir! Welcome to 0xC0FFEE SHOP v1.1\n");
  while ( 1 )
  {
    printf("How many cups, sir?\ncups> ");
    scanf("%08s%*c", &nptr);
    printf("%08s", &nptr);
    v6 = atoi(&nptr);
    //printf("v6 %d\n", v6);
    if ( v6 <= limit )
      break;
    printf("No way, sir. There is a long queue, please take %d cups at once. Thank you for your understanding.\n", limit);
  }
  do
  {
    if ( count >= limit )
      break;


  puts("+------------- MENU -------------+");
  puts("| 1. Black Coffee                |");
  puts("| 2. Milk Coffee                 |");
  puts("| 3. Jelly Freeze                |");
  puts("| 4. Cake                        |");
  puts("| 5. Water                       |");



    printf("what is your name, sir? then I can write it on the cup.\nsize> ");
    scanf("%08s%*c", &nptr);
    v6 = atoi(&nptr);
    if ( !v6 || v6 > 128 )
    {
      puts("Sorry sir, what's wrong with your name?! are you trying to hack us? I'm calling police now.");
      exit(-1);
    }
    memset(s, 0, 128u);
    for ( i = 0; i < v6; i += v2 )
      v2 = read(0, (char *)s + i, v6 - i);
    *((char *)s + i) = 0;
    printf("Which one, sir?\n>> ");
    scanf("%08s%*c", &nptr);
    v6 = atoi(&nptr);
    *((int *)s + 32) = v6;
    ++count;
    s = (char *)s + 132;
    printf("anything else, sir?\n> ");
    scanf("%08s%*c", &nptr);
  }
  while ( !strcmp(&nptr, "yes") );
  puts("Thank you so much, sir!\n...bling bling $$$\n...ching ching $$$\n\nHere is your receipt: ");
  for ( i = 0; i < count; ++i )
    printf("%16s | %03d\n", &buff[132 * i], *(int *)&buff[132 * i + 128]);
  return v11;
}
