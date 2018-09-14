from bisect import bisect
import time

def find(arr, x, k):
	if(k > len(arr)):
		return None
	elif(k == len(arr)):
		return arr
	index = bisect(arr, x)
	first, second = index - 1, index
	for i in range(k):
		if(first >= 0 and (second <= len(arr) - 1)):			
			left = x - arr[first]
			right = arr[second] - x
			if (left <= right):
				first = first - 1
			else:
				second = second + 1
		elif(first < 0):
			second = second + k - i
			return arr[first + 1 :second]
		elif(second == len(arr)):
			first = first - k + i
			return arr[first + 1 :second]
	return arr[first + 1 :second]
	








if __name__ == '__main__':
	a = list(range(1000000))
	x = 500000
	k = 1
	runtime = time.time()
	out = find(a, x, k)
	runtime = time.time() - runtime
	print(runtime)
	

			

		