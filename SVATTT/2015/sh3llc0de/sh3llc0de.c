
char shellcode[1024];
int  main(int argc, const char **argv, const char **envp)
{
  signed int i; // [esp+1Ch] [ebp-4h]

  //system("date");
printf("shellcode %08x\n",&shellcode);
  read(0, &shellcode, 1024u);
  for ( i = 0; i <= 1023; ++i )
  {
	printf("%d %02x|",i,*(unsigned char *)(i + shellcode));
    if ( *(unsigned char *)(i + shellcode) == 0xCD )
	{
		printf("%d 0xCD detect: %02x\n",i,*(unsigned char *)(i + shellcode));
		*(unsigned char *)(i + shellcode) = 0;
	}

    if ( *(unsigned char *)(i + shellcode) == 0x80)
	{
		printf("%d 0x80 detect: %02x\n",i,*(unsigned char *)(i + shellcode));
	      *(unsigned char *)(i + shellcode) = 0;	
	}

    if ( *(char *)(i + shellcode) == 0x83){
		printf("%d 0x83 detect: %02x\n",i,*(unsigned char *)(i + shellcode));
		*(char *)(i + shellcode) = 0;
	}

  }
  return ((int (*)(void))shellcode)();
}
