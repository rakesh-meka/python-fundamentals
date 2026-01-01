# Menu Driven Program using Loops
# Author: Rakesh Meka
# Purpose: Demonstrate while loop and conditional logic

while True:
    print("\n====== MENU ======")
    print("1. Check Even or Odd")
    print("2. Find Factorial")
    print("3. Reverse a Number")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

    elif choice == 2:
        num = int(input("Enter a number: "))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print(f"Factorial of {num} is {fact}")

    elif choice == 3:
        num = int(input("Enter a number: "))
        rev = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10
        print(f"Reverse of {num} is {rev}")

    elif choice == 4:
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")
