class Node:
	def __init__(self,x):
		self.val = x
		self.children = []
def bfs(rt):
	if not rt: return
	q = [rt]
	while q:
		u = q.pop(0)
		yield u
		for v in u.children:
			q.append(v)

# tag = -1: dfs; tag = 0: bfs
def xfs(rt, tag):
	if not rt: return
	arr = [rt]
	while arr:
		u = arr.pop(tag)
		yield u
		for v in u.children:
			arr.append(v)

def dfs(rt):
	return xfs(rt, -1)

def main():
	root = Node(0)
	a, b, c = Node(1), Node(2), Node(3)
	d = Node(5)
	e, f, g = Node(6), Node(7), Node(8)
	root.children = [a,b,c]
	a.children = [d]
	b.children = [e,f,g]
	# for i in bfs(root):
	# 	print(i.val)
	# for i in xfs(root, -1):
	# 	print(i.val)
	for i in dfs(root):
		print(i.val)

if __name__=='__main__':
	main()


### 339, 366, 297

