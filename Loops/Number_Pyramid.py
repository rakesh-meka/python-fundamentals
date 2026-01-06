# Number pyramid using loops

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    for num in range(1, i + 1):
        print(num, end="")
    for num in range(i - 1, 0, -1):
        print(num, end="")
    print()
