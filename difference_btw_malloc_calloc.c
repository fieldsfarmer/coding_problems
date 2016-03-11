#include <stdio.h>
#include <stdlib.h>
int main(){
	int sz = 5;
	int * m_array = (int *)malloc(sz * sizeof(int));
	int * c_array = (int *)calloc(sz, sizeof(int));
	int i;
	for(i=0; i<sz; ++i){
		printf("%d\n", *(m_array+i)); // you won't know what to print out
	}
	for(i=0; i<sz; ++i){
		printf("%d\n", *(c_array+i)); // would be all 0
	}
	return 0;
}