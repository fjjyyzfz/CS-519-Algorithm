def mergesort(a):
	if len(a) <= 1:
		return a
	else:
		left = []
		right = []
		for i in range(len(a)):
			#print(range(len(a)))
			if i < len(a)/2:
				left.append(a[i])
			else:
				right.append(a[i])
		return merge(mergesort(left), mergesort(right))

def merge(a, b):
	c = []
	while a != [] and b != []:
		if a[0] > b[0]:
			c.append(b[0])
			b.remove(b[0])
		else:
			c.append(a[0])
			a.remove(a[0])
	if a == []:
		c += b
	if b == []:
		c += a

	return c



if __name__ == '__main__':
	b = mergesort([4, 2, 5, 1, 6, 3])
	print(b)