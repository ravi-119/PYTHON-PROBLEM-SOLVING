# Calculating the Sum of Digits of a Number Until Single Digit

def Sum_of_Digits_of_a_Number_Until_Single_Digit(n):

    # Condition this checks if the input number n is 0.
    if n == 0:
        return 0
    # This formula leverages a property of numbers in modular arithmetic 
    return 1 + (n - 1) % 9

# Calling the Function 
number = int(input(" Enter a number: "))
print("the Sum of Digits of a Number Until Single Digit : ", Sum_of_Digits_of_a_Number_Until_Single_Digit(number))

