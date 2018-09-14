def qselect(num, a):
	if a == [] or len(a) < num or num <= 0:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot]
		mid = [x for x in a if x == pivot]
		right = [x for x in a[1:] if x > pivot]
		numLeft, numMid, numRight = len(left), len(mid), len(right)
		if num < numLeft:
			return qselect(num, left)
		elif num <= numLeft + numMid:
			return pivot, numLeft, numLeft + numMid -num
		else:
			pivot1, numLeft1, rest1 = qselect(num, right)
			return pivot1, numLeft + numMid + numLeft1, rest1
			


def find(arr, n, k):
	arrSort = [abs(x - n) for x in arr]
	maxValue, numUnmatch, rest = qselect(k, arrSort)
	result = []
	for i, val in enumerate(arrSort):
		if(val <= maxValue and rest == 0 and len(result) < k):
			result.append(arr[i])
		elif(val < maxValue and k == numUnmatch and len(result) < k):
			result.append(arr[i])
		elif(val <= maxValue and rest != 0 and len(result) < k):
			result.append(arr[i])
			rest -= 1
		elif(val < maxValue and rest == 0 and len(result) < k):
			result.append(arr[i])
	return result



	

if __name__ == "__main__":
	print(find([4,1,3,2,7,4], 5.2, 2))
	#print(find([4,1,3,2,7,4], 6.5, 3))
	#print(find([5,3,4,1,6,3], 3.5, 2))