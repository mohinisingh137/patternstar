rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print("_", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
