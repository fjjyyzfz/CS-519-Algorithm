from collections import Iterable

def sort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot]
		right = [x for x in a[1:] if x >= pivot]
		return [sort(left)] + [pivot] + [sort(right)]

def sorted(t):
	
	if isinstance(t, Iterable):
		return [item for sublist in t for item in sorted(sublist)]
	else:
		return [t]


def search(t, x):
	flatten_t = sorted(t)
	return x in flatten_t	


def _search(t, x):
	if t == []:
		return []
	else:
		left, root, right = t
		if root == x:
			return [left + root + right]
		elif root > x:
			_search(left, x)
		else:
			_search(right, x)


def insert(t, x):
	temp = _search(t, x)
	i = 0
	if temp == []:
		i += 1
		left, root, right = t
		
			

		

