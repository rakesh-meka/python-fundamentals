#Check whether a number is palindrome
 
num = int(input("Enter a number: "))

temp = abs(num)   # remove minus sign
original = temp
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if original == reverse:
    print("Palindrome Number (ignoring sign)")
else:
    print("Not a Palindrome")
