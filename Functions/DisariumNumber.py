#Q: Check Whether a Number is a Disarium Number (Using Function)g

def is_disarium(num):
    total = 0
    digits = str(num)

    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)

    return total == num

#Note: 
# A number is called a Disarium number if the sum of its digits powered with their respective positions equals the number itself.

# User input
number = int(input("Enter a number: "))

# Function call
if is_disarium(number):
    print(number, "is a Disarium Number")
else:
    print(number, "is NOT a Disarium Number")

