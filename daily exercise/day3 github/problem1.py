n = 5
for i in range(1, n+1):
	for j in range(0, n-i+1):
		print(' ', end='')
	start = 1
	for j in range(1, i+1):
		print(' ', start, sep='', end='')
		start = start* (i - j) // j 
	print()


n = 5
for i in range(1, n+1):

	start = 1
	for j in range(1, i+1):
		print(' ', start, sep='', end='')
		start = start* (i - j) // j 
	print()