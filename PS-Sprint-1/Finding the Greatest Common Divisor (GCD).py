# Write a program to find the GCD of two numbers.

num1 = int(input(" Enter the first number: "))
num2 = int(input(" Enter the second number: "))

if num1 > num2:
    min = num2 
else:
    min = num1

for i in range(1, min+1):
    if num1 % i == 0 and num2 % i == 0:
        HCF = i 
print("The HCF of", f"{num1, num2} is :", HCF)
