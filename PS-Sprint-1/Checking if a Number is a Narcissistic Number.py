# Write a program to check if a number is a narcissistic number (where the sum of its digits raised to the power of the number of digits equals the number itself).

def is_narcissistic(num):

    digits = str(num)
    num_digits = len(digits)

    total = 0 
    for digit in digits:
        total += int(digit) ** num_digits
    return total == num

number = int(input("Enter a nuumber to check wheather it is a narcissistic or not : "))
if is_narcissistic(number):
    print(f"The {number} is Narcissistic Number ")
else:
    print(f"The {number} is not Narcissistic Number ")


