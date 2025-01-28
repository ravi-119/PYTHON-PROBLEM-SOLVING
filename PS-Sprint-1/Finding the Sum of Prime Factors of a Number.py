# Finding the Sum of Prime Factors of a Number
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    
def prime_factors_sum(number):
    """Find the sum of the prime factors of a given number."""
    sum_of_primes = 0
    factor = 2

    while number > 1:
        if number % factor == 0:
            if is_prime(factor):
                sum_of_primes += factor
            number //= factor
        else:
            factor += 1

    return sum_of_primes

# Example usage:
num = int(input("Enter a number: "))
result = prime_factors_sum(num)
print(f"The sum of the prime factors of {num} is {result}")
