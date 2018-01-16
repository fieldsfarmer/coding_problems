#include <iostream>
#include <vector>
using namespace std;

// it also move smaller elements before the pivot and larger ones after 
// it return the index of the pivot

int partition(vector<int>& nums, int left, int right){
    int pivot = nums[right];
    int index = left - 1;
    for(int i = left; i < right; i++){
        if(nums[i] <= pivot){                    //// if for kth_larger change '<=' to '>'
            index++;
            swap(nums[i], nums[index]);
        }
    }
    swap(nums[index + 1], nums[right]);
    return index + 1;
}

int kth_smaller(vector<int>& nums, int k){
  int lo=0, hi=nums.size()-1;
  while(lo<=hi){
    int idx=partition(nums, lo, hi);
    if(idx == k-1){
      return nums[idx];
    }
    if(idx < k-1){
      lo = idx+1;
    } else {
      hi = idx-1;
    }
  }
  return -1;
}

void quick_sort(vector<int>& nums, int l, int r){
  if(l>=r) return;
  int k = partition(nums, l, r);
  quick_sort(nums,l,k-1);
  quick_sort(nums,k+1,r);
}
