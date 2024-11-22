# Write a program to generate multiplication tables for a given number.

def multiplication_table(number, limit=10):
    print(f"Multiplication table for {number}")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number*i}")

number = int(input("Enter the number to generate its multiplication table : "))
limit = int(input("Enter the limit for the table (default is 10): "))
multiplication_table(number, limit)




