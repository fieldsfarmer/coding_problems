import random

def random_array_generator(arr, k):
	l = len(arr)
	while True:
		if l<=k:
			yield arr
		else:
			yield random.sample(arr, k)

def g(arr):
	i = 0
	l = len(arr)
	for i in arr:
		yield i

def main():
	arr = [1,2,3,4,5,6]
	k = 3
	n = 10
	t = random_array_generator(arr, k)
	# for i in range(n):
	# 	# print(t.next())
	# 	print(next(t))
	u = g([])
	for i in range(10):
		try:
			print next(u)
		except StopIteration:
			print 'Done'
			break

if __name__ == '__main__':
	main()