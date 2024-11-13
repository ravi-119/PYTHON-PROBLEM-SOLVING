# Write a program to check if a string or number is a palindrome.

# Input: number to check
number = int(input("Enter a number: "))
original_number = number
reversed_number = 0

# Reverse the number using a while loop
while number > 0:
    # Get the last digit
    digit = number % 10  
    # Append the digit to the reversed number         
    reversed_number = reversed_number * 10 + digit 
    # Remove the last digit 
    number = number // 10          

# Check if the original number is equal to the reversed number
if original_number == reversed_number:
    print(f"{original_number} is a palindromic number.")
else:
    print(f"{original_number} is not a palindromic number.")


