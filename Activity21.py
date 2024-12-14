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