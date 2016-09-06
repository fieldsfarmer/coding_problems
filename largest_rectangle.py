# If you want to solve it using maximal square method, then you will be wrong!
# using the following dp cannot solve it, this is because it is not unique!
# m = ['101','101','111']
def wrong_maximalRectangle(m):
    r = len(m)
    if not r: return 0
    c = len(m[0])
    if not c: return 0
    dp = [[(0,0)]*c for _ in range(r)]
    res = 0
    
    for j in range(c):
        if m[0][j] == '1':
            if j>0:
                u,v = dp[0][j-1]
                dp[0][j] = (u+1,1)
            else:
                dp[0][j] = (1,1)
            u,v=dp[0][j]
            res = max(res, u*v)
    for i in range(1,r):
        if m[i][0] == '1':
            u,v = dp[i-1][0]
            dp[i][0] = (1,v+1)
            u,v = dp[i][0]
            res = max(res, u*v)
    
        
    for i in range(1,r):
        for j in range(1,c):
            if m[i][j] == '1':
                a,b = dp[i-1][j-1]
                cc,d = dp[i-1][j]
                e,f = dp[i][j-1]

                if a==0 and e==0:
                    u,v=1,1+d
                elif b==0 and d==0:
                    u,v=1+e,1
                else:
                    u = 1+min(a,e)
                    v = 1+min(b,d)

                dp[i][j] = (u,v)
                res = max(res, u*v)
    print dp
    return res

def maximalRectangle(m):
    r = len(m)
    if not r: return 0
    c = len(m[0])
    if not c: return 0
    left = [0]*c
    # right= [c]*c
    right = [c-1]*c
    height = [0]*c
    res = 0
    for i in range(r):
        cur_left, cur_right = 0, c
        for j in range(c):
            if m[i][j]=='1': height[j]+=1
            else: height[j]=0
        for j in range(c):
            if m[i][j]=='1': left[j]=max(left[j],cur_left)
            else:
                left[j]=0
                cur_left=j+1
                # cur_left = j
        for j in range(c-1,-1,-1):
            if m[i][j]=='1': right[j]=min(right[j],cur_right)
            else:
                right[j]=c-1
                cur_right=j-1
        for j in range(c):
            # res = max(res, height[j]*(right[j]-left[j]))
            print left
            print right
            print height
            res = max(res, height[j]*(right[j]-left[j]+1))

    return res

def main():
    # m = ['10100','10111','11111','10010']
    # m = ['01','01']
    m = ["10","10"]
    # m = ['101','101','111']
    # m = ["101101","111111","011011","111010","011111","110111"]
    # m = ['101','111','011','111','011']
    # m = ['1']
    print maximalRectangle(m)

if __name__ == '__main__':
    main()
