# Write a program to find the LCM of two numbers.
# Least Common Multiple  

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    max = num1
else:
    max = num2

while(True):
    if (max % num1 == 0 and max % num2 == 0 ):
        break 
    max = max + 1
print(" The LCM of", f"{num1, num2} is : ", max) 







