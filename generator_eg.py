#generator, decrator, closure
#oo class
#xrange vs range

#a generator function is one with keyword: yeild
import math

# def isPrime(a):
# 	if a > 1:
# 		if a == 2:
# 			return True
# 		if a%2 == 0:
# 			return False
# 		for p in range(3, (int)(math.sqrt(a)+1), 2):
# 			if a%p == 0: 
# 				return False
# 		return True
# 	return False

# def getPrimes(num):
# 	n = 2
# 	# yield n
# 	while n<num:
# 		if isPrime(n):
# 			yield n
# 		n += 1

# for i in getPrimes(100):
# 	print i

# def fib(m):
# 	n, a, b = 0, 0, 1
# 	while n < m:
# 		yield b;
# 		a, b = b, a+b
# 		n += 1

# for i in fib(6):
# 	print i

# def triangle(m):
# 	l = [1]
# 	n = 0
# 	yield l
# 	while n < m:
# 		l = [1]+[l[i]+l[i+1] for i in range(len(l)-1)]+[1]
# 		yield l
# 		n += 1

# for i in triangle(5):
# 	print i

'''http://code.activestate.com/recipes/117119/'''
def eratosthenes():
	'''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
	D = {}  # map composite integers to primes witnessing their compositeness
	q = 2   # first integer to test for primality
	while 1:
		if q not in D:
			yield q        # not marked composite, must be prime
			D[q*q] = [q]   # first multiple of q not already marked
		else:
			for p in D[q]: # move each witness to its next multiple
				D.setdefault(p+q,[]).append(p)
			del D[q]       # no longer need D[q], free memory
		q += 1

n = 0
a = []
for i in eratosthenes():
	a.append(i)
	n += 1
	if n == 100:
		break
print a


		