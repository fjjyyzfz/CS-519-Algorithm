def max_wis(arr):
	results = {-1:0, 0:0}
	n = len(arr);
	back = {}

	def find(n):
		if n not in results:
			if find(n - 1) > (find(n -2) + arr[n - 1]):
				results[n] = find(n - 1)
				back[n] = 0
			else:
				results[n] = find(n - 2) + arr[n - 1]
				back[n] = 1
		return results[n]
	def traceback(back, results, n):
		if n < 1:
			return []
		if back[n] == 1:
			return traceback(back, results, n - 2) + [results[n] - results[n - 2]]
		else:
			return traceback(back, results, n - 1)
	result = find(n)
	trace = traceback(back, results, n)
	return result, trace

def max_wis2(arr):
	n = len(arr)
	back = {}
	def find(n):
		fast, slow = 0, 0
		for i in range(0, n):
			if  fast > arr[i] + slow:
				fast, slow = fast, fast
				back[i] = 0
			else:
				fast, slow = arr[i] + slow, fast
				back[i] = 1
		return fast
	result = find(n)
	def traceback(back, arr, n):
		if n <= 0 or arr[n - 1] < 0:
			return []
		if back[n - 1] == 1:
			return traceback(back, arr, n - 2) + [arr[n - 1]]
		else:
			return traceback(back, arr, n - 1)
	trace = traceback(back, arr, n)
	return result, trace



if __name__ == "__main__":
	print(max_wis([7,8,5]))
	print(max_wis([-1,8,10]))
	print(max_wis([-5,-1,-4]))
	print(max_wis([]))
	