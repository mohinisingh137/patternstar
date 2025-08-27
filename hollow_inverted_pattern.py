rows = 5
for i in range(rows):
    print("*", end=" ")
    for j in range(rows - i - 1):
        print(" ", end=" ")
    print("*")
