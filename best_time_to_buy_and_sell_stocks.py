import sys
import heapq

def transactions_at_most_2(prices):
    r2,r1=0,0
    h2,h1=-sys.maxsize,-sys.maxsize
    for p in prices:
        r2 = max(r2,h2+p)
        h2 = max(h2,r1-p)
        r1 = max(r1,h1+p)
        h1 = max(h1,-p)
    return r2

def transactions_at_most_2_with_instructions(prices):
    r2,r1=0,0
    h2,h1=-sys.maxsize,-sys.maxsize
    res = [None, None, None, None]
    for i in range(len(prices)):
        p = prices[i]
        r2 = max(r2,h2+p)
        if r2>0:
            res[3] = i
        h2 = max(h2,r1-p)
        if r2>0:
            res[2] = i  
        r1 = max(r1,h1+p)
        if r1>0:
            res[1] = i
        h1 = max(h1,-p)
        if r1>0:
            res[0] = i
    return res

def maxProfit(k, prices):        
    heap=[]
    st=[]
    p,v=0,0
    l=len(prices)
    while p<l:
        v=p
        while v<l-1:
            if prices[v]<prices[v+1]: 
                break
            v+=1
        p=v+1
        while p<l:
            if prices[p]<prices[p-1]:
                break
            p+=1
        while st and prices[v]<prices[st[-1][0]]:
            heapq.heappush(heap,-(prices[st[-1][1]-1]-prices[st[-1][0]]))
            st.pop()
        while st and prices[p-1]>=prices[st[-1][1]-1]:
            heapq.heappush(heap, -(prices[st[-1][1]-1]-prices[v]))
            v=st[-1][0]
            st.pop()
        st.append([v,p])
    while st:
        # print st
        heapq.heappush(heap,-(prices[st[-1][1]-1]-prices[st[-1][0]]))
        st.pop()
    res = 0
    for i in range(k):
        if heap:
            res += -1*heapq.heappop(heap)
    return res

def main():
    prices = [1,2,3,2,0.5,2,4.5]
    # prices = [3,2,1,2]
    prices = [2,1,4,5,2,9,7]
    prices = [6,1,3,2,4,7]
    print(transactions_at_most_2(prices))
    print( maxProfit(2, prices) )
    # print( transactions_at_most_2_with_instructions(prices) )


if __name__ == '__main__':
    main()