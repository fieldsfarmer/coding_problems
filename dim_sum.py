class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        
        K = 6*n+1
        dp = [[0]*K for _ in range(n+1)]
        for k in range(1,7):
            dp[1][k] = 1.0/6
        for i in range(2,n+1):
            for j in range(i,6*i+1):
                for k in range(1, 7):
                    if j>k:
                        dp[i][j] += dp[i-1][j-k]
                dp[i][j] /= 6.0
        res = []
        for i in range(0, K):
            if dp[n][i] > 0:
                res.append((i, round(dp[n][i],2)))
        return res

s = Solution()
print(s.dicesSum(1))