# 1,2,5,10 dollar note, how many ways to construct 80 dollars?
# You can use each note infinitely times

def changes(m, A):
	dp=[[0]*(m+1) for j in range(len(A)+1)]
	dp[0][0]=1
	for i in range(len(A)):
		for j in range(m+1):
			dp[i+1][j]=dp[i][j]
			if j>=A[i]:
				dp[i+1][j]+=dp[i+1][j-A[i]]   # Here it is very important!
		# print i, dp[i]		
	return dp[len(A)][m]


def backPack(m,A):
	dp=[0]*(m+1)
	dp[0]=1
	for a in A:
		for i in range(a,m+1):
			dp[i]+=dp[i-a]
		# print dp
	return dp[m]

# leetcode 377
# which looks like a bp problem, but actually not!
# Given an integer array with all positive numbers and no duplicates, 
# find the number of possible combinations that add up to a positive integer target.
# nums = [1, 2, 3]
# target = 4
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)



def BP(m, A):
	dp = [0]*(m+1)
	A.sort()
	dp[0]=1
	for i in range(m+1):
		for j in range(len(A)):
			if A[j]<=i:
				dp[i]+=dp[i-A[j]]
		# print dp
	return dp[m]


## Try to split an arry equally
# [1,24,5,6] => [1,5,6],[24]

def split(arr):
	t = sum(arr)/2
	dp = [[False]*(t+1) for _ in range(len(arr)+1)]
	dp[0][0]=True
	for i in range(len(arr)):
		for j in range(t+1):
			 dp[i+1][j]=dp[i][j]
			 if j>=arr[i] and dp[i][j-arr[i]]:
			 	dp[i+1][j]=True
	for i in range(t,-1,-1):
		if dp[len(arr)][i]:
			return i





def main():
	m=80
	A=[1,2,5,10]
	# m=8
	# A=[1,2,5,10]
	# m=4
	# A=[1,2,3]
	print changes(m,A)
	print backPack(m,A)
	print BP(m,A)

	arr = [1,24,5,6] 
	print(split(arr))



if __name__ == '__main__':
	main()