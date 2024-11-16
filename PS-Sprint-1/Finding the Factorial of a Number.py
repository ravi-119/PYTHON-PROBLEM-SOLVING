# Write a program to compute the factorial of a given number.

def factorial(n):
    result = 1
    if n < 0:
        print("Invalid Input ")
    else:
        for i in range(1, n+1 ):
            result = result * i 
    print("Factorial of ",f'{n} is :', result)

n = int(input("Enter a Number: "))
factorial(n)

