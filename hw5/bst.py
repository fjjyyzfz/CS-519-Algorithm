def bsts(n):
	result = 0
	if n == 0:
		return 1
	for i in range(1, n + 1):
		result += bsts(i - 1) * bsts(n - i)
	return result

if __name__ == "__main__":
	print(bsts(5))

	