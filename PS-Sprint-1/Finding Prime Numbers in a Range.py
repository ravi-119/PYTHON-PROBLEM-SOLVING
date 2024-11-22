# Write a program to find all prime numbers within a given range.

def is_Prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1 ):
        if num%i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1 ):
        if is_Prime(num):
            primes.append(num)
    return primes


start = int(input("Enter the starting point of the range : "))
end = int(input("Enter the ending point of the range : "))

prime_numbers = find_primes_in_range(start, end)
print(f"Prime numbers between {start} and {end} : {prime_numbers}")

