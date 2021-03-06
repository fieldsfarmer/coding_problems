'''
Given n items with size A[i], an integer m denotes the size of a backpack. 
How full you can fill this backpack?

If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, 
we can select [2, 3, 5], so that the max size we can fill this backpack is 10. 
If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):

        # l = len(A)
        # f = [[False]*(m+1) for _ in range(l+1)]
        ### f[i][j] is true if can find items in A[:i] such that the total size if j
        # f[0][0] = True
        # for i in range(l):
        #     for j in range(m+1):
        #         f[i+1][j] = f[i][j]
        #         if A[i]<=j and f[i][j-A[i]]:
        #             f[i+1][j] = True
        # for j in range(m,-1,-1):
        #     if f[l][j]:
        #         return j
        # return 0


        ### optimized verison ####
        l = len(A)
        dp = [False]*(m+1)
        tmp = [False]*(m+1)
        dp[0] = True
        
        for i in range(l):
            for j in range(m+1):
                tmp[j]=dp[j]
                if A[i]<=j and dp[j-A[i]]:
                    tmp[j] = True
            dp = tmp
            tmp = [False]*(m+1)
       
        
        for j in range(m,-1,-1):
            if dp[j]:
                return j
        return 0

      
ss = Solution()          
a = [10, [3,4,8,5]]
print ss.backPack(*a)