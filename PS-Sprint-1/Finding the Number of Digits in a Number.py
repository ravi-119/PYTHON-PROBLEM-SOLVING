# Write a program to count the number of digits in a given number.

# Taking a number as an Input from user 
number = int(input("Enter a Number : "))

# Coverting number into string 
digits = str(number)

# Checking length of digits and storing in a new veriable that is num_digits
num_digits = len(digits)

# Finally printing the number of digits 
print(f"The no of digits in the {number} is : {num_digits}")

