def num_inversion(num):
	q = [0]
	mergesort(num, q)
	return sum(q)


def mergesort(a, count):	
	if len(a) <= 1:
		return a
	else:
		left = []
		right = []
		for i in range(len(a)):
			if i < len(a)/2:
				left.append(a[i])
			else:
				right.append(a[i])
		return merge(mergesort(left, count), mergesort(right, count), count)

def merge(a, b, count):
	c = []
	while a != [] and b != []:
		if a[0] > b[0]:
			c.append(b[0])
			b.remove(b[0])
			count.append(len(a))
		else:
			c.append(a[0])
			a.remove(a[0])
	if a == []:
		c += b
	if b == []:
		c += a

	return c


if __name__ == '__main__':
	#count = [0]
	b = num_inversion([2, 4, 1, 3])
	print(b)