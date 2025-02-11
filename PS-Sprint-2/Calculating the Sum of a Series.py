# Define a function to compute the harmonic sum
def harmonic_sum(n):  
    total = 0  # Initialize sum variable
    for k in range(1, n + 1):  # Loop from 1 to n
        total += 1 / k  # Add the reciprocal of k to the sum
    return total  # Return the final sum

# Take user input and convert it to an integer
n = int(input("Enter a number: "))  

# Compute the harmonic sum and print the result
print(f"Harmonic sum for n={n}: {harmonic_sum(n)}")  



"""
Function Execution (harmonic_sum(4))
total = 0
k = 1: total += 1 / 1 = 1.0
k = 2: total += 1 / 2 = 1.0 + 0.5 = 1.5
k = 3: total += 1 / 3 = 1.5 + 0.3333 = 1.8333
k = 4: total += 1 / 4 = 1.8333 + 0.25 = 2.0833
Final total = 2.0833
"""
