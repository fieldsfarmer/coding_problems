#include <vector>
#include <iostream>
// #include <climits>
#include <vector>

using namespace std;

// not very good
#define GETSIZE(array) (sizeof((array))/sizeof((array[0])))

// better see: http://www.cplusplus.com/forum/general/33669/
template <typename T, unsigned S>
inline unsigned getsize(const T (&v)[S]){return S;}

// result ensure to be at least 1;
int maxSubarrayProduct(int a[], int n){
	int max_here = 1;
	int min_here = 1;
	int res = 1;
	int i;
	for(i=0; i<n; ++i){
		if(a[i]>0){
			max_here *= a[i];
			min_here = min(1, min_here*a[i]);
		}
		else if(a[i]==0){
			max_here = 1;
			min_here = 1;
		}
		else{
			int tmp = max_here;
			max_here = max(min_here*a[i], 1);
			min_here = tmp * a[i];
		}
		res = max_here > res? max_here : res;	
	}
	return res;
}

// result ensured to be at least the largest element in the array;
int maxSubarrayProduct_1(int a[], int n){
	if(n==0) return 0;
	int max_here = a[0];
	int min_here = a[0];
	int res = a[0];
	for(int i=1; i<n; ++i){
		int tmp = max_here;
		max_here = max(a[i], max(min_here*a[i], max_here*a[i]));
		min_here = min(a[i], min(tmp*a[i], min_here*a[i]));
		res = max_here > res? max_here : res;
	}
	return res;
}


int main(){
	// int a1[] = {6, -3, -10, 0, 2};
	// int a1[] = {0, -1, 0, -2};   // should be 0; 
	int a1[] = {-2};
	int a2[] = {-1, -3, -10, 0, 60};
	int a3[] = {-2, -3, 0, -2, -40};
	cout << "test 1" << endl;
 	// cout << maxSubarrayProduct(a1, GETSIZE(a1)) << endl;
 	cout << maxSubarrayProduct(a1, getsize(a1)) << endl;
 	// cout << maxSubarrayProduct_1(a1, GETSIZE(a1)) << endl;
 	cout << maxSubarrayProduct_1(a1, getsize(a1)) << endl;

	cout << "test 2" << endl;
	cout << maxSubarrayProduct(a2, GETSIZE(a2)) << endl;
 	cout << maxSubarrayProduct_1(a2, GETSIZE(a2)) << endl;

 	cout << "test 3" << endl;
	cout << maxSubarrayProduct(a3, GETSIZE(a3)) << endl;
	cout << maxSubarrayProduct_1(a3, GETSIZE(a3)) << endl;

	// test for getsize
	// vector<int> v(5, 0);
	// cout << "test for getsize" << endl;
	// cout << getsize(v) << endl;
	return 0;

}