#include <vector>
#include <iostream>
#include <climits>
using namespace std;

// not very good
#define GETSIZE(array) (sizeof((array))/sizeof((array[0])))

int maxSubarrayProduct(int a[], int n){
	// int * dp = new int[n]; 

	// for(int i=0; i<n; ++i){
	// 	dp[i] = INT_MIN;
	// }
	// delete[] dp;

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



int main(){
	int a1[] = {6, -3, -10, 0, 2};
	int a2[] = {-1, -3, -10, 0, 60};
	int a3[] = {-2, -3, 0, -2, -40};
	cout << maxSubarrayProduct(a1, GETSIZE(a1)) << endl;
	cout << maxSubarrayProduct(a2, GETSIZE(a2)) << endl;
	cout << maxSubarrayProduct(a3, GETSIZE(a3)) << endl;
	return 0;
}