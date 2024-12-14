import os
isContinue = True
no = 0
while isContinue == True:
    ask = input("Would you like to add another triangle (yes / no): ")
    if ask.lower() == "no":
        print("Program Terminated")
        break
        isContinue = False
    elif ask.lower() == "yes":
        os.system('cls')
        no += 1
        for x in range(1, 6):
            for r in range(1,no + 1):
                for y in range(1,x + 1):
                    print("*", end=" ")

                for z in range(5, x, -1):
                    print(" ",end=" ")
                print()
            else:
                print("Invalid Answer, it's only (yes / no)")
                continue