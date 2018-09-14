def find(arr):
	assert len(arr) > 2
	arr.sort()
	n = len(arr) - 1
	result = []
	while(n > 1):
		i, j = 0, n - 1
		while(i < j):
			if(arr[i] + arr[j] == arr[n]):
				result.append((arr[i], arr[j], arr[n]))
				i += 1
				j -= 1
			elif(arr[i] + arr[j] > arr[n]):
				j -= 1
			else:
				i += 1
		n -= 1
	return result


if __name__ == '__main__':
	print(find([1,4,2,3,5]))
