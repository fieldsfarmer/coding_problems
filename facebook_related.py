# problems with 
a = [0,0,1,3,0,0,2,4,0,0]
a = [0,0,0,0,1]
def move_zeros_to_left(a):
	non_zero_index = len(a)-1
	i = 0
	while i < non_zero_index:
		if a[i] == 0:
			i += 1
		else:
			a[i], a[non_zero_index] = a[non_zero_index], a[i]
			non_zero_index -= 1
	return a

print(move_zeros_to_left(a))

def move_zeros_to_right(a):
	zero_index = len(a)-1
	non_zero_index = -1
	i = 0 
	while i < zero_index:
		if a[i] == 0:
			a[i], a[zero_index] = a[zero_index], a[i]
			zero_index -= 1
		else:
			i += 1
	return a

print(move_zeros_to_right(a))









