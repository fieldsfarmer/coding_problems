#calculate the largest square in a matrix such that the square only has 1 in its diagonal.


def diagonal_matrix(matrix):
	r=len(matrix)	
	if not r: return 0
	c=len(matrix[0])
	if not c: return 0
	leftzeros=get_left_zeros(matrix)
	upzeros = get_up_zeros(matrix)
	dp=[[0]*c for _ in range(r)]
	res = 0
	for i in range(r):
		dp[i][0]=1 if matrix[i][0]==1 else 0
		res = max(dp[i][0], res)
	for i in range(c):
		dp[0][i]=1 if matrix[0][i]==1 else 0
		res = max(dp[0][i], res)
	for i in range(1,r):
		for j in range(0,c):
			if matrix[i][j]==1:
				dp[i][j]=min(dp[i-1][j-1], leftzeros[i][j-1], upzeros[i-1][j])+1
				res = max(res, dp[i][j]**2)
	return res


def get_left_zeros(matrix):
	r=len(matrix)
	c=len(matrix[0])
	res=[[0]*c for _ in range(r)]
	for i in range(r):
		res[i][0]=1 if matrix[i][0]==0 else 0
	for i in range(r):
		for j in range(1,c):
			if matrix[i][j]==0:
				res[i][j]=res[i][j-1]+1
			else:
				res[i][j]=0
	return res

def get_up_zeros(matrix):
	r=len(matrix)
	c=len(matrix[0])
	res=[[0]*c for _ in range(r)]
	for i in range(c):
		res[0][i]=1 if matrix[0][i]==0 else 0
	for i in range(1,r):
		for j in range(c):
			if matrix[i][j]==0:
				res[i][j]=res[i-1][j]+1
			else:
				res[i][j]=0
	return res

def main():
	m = [[0,0,0,0],[0,0,0,0],[1,0,0,1],[0,1,0,1]]
	print diagonal_matrix(m)

if __name__ == '__main__':
	main()
