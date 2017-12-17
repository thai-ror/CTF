
int menu()
{
  puts("---------------------------");
  puts("1. echo server");
  puts("2. store memo");
  puts("3. show memo");
  puts("4. edit memo");
  puts("5. exit");
  puts("---------------------------");
  return puts("Your choice:");
}

//----- (0000555555554AC7) ----------------------------------------------------
int read_int()
{
  char nptr; // [rsp+0h] [rbp-20h]
  unsigned __int64 v2; // [rsp+18h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  if ( (signed int)_read_chk(0LL, &nptr, 15LL, 16LL) <= 0 )
  {
    puts("read error");
    exit(1);
  }
  return atoi(&nptr);
}
// 5555555548C8: using guessed type __int64 __fastcall _read_chk(_QWORD, _QWORD, _QWORD, _QWORD);

//----- (0000555555554B3A) ----------------------------------------------------
unsigned __int64 echo()
{
  char buf; // [rsp+0h] [rbp-80h]
  unsigned __int64 v2; // [rsp+78h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  printf("What do you want to say:");
  read(0, &buf, 112uLL);
  printf("You said: %s\n", &buf);
  return __readfsqword(0x28u) ^ v2;
}

//----- (0000555555554BAC) ----------------------------------------------------
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char *v3; // rsi
  unsigned int nbytes; // [rsp+Ch] [rbp-54h]
  signed int nbytes_4; // [rsp+10h] [rbp-50h]
  signed int v7; // [rsp+14h] [rbp-4Ch]
  unsigned int v8; // [rsp+18h] [rbp-48h]
  int v9; // [rsp+1Ch] [rbp-44h]
  int v10; // [rsp+1Ch] [rbp-44h]
  int v11; // [rsp+1Ch] [rbp-44h]
  char s[56]; // [rsp+20h] [rbp-40h]
  unsigned __int64 v13; // [rsp+58h] [rbp-8h]
  __int64 savedregs; // [rsp+60h] [rbp+0h]

  v13 = __readfsqword(0x28u);
  setvbuf(_bss_start, 0LL, 2, 0LL);
  setvbuf(stdin, 0LL, 2, 0LL);
  puts("Memo manager");
  v3 = 0LL;
  memset(s, 0, 48uLL);
  for ( nbytes = 16; ; printf("done! new size : %d\n", nbytes) )
  {
    while ( 2 )
    {
      menu();
      v8 = read_int();
      switch ( (unsigned int)&savedregs )
      {
        case 1u:
          echo();
          continue;
        case 2u:
          printf("Which one do you want to store in (1 , 2 , 3)?:", v3);
          v9 = read_int();
          if ( v9 <= 0 || v9 > 3 )
          {
            puts("Nop!");
            exit(0);
          }
          printf("What do you want to store in mem page %d :", (unsigned int)v9);
          v3 = &s[16 * (v9 - 1)];
          read(0, v3, 16uLL);
          nbytes_4 = 9;
          while ( 2 )
          {
            if ( nbytes_4 >= 0 )
            {
              if ( *((_BYTE *)&savedregs + 16 * (v9 - 1) + nbytes_4 - 64) != 10 )
              {
                --nbytes_4;
                continue;
              }
              *((_BYTE *)&savedregs + 16 * (v9 - 1) + nbytes_4 - 64) = 0;
            }
            break;
          }
          puts("done!");
          continue;
        case 3u:
          printf("Which memo page do you want to see (1 , 2 , 3)?:", v3);
          v10 = read_int();
          if ( v10 <= 0 || v10 > 3 )
          {
            puts("Nop!");
            exit(0);
          }
          if ( s[16 * (v10 - 1)] )
          {
            v3 = (char *)v8;
            printf("memo page %d : %s\n", v8, &s[16 * (v10 - 1)]);
          }
          else
          {
            puts("There is nothing in this memo page, please store something first.");
          }
          continue;
        case 4u:
          printf("Which memo page do you want to edit (1 , 2 , 3)?:", v3);
          v11 = read_int();
          if ( v11 <= 0 || v11 > 3 )
          {
            puts("Nop!");
            exit(0);
          }
          if ( !s[16 * (v11 - 1)] )
          {
            puts("There is nothing in this memo page, please store something first.");
            continue;
          }
          printf("Edit memo page %d :", v8);
          read(0, &s[16 * (v11 - 1)], nbytes);
          v7 = 9;
          break;
        case 5u:
          puts("Bye!");
          return 0;
        default:
          puts("Invalid choice!");
          continue;
      }
      break;
    }
    while ( v7 >= 0 )
    {
      if ( *((_BYTE *)&savedregs + 16 * (v11 - 1) + v7 - 64) == 10 )
      {
        *((_BYTE *)&savedregs + 16 * (v11 - 1) + v7 - 64) = 0;
        break;
      }
      --v7;
    }
    nbytes = strlen(&s[16 * (v11 - 1)]);
    if ( (signed int)nbytes > 54 )
    {
      puts("Too long!");
      exit(0);
    }
    v3 = (char *)nbytes;
  }
}


