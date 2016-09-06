# back pack problem and its reverse problem. Very interesting!
def bp(m, A):
	dp = [0]*(m+1)
	dp[0]=1
	for i in range(len(A)):
		for j in range(m+1):
			if j>=A[i]:
				dp[j]+=dp[j-A[i]]
	return dp

def bp_reverse(m, A):
	res = []
	tt = list(A)
	while tt[-1]!=0:
		for i in range(1,len(tt)):
			if tt[i]!=0:
				res.append(i)
				break
		u = bp(m,res)
		for i in range(len(tt)):
			tt[i]=A[i]-u[i]
	return res


def main():
	A = [2,5,6]
	m = 10
	# [1, 0, 1, 0, 1, 1, 2, 1, 2, 1, 3]
	# for m in range(1,11):
	# 	print bp(m,A)
	dp = [1, 0, 1, 0, 1, 1, 2, 1, 2, 1, 3]
	print bp_reverse(m,dp)
	# print bp(m,[2,5])

if __name__ == '__main__':
	main()