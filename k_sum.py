'''
Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

Given [1,2,3,4], k = 2, target = 5.
There are 2 solutions: [1,4] and [2,3]. Return 2.
'''
class Solution():
	def kSum(self, A, k, target):
		dp = [[[0]*(target+1) for _ in range(k+1)] for _ in range(len(A)+1)]
		dp[0][0][0] = 1
		for I in range(len(A)):
			for J in range(k+1):
				for K in range(target+1):
					dp[I+1][J][K] = dp[I][J][K]
					if A[I]<=K and J-1>=0:
						dp[I+1][J][K] += dp[I][J-1][K-A[I]]
		return dp[len(A)][k][target]