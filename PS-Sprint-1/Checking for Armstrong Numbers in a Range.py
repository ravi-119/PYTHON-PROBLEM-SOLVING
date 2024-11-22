# Write a program to find all Armstrong numbers within a given range.

# Defining a function to check a number is armstrong or not 
def armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == number 

# Defining a function to check armstrong numbers in a range 
def find_armstrong_number(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Taking a number from user 
start = int(input("Enter a starting point number: "))
end = int(input("Enter a ending point: "))

armstrong_numbers = find_armstrong_number(start, end)
if armstrong_numbers:
    print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers}")
else:
    print(f"No Armstrong numbers found between {start} and {end}.")



# Program to find all Armstrong numbers within a given range

# def is_armstrong(number):
#     """Check if a number is an Armstrong number."""
#     digits = str(number)
#     num_digits = len(digits)
#     sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
#     return sum_of_powers == number

# def find_armstrong_numbers(start, end):
#     """Find all Armstrong numbers within a given range."""
#     armstrong_numbers = []
#     for num in range(start, end + 1):
#         if is_armstrong(num):
#             armstrong_numbers.append(num)
#     return armstrong_numbers

# # Example usage

# # Input range from the user
# start = int(input("Enter the starting number of the range: "))
# end = int(input("Enter the ending number of the range: "))
    
# # Find and display Armstrong numbers
# armstrong_numbers = find_armstrong_numbers(start, end)
# if armstrong_numbers:
#     print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers}")
# else:
#     print(f"No Armstrong numbers found between {start} and {end}.")

