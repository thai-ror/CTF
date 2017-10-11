/* This file has been generated by the Hex-Rays decompiler.
   Copyright (c) 2007-2017 Hex-Rays <info@hex-rays.com>

   Detected compiler: GNU C++
*/

#include <defs.h>

#include <stdarg.h>


//-------------------------------------------------------------------------
// Function declarations

void *init_proc();
int sub_80486B0();
// int setsockopt(int fd, int level, int optname, const void *optval, socklen_t optlen);
// struct passwd *getpwnam(const char *name);
// int dup2(int fd, int fd2);
// ssize_t read(int fd, void *buf, size_t nbytes);
// void free(void *ptr);
// time_t time(time_t *timer);
// __sighandler_t signal(int sig, __sighandler_t handler);
// int chdir(const char *path);
// unsigned int alarm(unsigned int seconds);
// uint16_t htons(uint16_t hostshort);
// int setgroups(size_t n, const __gid_t *groups);
// int accept(int fd, struct sockaddr *addr, socklen_t *addr_len);
// int setgid(__gid_t gid);
// int getdtablesize(void);
// int __gmon_start__(void); weak
// void exit(int status);
// int open(const char *file, int oflag, ...);
// void srand(unsigned int seed);
// size_t strlen(const char *s);
// int vasprintf(char **, const char *, va_list);
// int bind(int fd, const struct sockaddr *addr, socklen_t len);
// int rand(void);
// __pid_t fork(void);
// uint32_t htonl(uint32_t hostlong);
// int listen(int fd, int n);
// int setuid(__uid_t uid);
// int socket(int domain, int type, int protocol);
// ssize_t recv(int fd, void *buf, size_t n, int flags);
// int close(int fd);
// ssize_t send(int fd, const void *buf, size_t n, int flags);
void sub_80488F0();
int sub_8048900();
int sub_8048970();
int sub_8048990();
int __cdecl sub_80489BC(uint16_t a1);
void __cdecl __noreturn sub_8048AF6(int fd, char *name, int); // idb
int __cdecl sub_8048B9F(char *name); // idb
int __cdecl sub_8048C25(int a1);
size_t __cdecl sub_8048CE4(int fd, char *s);
size_t sub_8048D56(int fd, char *a2, ...);
int __cdecl sub_8048DBA(int fd, void *buf, int); // idb
unsigned int __cdecl sub_8048E1C(int fd, int a2, int a3, int a4);
signed int __cdecl sub_8048EA0(unsigned __int8 *a1);
int __cdecl sub_8048EF6(int a1);
void __cdecl __noreturn main();
void init(void); // idb
void term_proc();
// int vasprintf(char **, const char *, va_list);

//-------------------------------------------------------------------------
// Data declarations

int (*off_804AF08[2])() = { &sub_8048990, &sub_8048970 }; // weak
int (*off_804AF0C)() = &sub_8048970; // weak
int (*dword_804B008)(void) = NULL; // weak
char *name = "crackme"; // idb
char byte_804B098; // weak
_UNKNOWN unk_804B09B; // weak
// extern _UNKNOWN _gmon_start__; weak


//----- (08048688) --------------------------------------------------------
void *init_proc()
{
  void *result; // eax

  result = &_gmon_start__;
  if ( &_gmon_start__ )
    result = (void *)__gmon_start__();
  return result;
}
// 80487B0: using guessed type int __gmon_start__(void);

//----- (080486B0) --------------------------------------------------------
int sub_80486B0()
{
  return dword_804B008();
}
// 804B008: using guessed type int (*dword_804B008)(void);

//----- (080488C0) --------------------------------------------------------
#error "80488C3: positive sp value has been found (funcsize=2)"

//----- (080488F0) --------------------------------------------------------
void sub_80488F0()
{
  ;
}

//----- (08048900) --------------------------------------------------------
int sub_8048900()
{
  int result; // eax

  result = &unk_804B09B - (_UNKNOWN *)&byte_804B098;
  if ( (unsigned int)(&unk_804B09B - (_UNKNOWN *)&byte_804B098) > 6 )
    result = 0;
  return result;
}
// 8048900: could not find valid save-restore pair for ebp
// 804B098: using guessed type char byte_804B098;

