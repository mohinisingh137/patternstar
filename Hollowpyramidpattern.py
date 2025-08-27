
N = int(input("Enter the row: "))
for i in range(1, N+1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2*(N-i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
