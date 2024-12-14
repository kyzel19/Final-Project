for k in range(1,5):
	for y in range(5, k, -1):
		print(" ", end = " ")
	for z in range(1, k+1):
		print("*", end=" ")
	for e in range(1, k+1):
		print("*", end =" ")
	print()

for k in range(0,4):
	for y in range(4, 0, -1):
		print(" ", end = " ")
	for z in range(2,4):
		print("*", end=" ")
	for e in range(4, 0, -1):
		print(" ", end =" ")
	print()