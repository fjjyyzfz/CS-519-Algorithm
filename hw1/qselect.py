import random


def qselect(num, a):
	if a == [] or len(a) < num or num <= 0:
		return []
	else:
		pivot_index = random.randint(0, len(a)-1)
		a[0], a[pivot_index] = a[pivot_index], a[0]
		pivot = a[0]
		left = [x for x in a if x < pivot]
		right = [x for x in a[1:] if x >= pivot]
		if len(left) + 1 == num:
			return pivot
		elif len(left) + 1 > num:
			return qselect(num, left)
		elif len(left) + 1 < num:
			num = num - len(left) - 1
			return qselect(num, right)

