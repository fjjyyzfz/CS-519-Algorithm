import heapq



def kmergesort(arr, k):
	n = len(arr)
	newArr = []
	if n >= k:
		for i in range(k):			
			newArr.append(kmergesort(arr[i * n // k:(i + 1) * n // k], k))
	else:
		for i in arr:
			newArr.append([i]) 
			print(newArr)
	return kmerge(newArr, len(newArr))







def kmerge(arr, k):
	result = []
	for i in range(k):
		result = list(heapq.merge(result, arr[i]))

	return result

if __name__ == '__main__':
	print(kmergesort([4, 1, 5, 2, 6, 3, 7, 0], 3))
	print(kmergesort([4, 1], 3))