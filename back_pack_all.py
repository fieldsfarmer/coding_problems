# Given n items with size A[i], an integer m denotes the size of a backpack. 
# How full you can fill this backpack?
# each item can only be used for once
def back_pack_1(m,A):
	dp = [[False]*(m+1) for _ in range(len(A)+1)]
	dp[0][0]=True
	for i in range(len(A)):
		for j in range(m+1):
			dp[i+1][j]=dp[i][j]
			if j>=A[i] and dp[i][j-A[i]]:
				dp[i+1][j]=True
	res = 0
	for i in range(m,-1,-1):
		if dp[len(A)][i]:
			return i
	return res

# Following the above, but item can be used for infinite times
def back_pack_2(m,A):
	dp = [[False]*(m+1) for _ in range(len(A)+1)]
	dp[0][0]=True
	for i in range(len(A)):
		for j in range(m+1):
			dp[i+1][j]=dp[i][j]
			if j>=A[i] and dp[i+1][j-A[i]]:
				dp[i+1][j]=True
	res = 0
	for i in range(m,-1,-1):
		if dp[len(A)][i]:
			return i
	return res

def back_pack_2_1(m,A):
	dp=[False]*(m+1)
	dp[0]=True
	for i in range(len(A)):
		for j in range(m+1):
			if j>=A[i] and dp[j-A[i]]:
				dp[j]=True
	res = 0
	for i in range(m,-1,-1):
		if dp[i]:
			return i
	return res
#########################################################
# Given n items with size Ai and value Vi, and a backpack with size m. 
# What's the maximum value can you put into the backpack?
def back_pack_3(m,A,V):
	dp = [[0]*(m+1) for _ in range(len(A)+1)]
	for i in range(len(A)):
		for j in range(m+1):
			dp[i+1][j]=dp[i][j]
			if j>=A[i]:
				dp[i+1][j]=max(dp[i+1][j], dp[i][j-A[i]]+V[i])
	return dp[len(A)][m]

# Following the above, but infinite times
def back_pack_4(m,A,V):
	dp = [0]*(m+1)
	for i in range(len(A)):
		for j in range(m+1):
			if j>=A[i]:
				dp[j]=max(dp[j],dp[j-A[i]]+V[i])
	return dp[m]

#########################################################
# Given n items with size A[i] which an integer array and all positive numbers, 
# no duplicates. An integer m denotes the size of a backpack. 
# Find the number of possible fill the backpack.
def back_pack_5(m, A):
	dp=[[0]*(m+1) for _ in range(len(A)+1)]
	dp[0][0]=1
	for i in range(len(A)):
		for j in range(m+1):
			dp[i+1][j]=dp[i][j]
			if j>=A[i]:
				dp[i+1][j]+=dp[i][j-A[i]]
	return dp[len(A)][m]

# Follow up: each item may be chosen unlimited number of times
def back_pack_6(m, A):
	dp=[[0]*(m+1) for _ in range(len(A)+1)]
	dp[0][0]=1
	for i in range(len(A)):
		for j in range(m+1):
			dp[i+1][j]=dp[i][j]
			if j>=A[i]:
				dp[i+1][j]+=dp[i+1][j-A[i]]
	return dp[len(A)][m]

def back_pack_6_1(m,A):
	dp=[0]*(m+1)
	dp[0]=1
	for i in range(len(A)):
		for j in range(m+1):
			if j>=A[i]:
				dp[j]+=dp[j-A[i]]
	return dp[m]

#########################################################
# Given an array nums with all positive numbers and no duplicates, 
# find the number of possible combinations that add up to a positive integer target.
# Given A = [1, 2, 4], m = 4
# # The possible combination ways are:
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# [4]

def back_pack_7(m, A):
	dp=[0]*(m+1)
	dp[0]=1
	for i in range(m+1):
		for j in range(len(A)):
			if i>=A[j]:
				dp[i]+=dp[i-A[j]]
	return dp[m]




def main():
	A = [2, 3, 5, 7]
	m = 11
	print back_pack_1(m,A)
	print back_pack_2(m,A)
	print back_pack_2_1(m,A)

	A = [2, 3, 5, 7]
	V = [1, 5, 2, 4]
	m = 10
	print back_pack_3(m,A,V)
	print back_pack_4(m,A,V)

	A = [1,2,3,3,7]
	m = 8
	print back_pack_5(m,A)

	A = [2,3,6,7]
	m = 7
	print back_pack_6(m,A)
	print back_pack_6_1(m,A)

	A = [1, 2, 4]
	m = 4
	print back_pack_7(m, A)

	
if __name__ == '__main__':
	main()