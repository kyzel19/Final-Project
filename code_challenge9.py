z = eval(input("Enter a number: "))
for x in range(z, 0,-1):
	for y in range(z,x,-1):
		print(" ", end=" ")
	print("* " * x)