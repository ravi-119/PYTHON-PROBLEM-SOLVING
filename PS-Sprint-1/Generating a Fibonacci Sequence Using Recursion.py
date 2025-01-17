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



    
"""
    Example walkthrough (if num == 6 ):
    iteartion 1 (i = 0 ): fibonacci(0) = 0 -> Print 0.
    iteartion 2 (i = 1 ): fibonacci(1) = 1 -> Print 1.
    iteartion 3 (i = 2 ): fibonacci(2) =  fibonacci(1) +  fibonacci(0) = 1 + 0 = 1 -> Print 1.
    iteartion 4 (i = 3 ): fibonacci(3) =  fibonacci(2) +  fibonacci(1) = 1 + 1 = 2 -> Print 2.
    iteartion 5 (i = 4 ): fibonacci(4) =  fibonacci(3) +  fibonacci(2) = 2 + 1 = 3 -> Print 3.
    iteartion 6 (i = 5 ): fibonacci(5) =  fibonacci(4) +  fibonacci(3) = 3 + 2 = 5 -> Print 5.
    
"""








