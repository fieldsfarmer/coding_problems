class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, A, V, m):
        # Write your code here
        # l = len(A)
        # dp = [[0]*(m+1) for _ in range(l+1)]
        # for i in range(l):
        #     for j in range(m+1):
        #         if i==0 or j==0:
        #             dp[i][j] = 0
        #         if A[i]>j:
        #             dp[i+1][j] = dp[i][j]
        #         else:
        #             dp[i+1][j] = max(dp[i][j], dp[i][j-A[i]]+V[i])
        #             a = j-A[i]
        #             cnt = 1
        #             while a-A[i]>=0:
        #                 a -= A[i]
        #                 cnt += 1
        #                 dp[i+1][j] = max(dp[i+1][j], dp[i][a]+cnt*V[i])
        # return dp[l][m]
        
        # l = len(A)
        # d = [0]*(m+1)
        # t = [0]*(m+1)
        # for i in xrange(l):
        #     for j in xrange(1,m+1):
        #         if A[i]>j:
        #             t[j] = d[j]
        #         else:
        #             cnt = 0
        #             a = j
        #             t[j] = d[j]
        #             while a-A[i]>=0:
        #                 a-=A[i]
        #                 cnt += 1
        #                 t[j] = max(t[j], d[a]+cnt*V[i])
        #     d = t
        # return d[-1]


        #### The above two methods are all TLE; To the surprise, 
        #### the good one is the easiest one as following.
        
        l = len(A)
        d = [0]*(m+1)
        for a,v in zip(A,V):
            for j in range(a,m+1):
                if d[j-a]+v > d[j]:
                    d[j] = d[j-a]+v
        return d[m]
        
        
                    
                    
                    
                    
                    
        