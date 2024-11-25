# Write a program to find the Fibonacci number at a specific position.

def fibonacciNumber_specificPosition(n):
    # First of all checking at 0th index
    if n <= 0:
        return 0
    # Checking at the 1st index
    elif n == 1:
        return 1
    # Checking further indexes
    prev, curr = 0, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr

# Finally calling the function 
position  = int(input("Enter the position : "))
print(f"The fibonacci number at position {position} is {fibonacciNumber_specificPosition(position)}")

