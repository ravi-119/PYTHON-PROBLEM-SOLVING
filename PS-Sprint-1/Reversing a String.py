# Write a program to reverse a given string.

def reverse_string (input_string):
    # reverse the string using slicing 
    return input_string[: : -1]


user_input = input("Enter a string to revers : ")
reversed_string = reverse_string(user_input)
print(f"Reversed string : {reversed_string}")

