print("Summation of 10 random numbers\n")
x = 0
even = 0
odd = 0 
for k in range (1,11):
	add = eval(input(f"Input (k) = "))
	x += add
	if add % 2 == 0:
		even += add
	else:
		odd += add

print(f"The Summation of the number is: {x} ")
print(f"The Summation of the number is: {even} ")
print(f"The Summation of the number is: {odd} ")