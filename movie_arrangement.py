import sys
def arrange_moves(d):
	d,start,end = change_interval_to_number(d)
	print d
	l = len(d)
	v = [False]*(end-start)
	movies = {}
	for k in d.keys():
		movies[k]=-1
	dfs(movies, d, v, l)
	return movies

def dfs(movies, d, v, l):
	if l==0: return True
	for m in movies.keys():
		if movies[m]<0:
			for n in d[m]:
				if not v[n]:
					movies[m]=n
					v[n]=True
					if dfs(movies, d, v,l-1):
						return True
					v[n]=False
	return False


def change_interval_to_number(d):
	start = sys.maxint
	end = -1
	for v in d.values():
		for i in v:
			start=min(start, i[0])
			end = max(end, i[1])
	res = {}
	for k in d.keys():
		t = []
		for i in d[k]:
			t.append(i[0]-start)
		t.sort()
		res[k]=t
	return (res, start, end)


def main():
	d = {
		0: [[0,1],[3,4]],
		1: [[1,2],[3,4]],
		2: [[2,3],[4,5]],
		3: [[3,4],[5,6]]
	}
	print arrange_moves(d)

if __name__ == '__main__':
	main()