//----- (08048970) --------------------------------------------------------
int sub_8048970()
{
  int result; // eax

  if ( !byte_804B098 )
  {
    result = sub_8048900();
    byte_804B098 = 1;
  }
  return result;
}
// 8048970: could not find valid save-restore pair for ebp
// 804B098: using guessed type char byte_804B098;

//----- (08048990) --------------------------------------------------------
int sub_8048990()
{
  return 0;
}
// 8048990: could not find valid save-restore pair for ebp

//----- (080489BC) --------------------------------------------------------
int __cdecl sub_80489BC(uint16_t a1)
{
  int optval; // [esp+34h] [ebp-24h]
  int fd; // [esp+38h] [ebp-20h]
  struct sockaddr addr; // [esp+3Ch] [ebp-1Ch]
  unsigned int v5; // [esp+4Ch] [ebp-Ch]

  v5 = __readgsdword(0x14u);
  optval = 1;
  addr.sa_family = 2;
  *(_WORD *)addr.sa_data = htons(a1);
  *(_DWORD *)&addr.sa_data[2] = htonl(0);
  if ( signal(17, (__sighandler_t)1) == (__sighandler_t)-1 )
    exit(-1);
  fd = socket(2, 1, 6);
  if ( fd == -1 )
    exit(-1);
  if ( setsockopt(fd, 1, 2, &optval, 4u) == -1 )
    exit(-1);
  if ( bind(fd, &addr, 0x10u) == -1 )
    exit(-1);
  if ( listen(fd, 16) == -1 )
    exit(-1);
  return fd;
}

//----- (08048AF6) --------------------------------------------------------
void __cdecl __noreturn sub_8048AF6(int fd, char *name, int a3)
{
  int v3; // [esp+14h] [ebp-14h]
  int v4; // [esp+14h] [ebp-14h]
  __pid_t v5; // [esp+18h] [ebp-10h]
  int status; // [esp+1Ch] [ebp-Ch]

  while ( 1 )
  {
    do
    {
      do
        v3 = accept(fd, 0, 0);
      while ( v3 == -1 );
      v4 = sub_8048C25(v3);
      v5 = fork();
    }
    while ( v5 == -1 );
    if ( !v5 )
    {
      sub_8048B9F(name);
      close(fd);
      alarm(0x10u);
      status = ((int (__cdecl *)(int))a3)(v4);
      close(v4);
      exit(status);
    }
    close(v4);
  }
}

//----- (08048B9F) --------------------------------------------------------
int __cdecl sub_8048B9F(char *name)
{
  int result; // eax
  struct passwd *v2; // [esp+1Ch] [ebp-Ch]

  v2 = getpwnam(name);
  if ( !v2 )
    exit(-1);
  if ( setgroups(0, 0) == -1
    || setgid(v2->pw_gid) == -1
    || setuid(v2->pw_uid) == -1
    || (result = chdir(v2->pw_dir), result == -1) )
  {
    exit(-1);
  }
  return result;
}

//----- (08048C25) --------------------------------------------------------
int __cdecl sub_8048C25(int a1)
{
  int buf; // [esp+14h] [ebp-14h]
  int v3; // [esp+18h] [ebp-10h]
  int fd; // [esp+1Ch] [ebp-Ch]

  v3 = getdtablesize();
  fd = open("/dev/urandom", 0);
  buf = 0;
  if ( fd >= 0 )
  {
    while ( buf < a1 )
    {
      read(fd, &buf, 2u);
      buf %= v3;
    }
    close(fd);
  }
  else
  {
    while ( buf < a1 )
      buf = rand() % v3;
  }
  if ( dup2(a1, buf) == -1 )
    return a1;
  close(a1);
  return buf;
}

//----- (08048CE4) --------------------------------------------------------
size_t __cdecl sub_8048CE4(int fd, char *s)
{
  size_t i; // [esp+14h] [ebp-14h]
  size_t v4; // [esp+18h] [ebp-10h]
  ssize_t v5; // [esp+1Ch] [ebp-Ch]

  v4 = strlen(s);
  for ( i = 0; i < v4; i += v5 )
  {
    v5 = send(fd, &s[i], v4 - i, 0);
    if ( v5 <= 0 )
      return -1;
  }
  return i;
}

