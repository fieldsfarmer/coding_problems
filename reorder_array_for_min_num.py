from functools import cmp_to_key # for python3

def comparison(a, b):
	t,s=str(a)+str(b),str(b)+str(a)
	if t<s: return -1
	elif t>s: return 1
	else: return 0

def main():
	arr = [ [0,0,0,0], 
			[3, 32, 321], 
			[41,23,87,55,50,53,18,9,39,63,35,33,54,25,26,49,74,61,32,81,
			 97,99,38,96,22,95,35,57,80,80,16,22,17,13,89,11,75,98,57,
			 81,69,8,10,85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,
			 80,43,10,24,88,52,16,92,61,28,26,78,28,28,16,1,56,31,47,85,
			 27,30,85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,
			 55]]
	for i in arr:
		i.sort(cmp=comparison) # python 2
		# i.sort(key=cmp_to_key(comparison)) # python 3
		p = None
		u = ''.join([str(x) for x in i])
		# print (u)
		for j in range(len(u)):
			if u[j] != '0':
				p = j
				break
		if p==None: 
			print('0')
		else: 
			print(u[p:])

if __name__ == '__main__':
	main()