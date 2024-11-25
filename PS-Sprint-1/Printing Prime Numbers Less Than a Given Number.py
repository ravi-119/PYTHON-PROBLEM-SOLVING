# Write a program to print all prime numbers less than a given number.

def is_Prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes_below_n(limit):
    prime_number = []
    for num in range(2, limit):
        if is_Prime(num):
            prime_number.append(num)
    return prime_number


limit = int(input("Enter a Number : "))
print(f"Prime Numbers less than {limit} are : {primes_below_n(limit)}")


    
    