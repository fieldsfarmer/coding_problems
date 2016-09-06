class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        l = len(A)
        if not l: return 0
        dp = [1]*l
        res = 1
        for i in range(1,l):
            if A[i]>=A[i-1]:
                dp[i]=dp[i-1]+1
                res = max(res, dp[i])
            else:
                dp[i]=1
        print dp
        dp = [1]*l
        for i in range(1,l):
            if A[i]<=A[i-1]:
                dp[i]+=1
                print A[i]
                print dp[i]
                res = max(res,dp[i])
            else:
                dp[i]=1
        print dp
        return res

a = [5,4,2,1,3]
s = Solution()
print s.longestIncreasingContinuousSubsequence(a)