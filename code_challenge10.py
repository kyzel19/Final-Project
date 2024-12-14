for k in range(1,6):
	for y in range(6, k, -1):
		print(" ", end = " ")
	for z in range(1, k+1):
		print("*", end=" ")
	for e in range(1, k+1):
		print("*", end =" ")
	print()

for k in range(1,6):
	for y in range(1, k + 1):
		print(" ", end = " ")
	for z in range(6, k ,-1):
		print("*", end=" ")
	for e in range(6, k, -1):
		print("*", end =" ")
	print()