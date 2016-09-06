class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        l=len(values)
        if l==0: return False
        if l==1: return True
        dp=[[0]*l for _ in range(l)]
        for i in range(l):
            dp[i][i]=values[i]
        for i in range(1,l):
            dp[i-1][i]=max(values[i-1],values[i])
        for i in range(l-1):
            for j in range(i+1,l):
                dp[i][j] = sum(values[i:j+1])-min(dp[i+1][j],dp[i][j-1])
        return dp[0][l-1]*2>sum(values)


s = Solution()
v = [1,9999999,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,200,1,1,1,1,1,1,1,1,800,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
v = [1,20,4]
v =[1,9,1,1,1]
print s.firstWillWin(v)