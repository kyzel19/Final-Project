print("Factorial\n")

f = eval(input("Enter any number to factor: "))
outcome = 1
for x in range(f, 0, -1):
	outcome *= x

print(f"The Factorial of {f} is {outcome} ")