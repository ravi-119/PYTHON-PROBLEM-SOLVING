# Finding the Sum of Squares of Digits

# Function to calculate the sum of squares of digits
def sum_of_squares_of_digits(number):
    number = abs(number)  # Ensure the number is positive
    total = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        total += digit ** 2  # Add the square of the digit
        number //= 10  # Remove the last digit
    return total

# Input from the user
num = int(input("Enter a number: "))

# Call the function and display the result
result = sum_of_squares_of_digits(num)
print(f"The sum of the squares of the digits of {num} is {result}")

