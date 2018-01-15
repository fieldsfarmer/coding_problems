#include<iostream>
#include<list>
#include<vector>
#include<algorithm>
using namespace std;

void qs(vector<int>& v, int l, int r){
  if(l>=r) return;
  int pivot = l;
  int pv = v[l];
  int left = l, right = r;
  while(left<=right){
    while(left<=right && v[left]<pv) left++;
    while(left<=right && v[right]>pv) right--;
    if(left<=right){
      swap(v[left],v[right]);
      left++;
      right--;
    }
  }
  qs(v, l, right);
  qs(v, left, r);
}

void quickSort(vector<int>& v){
  int L = v.size();
  qs(v, 0, L-1);
}

int main() {
  vector<int> v = {5,4,3,2,1};
  quickSort(v);
  for(auto i : v)
    cout << i << endl;

  return 0;
}
