name = input("Enter Your Name: ")

isStudent = input("Are you a student of DLL(Yes/No): ")

if isStudent.lower()=="yes":
	print("Welcome to the DLL BSIT Scholarship form") 
	GG = input("Are you from Brgy. Gulang Gulang (yes/no):")
	if GG.lower()=="yes":
		print("Please fillup the second form")
		yearlevel = input("What year are you currently enrolled?\nF-Freshnen\nS-Sophomore\nJ-Junior\nR-Senior\nPlease input your answer here: ")

		if yearlevel.lower() == 'f':
			print(f"Hi {name}, Freshmen, Welcome to DLL")

		elif yearlevel.lower() == 's': 
			print(f"Hi {name}, Sophomore, Welcome to DLL")

		elif yearlevel.lower() == 'j': 
			print(f"Hi {name}, Junior, Welcome to DLL")

		elif yearlevel.lower() == 'r': 
			print(f"Hi {name}, Senior, Welcome to DLL")

		else:
			print("Invalid Option")
		IsNeeded = input("Would you like to apply for a scholarship? (yes/no): ")

		if IsNeeded.lower() == "yes":
			 print("Scholarship approved")
		else:
			print("Unfortunately, this scholarship grant are only for residents of Gulang-Gulang")
		print("Your form has been successfully submitted")