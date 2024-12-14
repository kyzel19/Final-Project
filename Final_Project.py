def printing_function():
    # ACT 1
    print("Hello World")

    # ACT 2
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter a number: "))
    answer = num1 + num2
    print(num1 , " plus " , num2 , " = " , answer)

def input_func():

    # ACT 3
    Name = input("PLEASE INPUT YOUR NAME : ")                
    Nickname = input("PLEASE INPUT YOUR NICKNAME : ")
    Age = input("PLEASE INPUT YOUR AGE : ")
    Birthmonth = input("PLEASE INPUT YOUR BIRTHMONTH : ")
    Birthday = input("PLEASE INPUT YOUR BIRTHDAY : ")
    Birthyear = input("PLEASE INPUT YOUR BIRTHYEAR : ")
    Gender = input("PLEASE INPUT YOUR GENDER : ")
    Address = input("PLEASE INPUT YOUR ADDRESS : ")
    Nationality = input("PLEASE INPUT YOUR NATIONALITY : ")
    isMarried = False
    CivilStatus = input("PLEASE INPUT YOUR CIVILSTATUS : ")
    Religion = input("PLEASE INPUT YOUR RELIGION : ")
    Citizenship = input("PLEASE INPUT YOUR CITIZENSHIP : ")
    Height = input("PLEASE INPUT YOUR HEIGHT : ")
    Weight =  input("PLEASE INPUT YOUR WEIGHT : ")
    NameofFather = input("PLEASE INPUT YOUR NAMEOFFATHER : ")
    OccupationofFather = input("PLEASE INPUT YOUR OCCUPATIONOFFATHER : ")
    ContactNumberofFather = input("PLEASE INPUT YOUR CONTACTNUMBEROFFATHER : ")
    NameofMother = input("PLEASE INPUT YOUR NAMEOFMOTHER : ")
    OccupationofMother = input("PLEASE INPUT YOUR OCCUPATIONOFMOTHER : ")
    ContactNumberofMother = input("PLEASE INPUT YOUR CONTACTNUMBEROFMOTHER : ")
    Elementary = input("PLEASE INPUT YOUR ELEMENTARY : ")
    YearAttendedElementary = input("PLEASE INPUT YOUR YEARATTENDEDELEMENTARY : ")
    YearEndedElementary = input("PLEASE INPUT YOUR YEARENDEDELEMENTARY : ")
    HighSchool = input("PLEASE INPUT YOUR HIGHSCHOOL : ")
    YearAttendedHighSchool = input("PLEASE INPUT YOUR YEARATTENDEDHIGHSCHOOL : ")
    YearEndedHighSchool = input("PLEASE INPUT YOUR YEARENDEDHIGHSCHOOL : ")
    College = input("PLEASE INPUT YOUR COLLEGE : ")
    Course = input("PLEASE INPUT YOUR COURSE : ")
    Skills = input("PLEASE INPUT YOUR SKILLS : ")
    print("My name is " + Name + ", I am often referred to as " + Nickname + ".\nI am " ,Age, " years old, born in " + Birthmonth + " on " + Birthday + ", " + Birthyear + ".\nI currently reside at " + Address + ".\nI am " + Gender + " by gender and my religion is " + Religion + "." + "\nMy nationality is " + Nationality + ", and I hold " + Citizenship + " citizenship" + ".\nIt is " ,isMarried, "that I am married and my civil status is " + CivilStatus + ".\nMy height is" ,Height, "in cm and I weigh" ,Weight,"in kg." + "\nMy father is " + NameofFather + ", works as a " + OccupationofFather + ".\nHe can be reached at " ,ContactNumberofFather,"\b.\nMy mother name is " + NameofMother + ", is employed as a " + OccupationofMother + "\b.\nShe can be reached at " ,ContactNumberofMother, "\nIn terms of my Educational Background,\nI completed my elementary education at " + Elementary + " from " ,YearAttendedElementary,"to",YearEndedElementary,"\b.\nI then attended High School in " + HighSchool + " from " ,YearAttendedHighSchool,"to",YearEndedHighSchool,"\b.\nI pursued higher education at " + College + ", where I studied " + Course + ".\nI have developed skills in " + Skills + ".\nDeveloping these skills will help me navigate complex situations, enhance my professional growth,\nand contribute more effectively goals.") 


    #ACT 4
    Number1 = eval(input("Enter a number --->"))
    Number2 = eval(input("Enter a number --->"))
    answer = Number1 + Number2
    print("The sum of", Number1, "and", Number2, "is", answer)


def arith_func():
    
    #ACT 5
    print("Fahrenheit to Celcius")
    temp=eval(input('\nEnter Temperature in Fahrenheit: '))
    celsius=(temp - 32) * 5/9
    print(f'\n\nThe conversion of {temp} degrees Fahrenheit is {celsius} degrees Celsius\n\nor')
    print(f'\nThe conversion of {temp} degrees Fahrenheit is {round(celsius, 2)} degrees Celsius')

    #ACT 6
    x=5
    print(x)
    x=x+10 
    print(x)
    x=x+15 
    print(x)
    x += 20 
    print(x)
    x=25 
    print(x)

