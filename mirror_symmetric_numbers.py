def isSelfSym(a):
	return a=='0' or a=='1' or a=='8'

def isMirrorSym(a, b):
	return (a==b and isSelfSym(a)) or (a=='6' and b=='9') or (a=='9' and b=='6')

def isSameAfter180(a):
	if len(a)%2==1 and not isSelfSym(a[len(a)/2]):
			return False
	for i in range(len(a)/2):
		if not isMirrorSym(a[i], a[len(a)-i-1]):
			return False
	return True

def generateSymStrings(n):
	if not n: return ''
	self_sym = ['0', '1', '8']
	mirror = ['6', '9', '0', '1', '8']
	q = ['']
	for i in range(n/2):
		expand(q, mirror)
	if n%2==1:
		expand(q, self_sym)
	res = []
	while q:
		u = q.pop(0)
		res.append(getFinal(u, n))
	return res

def getFinal(u, n):
	if n<2:
		return u
	for i in range(n/2-1, -1, -1):
		u = u+getMirror(u[i])
	return u

def getMirror(s):
	if s in ('0', '1', '8'): return s
	if s == '6': return '9'
	if s == '9': return '6'



def expand(q, arr):
	l = len(q)
	for i in range(l):
		u = q.pop(0)
		for a in arr:
			q.append(u+a)

def main():
	print( isSameAfter180('161'), isSameAfter180('688'), isSameAfter180('6889'))
	print generateSymStrings(4)




if __name__ == '__main__':
	main()