SVATTT 2016
binary:mrc-50

  int v2; // ST18_4@5
  unsigned int v4; // [sp+1Ch] [bp-1Ch]@1
  size_t v5; // [sp+20h] [bp-18h]@3
  const char *v6; // [sp+24h] [bp-14h]@3
  size_t i; // [sp+28h] [bp-10h]@3

  v4 = -1;
  if ( a1 < 2 )
  {
    printf("usage: %s <filename>\n", *a2);
    exit(-1);
  }
  v6 = (const char *)sub_80485C0(a2[1]);
  v5 = strlen(v6);
  for ( i = 0; i < v5; ++i )
  {
    v2 = (v4 >> 24) ^ v6[i];
    printf("%02x", (unsigned __int8)v4);
    v4 = v4 & (-(char)(v6[i] >> 7) | 0xFFFFFF00) ^ dword_804A044[v2];
  }
  printf("%08x\n", v4);
  return 0;
}


./mrc-150 flag.txt
ffc309e61f2ac3df48d3b9b64fd1720bfb95b460a1235f5d91c4f92ce90dfa516e1b8c49225b808560a9d853980662dc26984e


Flag:
SVATTT{Whats_differenc3_between_my_mrc_@nd_crc}


