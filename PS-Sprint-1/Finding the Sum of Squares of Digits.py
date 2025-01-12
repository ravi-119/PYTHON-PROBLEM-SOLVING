# Finding the Sum of Squares of Digits

# Function to calculate the sum of squares of digits
def sum_of_squares_of_digits(number):
    # Ensure the number is positive
    number = abs(number)  
    total = 0
    while number > 0:
        # Get the last digit
        digit = number % 10 
        # Add the square of the digit
        total += digit ** 2  
        # Remove the last digit
        number //= 10  
    return total

# Input from the user
num = int(input("Enter a number: "))
# Call the function and display the result
result = sum_of_squares_of_digits(num)
print(f"The sum of the squares of the digits of {num} is {result}")
