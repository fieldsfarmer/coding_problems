import collections

def longest_substring_with_k_distinct_chars(str, k):
	if k == 0:
		return ''
	l = len(str)
	if k>=l:
		return str
	i, j = 0, 0
	d = collections.defaultdict(int)
	cnt = 0
	res = ''
	while i<l:
		if d[str[i]]==0 and cnt==k:
			t = str[j:i]
			if len(t)>len(res):
				res = t
			while j<i:
				d[str[j]]-=1
				if d[str[j]]==0:
					j += 1
					cnt -= 1
					break
				j+=1
		if d[str[i]]==0:
			cnt+=1
		d[str[i]]+=1
		i+=1
	if len(res)<i-j:
		res = str[j:i]
	return res

def data_stream(s, k):
	l = len(s)
	if k == 0: return [0]*l
	res = []
	# record whether a chars shows or not
	d1 = collections.defaultdict(int)
	# save the last position
	d2 = collections.defaultdict(int)
	cnt = 0
	j = 0
	for i in range(l):
		d2[s[i]]=i
		if d1[s[i]]==0 and cnt==k:
			min_k, min_v = get_key_with_min_value(d2)
			j = min_v+1
			# set the key with min last position as non existent
			d1[min_k]==0
		if d1[s[i]]==0: cnt+=1
		d1[s[i]]+=1
		res.append([s[j:i+1]])
	return res

def data_stream1(s, k):
	l = len(s)
	if k==0: return [0]*l
	# save the last position
	d = {}
	cnt = 0
	initial = 0
	res = []
	lens = []
	for i in range(l):
		if (s[i] not in d or d[s[i]]==-1) and cnt == k:
			# get the key and value of the d with min last position
			mink, minv = get_key_with_min_value(d)
			# update the initial position of substring
			initial = minv+1
			d[mink]=-1
			cnt -= 1
		if s[i] not in d or d[s[i]]==-1: cnt+=1
		d[s[i]]=i

		if not lens or i-initial+1>lens[-1]:
			lens += [i-initial+1]
		else:
			lens += [lens[-1]]
		res.append(s[initial:i+1])

	return lens, res


# return the key that has minimum value which is not -1
def get_key_with_min_value(d):
	arr = list(d.values())
	arr.sort()
	m_v=-1
	for i in arr:
		if i != -1:
			m_v = i
			break
	for k in d.keys():
		if d[k] == m_v:
			return (k, m_v)


def main():
	s = 'eceba'
	s = 'ecebabbdadada'
	k = 2
	# print(longest_substring_with_k_distinct_chars(s, 2))
	s = 'aababaccaabbbbbbbbbb'
	print data_stream1(s, 2)

if __name__ == '__main__':
	main()

