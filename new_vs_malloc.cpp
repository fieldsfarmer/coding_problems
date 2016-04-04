#include <iostream>
using namespace std;

int main(){
	int *a = new (nothrow) int[10];
	if(a == NULL){
		cout << "something wrong happens!" << endl;
		return 1;
	}
	for(int i=0; i<10; i++){
		a[i] = i;
		cout << a[i] << " ";
	}
	cout << endl;
	delete[] a;
	return 0;
}