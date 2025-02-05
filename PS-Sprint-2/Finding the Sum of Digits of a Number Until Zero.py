# Finding the Sum of Digits of a Number Until Zero

def sum_of_digits_until_zero(n):
    while n >= 10:  
        digit_sum = 0  # Initialize sum of digits
        for digit in str(n):  # Iterate through each digit
            digit_sum += int(digit)  # Convert to integer and add to sum
        n = digit_sum  # Update n with the new sum
    return n  # Return the final single-digit sum

# Example usage:
num = int(input("Enter a number: "))  # Get user input and convert to integer
result = sum_of_digits_until_zero(num)  # Call function to compute result
print(f"Sum of digits until a single digit: {result}")  # Print final output
