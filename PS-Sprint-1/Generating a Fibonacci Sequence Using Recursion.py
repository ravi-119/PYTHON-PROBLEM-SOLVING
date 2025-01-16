# Generating a Fibonacci Sequence Using Recursion

def fibonacci(n):
    """
    Recursive function to generate the nth Fibonacci number.
    :param n: The position of the Fibonacci number.
    :return: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
num = int(input("Enter the number of terms for the Fibonacci sequence: "))
print("Fibonacci sequence:")
for i in range(num):
    print(fibonacci(i))



    
