tuloy = True
a = 0
while tuloy == True:
    number = eval(input("Enter a number: "))
    if number == 0:
        print("Program Terminated")
        print(f"The total of the number you enter is {a}")
        break
    else:
        a += number
        continue