//----- (08048D56) --------------------------------------------------------
size_t sub_8048D56(int fd, char *a2, ...)
{
  char *s; // [esp+18h] [ebp-10h]
  size_t v4; // [esp+1Ch] [ebp-Ch]
  va_list va; // [esp+38h] [ebp+10h]

  va_start(va, a2);
  s = 0;
  v4 = 0;
  v4 = vasprintf(&s, a2, va);
  if ( v4 != -1 )
    v4 = sub_8048CE4(fd, s);
  free(s);
  return v4;
}

//----- (08048DBA) --------------------------------------------------------
int __cdecl sub_8048DBA(int fd, void *buf, int a3)
{
  int n; // [esp+18h] [ebp-10h]
  ssize_t v5; // [esp+1Ch] [ebp-Ch]

  n = a3;
  if ( a3 )
  {
    while ( n > 0 )
    {
      v5 = recv(fd, buf, n, 0);
      if ( v5 == -1 )
        break;
      n -= v5;
    }
  }
  return a3 - n;
}

//----- (08048E1C) --------------------------------------------------------
unsigned int __cdecl sub_8048E1C(int fd, int a2, int a3, int a4)
{
  char buf; // [esp+27h] [ebp-11h]
  unsigned int i; // [esp+28h] [ebp-10h]
  ssize_t v7; // [esp+2Ch] [ebp-Ch]

  v7 = 0;
  i = 0;
  if ( a3 )
  {
    for ( i = 0; i < a3; ++i )
    {
      v7 = recv(fd, &buf, 1u, 0);
      if ( v7 == -1 )
        break;
      *(_BYTE *)(i + a2) = buf;
      if ( buf == (_BYTE)a4 )
        break;
    }
  }
  return i;
}

//----- (08048EA0) --------------------------------------------------------
signed int __cdecl sub_8048EA0(unsigned __int8 *a1)
{
  int v1; // ST0C_4
  unsigned __int8 v3; // [esp+3h] [ebp-Dh]
  signed int v4; // [esp+4h] [ebp-Ch]
  unsigned __int8 *v5; // [esp+8h] [ebp-8h]

  v3 = *a1;
  v4 = 1337;
  if ( *a1 )
  {
    v5 = a1;
    do
    {
      v1 = 32 * v4 + v3;
      v3 = (v5++)[1];
      v4 += v1;
    }
    while ( v3 );
  }
  return v4;
}

//----- (08048EF6) --------------------------------------------------------
int __cdecl sub_8048EF6(int a1)
{
  int fd; // ST18_4
  unsigned int v3; // [esp+14h] [ebp-214h]
  _BYTE v4[256]; // [esp+1Ch] [ebp-20Ch]
  char buf[256]; // [esp+11Ch] [ebp-10Ch]
  unsigned int v6; // [esp+21Ch] [ebp-Ch]

  v6 = __readgsdword(0x14u);
  sub_8048CE4(a1, "Enter registration code: ");
  v3 = sub_8048E1C(a1, (int)v4, 255, 10);
  if ( v3 == -1 )
    return 0;
  v4[v3] = 0;
  if ( sub_8048EA0(v4) == 0xEF2E3558 )
  {
    sub_8048CE4(a1, "Thank you, valued customer!\n");
    fd = open("key", 0);
    buf[read(fd, buf, 0x40u)] = 0;
    sub_8048D56(a1, "Your key is: %s\n", buf);
  }
  else
  {
    sub_8048D56(a1, "Invalid registration code.\n");
  }
  return 0;
}
// 8048EF6: using guessed type char buf[256];

//----- (08049036) --------------------------------------------------------
void __cdecl __noreturn main()
{
  unsigned int v0; // eax
  int v1; // eax

  v0 = time(0);
  srand(v0);
  v1 = sub_80489BC(0xD431u);
  sub_8048AF6(v1, name, (int)sub_8048EF6);
}

//----- (08049090) --------------------------------------------------------
void init(void)
{
  int v0; // edi
  int v1; // esi

  v0 = 0;
  init_proc();
  v1 = &off_804AF0C - off_804AF08;
  if ( v1 )
  {
    do
      off_804AF08[v0++]();
    while ( v0 != v1 );
  }
}
// 804AF08: using guessed type int (*off_804AF08[2])();
// 804AF0C: using guessed type int (*off_804AF0C)();

//----- (08049104) --------------------------------------------------------
void term_proc()
{
  ;
}

#error "There were 1 decompilation failure(s) on 20 function(s)"