def nes_condi():

    #ACT 7
    gold = 0

    miner = input("What is your name: ")

    isGold = input("Did you mine gold today?")

    if isGold.lower()=="yes":
        gold += 1
        print(f"Hi {miner}, Today you have a total of {gold} gold.")
    else: 
        print(f"Hi {miner}, Today you have a total of {gold} gold.")

    #ACT 8
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

    #ACT 9
    age = eval(input("Enter age: "))

    if age >=1 and age <=7:
        print(f"Toddler")
    elif age >=8 and age <= 13:
        print(f"Pre Teen")
    elif age >=14 and age <=18:
        print(f"Teenager")
    elif age >=19 and age <=31:
        print(f"Early Adulthood")
    elif age >=32 and age <=45:
        print(f"Mid Adulthood")
    elif age >=46 and age <=59:
        print(f"Post Adulthood")
    elif age >=60 and age <=150:
        print(f"Senior")

    #ACT 10
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

def for_loop():

    #ACT 11
    for hannie in range(1,5):
	print("hanniehae")
	name = input("Hi! Please input your name: ")
	print(f"Hi {name}")

    #ACT 12
    for k in range(1,10,3):
	print(k)

    #ACT 13
    print("Factorial\n")

    f = eval(input("Enter any number to factor: "))
    outcome = 1
    for x in range(f, 0, -1):
        outcome *= x

    print(f"The Factorial of {f} is {outcome} ")

    #ACT 14
    for k in range (0,11):
	for y in range(0,11):
		print("*", end="")
	print()

    #ACT 15
    for k in range (0,11):
	print(k, end="")
	for y in range(0,k):
		print("*", end="")
	print("")

    #ACT 16
    for x in range(1,6):
    for y in range(1, x + 1):
        print(" ", end = " ")
    for z in range(6, x, -1):
        print("^",end=" ")
    for k in range(6, x, -1):
        print("*",end=" ")
    print()

    #ACT 17
    col = eval(input("Enter number of columns: "))

    for x in range(1, 11):
        for y in range(1,col + 1):
            print(f"{x} x {y} = {x*y}",end = "\t")
        print()

    #ACT 18
    no = eval(input("Enter number of triangles: "))
    for x in range(1, 5):
        for k in range(1,no + 1):
            for z in range(1,x + 1):
                print("*", end= " ")

            for e in range(5, x, -1):
                print(" ", end=" ")
        print()

def while_loop():

    #ACT 19
    tuloy = True
    while tuloy == True:
        name = input("Please enter a name: ")

        if name.lower() == "stop":
            print("Program Terminated")
            break
            tuloy = False
        else:
            continue

    #ACT 20
    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no): ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        else:
            no += 1
            for x in range(1, 5):
                for r in range(1,no + 1):
                    for y in range(1,x + 1):
                        print("*", end= " ")

                    for z in range(5, x, -1):
                        print(" ", end=" ")
                print()
            continue

    #ACT 21
    def pang_hello():
    print("Hello Kyzel")

    def pang_hello_v2(name):
        print(f"Hello {name}")

    def activity2():
        num1 = eval(input("Enter a number: "))
        num2 = eval(input("Enter a number: "))
        answer = num1 + num2
        print(num1 , " plus " , num2 , " = " , answer)

    tuloy = True
    while tuloy == True:
        ask = input("Please provide a name: ")

        if ask.lower() != "stop":
            pang_hello_v2(ask)
            if ask.lower() == "2":
                activity2()
            continue
        
        else:
            break

    #ACT 22
    pass

    #ACT 23
    def factorial(number):
    fact = 1
    for k in range(number, 0, -1):
        fact *= 1
    return fact

    #ACT 24
    from Activity23 import factorial

    print(f"The Factorial of 4 is {factorial(4)}")

def listing():
    #ACT 25
    # Python list
    fruits = ["apples", "banana", "oranges", "star apple", "grapes"]
    print(fruits)

    #Indexing / Index - address / location of an item inside a list 
    #           0       1           2           3           4
    #fruits = ["apples", "banana", "oranges", "star apple", "grapes"]
    print(f"My favorite childhood fruit is {fruits[3]}")

    print(f"The last item on the list is {fruits[-1]}")

    #adding another item on the list
    fruits.append("longgan")
    print(fruits)
    fruits.append("strawberry")
    print(fruits)
    #inserting item on a specific index
    fruits.insert(3, "strawberry")
    print(fruits)
    fruits.remove("longgan")
    print(fruits)

    while True:
        fruits = input("Do you wish to add more fruits: ")

        if fruits.lower() == "no":
            print(fruits)
            break
        else:
            fruits.append(fruits)
            print("Fruit added to list ")
            continue
