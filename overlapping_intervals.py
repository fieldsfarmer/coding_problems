a = [[1,3],[5,7]]
b = [[2,6]]


def overlapping_intervals(a, b):
	i, j = 0, 0
	res = []
	while i<len(a) and j<len(b):
		if isOK(a[i],b[j]):
			c = [ max(a[i][0], b[j][0]), min(a[i][1],b[j][1]) ]
			if c[1] == a[i][1]:
				i += 1
			if c[1] == b[j][1]:
				j += 1
			res.append(c)
	return res

def isOK(a, b):
	return max(a[0], b[0])<=min(a[1],b[1])


print overlapping_intervals(a, b)