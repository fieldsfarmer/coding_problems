'''
Given n items with size Ai and value Vi, and a backpack with size m. 
What's the maximum value can you put into the backpack?
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], 
and a backpack with size 10. The maximum value is 9.
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        l = len(A)
        dp = [[0]*(m+1) for _ in range(l+1)]
        ### dp[i][j] is the maxvalue for items in A[:i] and maximum size of j
        for i in range(l):
            for j in range(m+1):
                if i==0 or j==0: dp[i][j] = 0
                if A[i]>j:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = max(dp[i][j], dp[i][j-A[i]]+V[i])
        return dp[l][m]
