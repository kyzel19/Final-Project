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