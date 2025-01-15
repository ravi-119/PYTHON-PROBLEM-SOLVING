# Finding the Count of Specific Digits in a Number

# Function Definition
def count_specific_digit(number, digit):

    # Convert Number and Digit to String
    number_str = str(abs(number))
    digit_str = str(digit)

    # Count Occurrences
    count = number_str.count(digit_str)
    return count

# calling the function 

# Taking number and digit from user as input
number = int(input(" Enter a number : "))
digit = int(input( " Enter a digit : "))

# Finally printing the result 
print(f"The digit {digit} appears {count_specific_digit(number, digit)} times in {number}.")



