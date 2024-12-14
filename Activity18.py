no = eval(input("Enter number of triangles: "))
for x in range(1, 5):
    for k in range(1,no + 1):
        for z in range(1,x + 1):
            print("*", end= " ")

        for e in range(5, x, -1):
            print(" ", end=" ")
    print()