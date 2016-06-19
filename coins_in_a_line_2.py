'''
There are n coins with different value in a line. Two players take turns to take 
one or two coins from left side until there are no more coins left. The player 
who take the coins with the most value wins.

Could you please decide the first player will win or lose?

Given values array A = [1,2,2], return true.
Given A = [1,2,4], return false.
'''

# use memory search. dp[n] is to calculate the largest values if there are still n coins left

class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        if n<3: return True
        total = sum(values)
        dp = [0]*(n+1)
        v  = [False]*(n+1) 
        return total<2*self.msearch(dp,v,n, values)
    def msearch(self,dp,v,n, values):
        if v[n]: return dp[n]
        v[n] = True
        l = len(values)
        if n==0: dp[n] = 0
        elif n==1: dp[n] = values[l-n]
        elif n<=3: dp[n] = values[l-n]+values[l-n+1]
        else:
            dp[n] = max(
                values[l-n]+min(self.msearch(dp,v,n-2,values), self.msearch(dp,v,n-3,values)),
                values[l-n]+values[l-n+1]+min(self.msearch(dp,v,n-3,values), self.msearch(dp,v,n-4,values))
            )
        return dp[n]