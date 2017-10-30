#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv) {
        char *p, *q;

        p = malloc(16);
        q = malloc(16);
        if (argc >= 2)
                strcpy(p, argv[1]);
        free(q);
        free(p);
        return 0;
}
