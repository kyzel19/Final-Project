name = input("Enter your name :")
purchased_or_not = input("Did you purchase a grocery today? (Yes or No) :")

if purchased_or_not.lower() == "yes": 
    purchased = input("What did you purchase :")
else:
    print(exit("You didn't purchase a grocery today"))
   
orig_price = eval(input("Item Price :"))
age = int(input("Age :"))

#if purchased a grocery, product price would be taxed 12.3% added to the orig_price
#if the purchase is not more than four thousand
taxed_price = (orig_price * 0.123) + orig_price

#if purchase is more than four thousand, there will be a discount of 3.8%
discount = orig_price - (orig_price * 0.038) 
discount_taxed_price = orig_price - (discount * 0.123)

#if you are a senior not exceeding the age of 150, there will be a discount of 12.3%
discount_senior = orig_price - (taxed_price * 0.123)

#if senior and purchase is more than four thousand
two_discount = orig_price - (taxed_price * 0.161)

if age >= 60 and age <= 150 and orig_price >= 4000 :
   print(f'Total : {round(two_discount,2)}')
   payment = eval(input("Payment :"))
   print(f'Change : {round(payment - two_discount,2)}')
    
elif orig_price >= 4000 :
   print(f'Total : {round(discount_taxed_price, 2)} ')
   payment = eval(input("Payment :"))
   print(f'Change : {round(payment - discount_taxed_price, 2)} ')

elif age >= 60 and age <= 150 :
   print(f'Total : {round(discount_senior,2)} ')
   payment = eval(input("Payment :"))
   print(f'Change : {round(payment - discount_senior,2)} ')
    
else : 
    print(f'Total : {round(taxed_price,2)} ')
    payment = eval(input("Payment :"))
    print(f'Change : {round(payment - taxed_price,2)} ')
  