Prelim = eval(input("Enter Prelim grade --> "))

Midterm = eval(input("Enter Midterm grade --> "))

Semifinal = eval(input("Enter Semifinal grade --> "))

Final = eval(input("Enter Final grade --> "))

Quiz = eval(input("Enter Quiz grade --> "))

Project = eval(input("Enter Project grade --> "))



if(Prelim >=65 and Prelim <=100) and (Midterm >=65 and Midterm <=100) and (Semifinal >=65 and Semifinal <=100) and (Final >=65 and Final <=100) and (Quiz >=65 and Quiz <=100) and (Project >=65 and Project <=100):
	 FinalGrade = (Prelim * 0.15) + (Midterm * 0.15) + (Semifinal * 0.15) + (Final * 0.15) + (Quiz * 0.25) + (Project * 0.15)
print(f"Your grade is : {round(FinalGrade, 2)}")
if FinalGrade > 100 :
	print("Invalid Grade, Perhaps a mistake?")
elif FinalGrade >= 75 : 
	print("Congratulations! You've passed the course")
else:
	print("Unfortunately, You failed")