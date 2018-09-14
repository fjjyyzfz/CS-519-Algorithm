import random, sys
from random import shuffle
random.seed(1325)
sys.path.append("/nfs/farm/classes/eecs/winter2018/cs519-010/include")
#from bst import sort

def sort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot]
		right = [x for x in a[1:] if x >= pivot]
		return [sort(left)] + [pivot] + [sort(right)]


def longest(a):
	return(max(heightandpath(a)))

def heightandpath(a):	
	if a == []:
		return None
	else:
		left = a[0]
		root = a[1]
		right = a[2]
		if left == [] and right == []:
			return [0, 0]
		return compare(heightandpath(left), heightandpath(right))



def compare(pair_l, pair_r):
	if pair_l == None:
		heightsum = pair_r[0] + 1
		pair = [heightsum, max(heightsum, pair_r[1])]
	elif pair_r == None:
		heightsum = pair_l[0] + 1
		pair = [heightsum, max(heightsum, pair_l[1])]
	else:
		heightsum = pair_l[0] + pair_r[0] + 2
		pair = [max([pair_l[0], pair_r[0]]) + 1, max(heightsum, pair_l[1], pair_r[1])]
	#print(pair)
	return pair

if __name__=='__main__':
	b = longest([[], 9, [[[], 10, []], 11, [[], 13, [[], 14, []]]]])
	#b = longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
	#print(random.sample(range(100), 100))
	#b = longest([[[], 3, []], 4, [[[], 10, []], 11, []]])
	#b = longest([[[], 3, []], 4, [[[[[], 6, []], 7, []], 8, [[], 8, []]], 10, [[], 11, [[], 13, [[], 15, []]]]]])
	#b = longest(sort(random.sample(range(100), 100)))
	#print(sort(random.sample(range(100), 100)))
	print(b)