# Write a program to calculate the sum of digits of a number.

num = int(input("Enter the Number : "))
sum = 0 

while num > 0:
    # Add the digit to the sum 
    sum = sum + num % 10

    # Remove the digit 
    num = num // 10
print(sum)


