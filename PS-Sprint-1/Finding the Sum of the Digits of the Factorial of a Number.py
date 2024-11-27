# Write a program to find the sum of the digits of the factorial of a given number.

# importing math module
import math

def sum_of_digits_of_factorial(num):
    # Calculate the factorial of the number
    factorial = math.factorial(num)
    # Convert the factorial to a string, sum up the digits
    return sum(int(digit) for digit in str(factorial))


# Finally Calling the function 
number = int(input("Enter a Number : "))
result = sum_of_digits_of_factorial(number)
print(f"Sum of digits of factorial of {number} is {result}")
