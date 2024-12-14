name = input("Please enter your name: ")

deposit = eval(input("Please enter amount to deposit: "))

one_th = deposit // 1000

one_th1 = deposit % 1000

five_h = one_th1 // 500

five_h1  = one_th1 % 500

two_h = five_h1 // 200

two_h1 = five_h1 % 200

one_h = two_h1 // 100

one_h1 = two_h1 % 100

fifty = one_h1 // 50

fifty1 = one_h1 % 50

twenty =  fifty1 // 20

twenty1 = fifty1 % 20

ten = twenty1 // 10

ten1 = twenty1 % 10

five = ten1 // 5

five1 = ten1 % 5

one = five1 // 1

print("Hi,", name,  "the breakdown of your deposit is: ")

print(one_th, "-1000")

print(five_h, "-500")

print(two_h, "-200")

print(one_h, "-100")

print(fifty, "-50")

print(twenty, "-20")

print(ten, "-10")

print(five, "-5")

print(one, "-1")