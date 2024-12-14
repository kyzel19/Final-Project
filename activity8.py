password = input("Enter your password: ")

if password.lower() == "secret": 
	print("Access Granted")
	print("Enjoy using the system")
elif password.lower() == "1004":
	print("Welcome, Yoon Jeonghan")
	print("Access Granted")
else:
	print("Incorrect password, Access Denied")

print("Thank you!")