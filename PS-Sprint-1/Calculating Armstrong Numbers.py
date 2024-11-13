# Write a program to check if a number is an Armstrong number.

num = int(input("Enter a number : "))

digits = str(num)
num_digits = len(digits)

total = 0 

for digit in digits:
    total += int(digit) ** num_digits

if total == num:
    print( f"{num} is a armstrong number" )
else:
    print( f"{num} is not a armstrong number" )



