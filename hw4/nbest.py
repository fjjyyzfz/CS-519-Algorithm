import random



def nbesta(a, b):
	AB = {}
	for i in a:
		for j in b:
			AB.setdefault(i + j, []).append((i, j))
	keys = sorted(AB.keys())
	pairs = [AB[key] for key in keys]
	i = 0
	k = 0
	result = []
	while(i < len(a)):
		if len(pairs[k]) == 1:
			result.append(pairs[k][0])
			i += 1
			k += 1
		else:
			sortedPairs = sorted(pairs[k], key = lambda x:x[1])
			j = 0
			while(i < len(a)) and (j < len(sortedPairs)):
				result.append(sortedPairs[j])
				i += 1
				j += 1
			k += 1
	return result

def nbestb(a, b):
	pairs = []
	for i in a:
		for j in b:
			pairs.append((i, j))
	result =[]
	for j in range(len(a)):
		result.append(qselect(j + 1, pairs))
	return result


def nbestc(a, b):
	result = []
	sortedA, sortedB = sorted(a), sorted(b)
	result.append((sortedA[0], sortedB[0]))
	i1, i2, j1, j2 = 0, 0, 0, 0
	while(len(result) < len(a)):
		sum1 = sortedA[i1] + sortedB[j1 + 1]
		sum2 = sortedA[i2 + 1] + sortedB[j2]
		if(sum1 < sum2 or (sum1 == sum2 and sortedA[j1 + 1] < sortedB[j2])):			
			result.append((sortedA[i1], sortedB[j1 + 1]))
			j1 += 1
		if(sum1 > sum2 or (sum1 == sum2 and sortedA[j2] < sortedB[j1 + 1])):	
			result.append((sortedA[i2 + 1], sortedB[j2]))
			i2 += 1		
		if(j1 == len(a) - 1):
			i1 += 1
			j1 = 0
		if(i2 == len(a) - 1):
			j2 += 1
			i2 = 0

	return result





def qselect(num, a):
	if a == [] or len(a) < num or num <= 0:
		return []
	else:
		pivot_index = random.randint(0, len(a)-1)
		a[0], a[pivot_index] = a[pivot_index], a[0]
		pivot = a[0]
		left = [x for x in a if sum(x) < sum(pivot) or (sum(x) == sum(pivot) and x[1] < pivot[1])]
		right = [x for x in a[1:] if sum(x) >= sum(pivot)]
		if len(left) + 1 == num:
			return pivot
		elif len(left) + 1 > num:
			return qselect(num, left)
		elif len(left) + 1 < num:
			num = num - len(left) - 1
			return qselect(num, right)







if __name__ == '__main__':
	a, b = [4, 1, 5, 3], [2, 6, 3, 4]
	print(nbesta(a, b))
	print(nbestb(a, b))
	print(nbestc(a, b))






