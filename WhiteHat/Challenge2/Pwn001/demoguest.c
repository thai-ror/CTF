#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
  int i;
  srand(time(NULL) + 4);
  for (i = 0; i < 3; i++) {
    printf("%d\n", rand()%100+1);
  }
  return 0;
}
