
### This one returns the longest subset that the difference of its smallest
### and largest is less than diff
### 
def solution(arr, diff):
	if not arr:
		return []
	if diff == 0:
		return [a[0]]
	arr.sort()
	maxL = 0
	res = None
	for i in range(len(arr)):
		right = helper(arr, i, len(arr)-1, arr[i]+diff) 
		if right - i + 1 > maxL:
			maxL = right - i + 1
			res = arr[i:right+1]
	return res

### It returns the largest number in arr between index left and
### index right that is <= k
def helper(arr, left, right, k):
	if left>right or arr[left] > k:
		return -1
	if arr[right] <= k:
		return right
	l,r=left, right
	res = -1
	while l<=r:
		m = l+(r-l)/2
		if arr[m]<=k:
			res = m
			t = helper(arr,m+1,right,k)
			if t<0:
				return res
			else:
				return t
		else:
			r = m-1
	return res

### This one returns the longest subset such that after sort,
### the distance between neighbor are less than diff
def largest_subset_interval(arr, interval):
	if not arr: return []
	if len(arr)==1: return arr
	maxL = 0
	res = []
	l,r=0,0
	while r<len(arr)-1:
		if arr[r+1]-arr[r]<=interval:
			r += 1
		else:
			if r-l+1>maxL:
				maxL = r-l+1
				res = arr[l:r+1]
			l = r+1
			r = r+1
	return res



def main():
	arr = [0,1,2,3,3,3,4,5]
	print(helper(arr, 0, len(arr)-1, 3))
	# ([4, 3, 0, 15, 21], 1) => [3, 4]
	arr = [4, 3, 0, 15, 21]
	print(solution(arr, 1))

	print(largest_subset_interval(arr, 1))


if __name__ == '__main__':
	main()