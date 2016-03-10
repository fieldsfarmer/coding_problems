#include <iostream>
using namespace std;

template<typename T, unsigned S>
inline unsigned getsize(const T (&v)[S]){return S;}

int maxSubarraySum(int a[], int n){
	if(n == 0) return 0;
	int res = a[0];
	int max_here = a[0];
	for (int i = 1; i < n; ++i)
	{
		max_here = max(a[i], a[i]+max_here);
		res = max(res, max_here);
	}
	return res;
}

int main(){
	int a1[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
	cout << "test 1" << endl;
	cout << maxSubarraySum(a1, getsize(a1)) << endl;

	int a2[] = {-10, -9, -1, -8, -2};
	cout << "test 2" << endl;
	cout << maxSubarraySum(a2, getsize(a2)) << endl;


	return 0;
}