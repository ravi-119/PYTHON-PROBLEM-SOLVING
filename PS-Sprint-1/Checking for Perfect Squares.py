# Checking for Perfect Squares

import math

def is_perfect_square(number):
    """
    Check if a number is a perfect square.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if the number is a perfect square, False otherwise.
    """
    if number < 0:
        # Negative numbers cannot be perfect squares
        return False 
    # Get the integer square root 
    sqrt = math.isqrt(number)  
    return sqrt * sqrt == number

# Example usage

num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")