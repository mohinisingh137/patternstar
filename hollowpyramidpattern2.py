N = int(input("Enter the row: "))
for i in range(1, N+1):
    for j in range(i,N+1):
        print("*", end=" ")
    for j in range(2*i-2):
        print(" ", end=" ")
    for j in range(i,N+1):
        print("*", end=" ")
    print()
