def num_no(n):
	assert n >= 0
	if n == 0:
		return 0;
	a, b = 3, 2
	if n == 1:
		return b
	if n == 2:
		return a
	for i in range(3,n + 1):
		a, b = a + b, a
	return a

def num_yes(n):
	assert n >= 2
	a, b = 3, 1
	if n == 2:
		return b
	if n == 3:
		return a
	for i in range(4, n + 1):
		a, b = a + b + 2**(i - 2), a
	return a





if __name__ =="__main__":
	print(num_no(3))
	print(num_yes(5))