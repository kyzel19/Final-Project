for k in range(1,7):
	for y in range(6, k, -1):
		print(" ", end = " ")
	for y in range(k, 1, -1):
		print(y, end=" ")
	for z in range(1, k+1):
		print(z, end =" ")
	print()

for k in range(5,0,-1):
	for y in range(6, k, -1):
		print(" ", end = " ")
	for y in range(k,1,-1):
		print(y, end=" ")
	for z in range(1,k+1):
		print(z, end =" ")
	print()