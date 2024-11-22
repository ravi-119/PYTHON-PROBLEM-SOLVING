# Write a program to determine if a number is a perfect number.

def perfect_number(num):
    sum_of_proper_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_proper_factors = sum_of_proper_factors + i

    if sum_of_proper_factors == num:
        print(f"The number {num} is a perfect number")
    else:
        print(f"The number {num} is not a perfect number")

Number = int(input("Enter a number to check weather it a perfect number or not : "))
perfect_number(Number)




