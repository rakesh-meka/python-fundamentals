# Program to count frequency of characters in a string

text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:")
for key, value in frequency.items():
    print(key, ":", value)
