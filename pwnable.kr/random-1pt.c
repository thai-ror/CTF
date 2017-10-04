#include <stdio.h>

int main(){
	unsigned int random;
	random = rand();	// random value!
	printf("\nrandom addr %x %d", &random,random);
	unsigned int key=0;
	scanf("%d", &key);


	printf("\nkey addr %x %d", &key,key);

	if( (key ^ random) == 0xdeadbeef ){
		printf("Good!\n");
		system("/bin/cat flag");
		return 0;
	}

	printf("\nWrong, maybe you should try 2^32 cases.\n");
	return 0;
}
