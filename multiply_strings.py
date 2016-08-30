def multiply_strings(a,b):
	if a == '0' or b == '0':
		return '0'
	if a == '1': return b
	if b == '1': return a
	r = [0]*(len(a)+len(b))
	position = 0
	for i in reversed(a):
		t = position
		for j in reversed(b):
			r[t] += int(i)*int(j)
			r[t+1] += r[t]/10
			r[t] %= 10
			t += 1
		position += 1
	non_zero = -1
	for i in range(len(r)-1, -1, -1):
		if r[i]!=0:
			break
	return ''.join(map(str,r[:i+1][::-1]))

def main():
	a = '1123'
	b = '20'
	print(multiply_strings(a,b))


if __name__ == '__main__':
	main()