# Given four points, judge what it looks like:
# square, rectangle, diamond, parallelogram

def what_shape(points):
	lines = []
	for i in range(0,3):
		for j in range(i+1, 4):
			lines.append( square_dist(points[i], points[j]) )
	lines.sort()
	if all(lines[i] == lines[0] for i in range(4)):
		if lines[4] == lines[5]:
			print('square')
		else:
			print('diamond')
	elif lines[0] == lines[1] and lines[2] == lines[3]:
		if lines[4] == lines[5]:
			print('rectangle')
		else:
			print('parallelogram')
	else:
		print('something else')


def square_dist(p1, p2):
	return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

# This one don't need to calculate the distance
def is_square(points):
	cx, cy = 0, 0
	for i in points:
		cx += i[0]
		cy += i[1]
	cx /= 4.0
	cy /= 4.0
	vx, vy = points[0][0]-cx, points[0][1]-cy
	l = [points[0]]
	for i in range(1,4):
		vx, vy = -vy, vx
		l.append( (vx+cx, vy+cy) )
	l.sort()
	points.sort()
	if l == points:
		print 'it is square'
	else:
		print 'it is not'

def main():
	# points = [(0,0),(0,1),(1,1),(1,0)]
	# is_square(points)
	points = [(0,0),(0,2),(1,2),(1,0)]
	is_square(points)
	# what_shape(points)


if __name__ == '__main__':
	main()