'''
There are n coins in a line. Two players take turns to take a coin from 
one of the ends of the line until there are no more coins left. 
The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Example
Given array A = [3,2,2], return true.
Given array A = [1,2,4], return true.
Given array A = [1,20,4], return false.
'''


class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        sz = len(values)
        if sz<2: return True
        dp = [[0]*sz     for _ in range(sz)]
        v  = [[False]*sz for _ in range(sz)]
        total = sum(values)
        return total < 2*self.msearch(dp,v,0,sz-1,values)
    def msearch(self, dp, v, left, right, values):
        if v[left][right]: return dp[left][right]
        v[left][right] = True
        res = 0
        
        if left==right: res = values[left]
        elif left+1==right:
            res = max(values[left], values[right])
        elif left<right: 
            res = max(
                values[left]+min(self.msearch(dp,v,left+2,right,values), self.msearch(dp,v,left+1,right-1,values)),
                values[right]+min(self.msearch(dp,v,left+1,right-1,values),self.msearch(dp,v,left,right-2,values))
            )
        dp[left][right] = res
        return res