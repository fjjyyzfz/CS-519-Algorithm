import heapq;

def ksmallest(k, arr):
	kArr = []
	for i in arr:
		if len(kArr) < k:
			heapq.heappush(kArr, -i)
		elif -i > kArr[0]:
			heapq.heappushpop(kArr, -i)
	kSmall = sorted([-i for i in kArr])
	return kSmall

if __name__ == '__main__':
	print(ksmallest(20,[10, 2, 9, 3, 7, 8, 11, 5, 7]))
	print(ksmallest(3, range(1000000, 0, -1)))
	print(ksmallest(20, [10, 7, 23, 2, 9, 3, 7, 8, 11, 5, 7]))
	