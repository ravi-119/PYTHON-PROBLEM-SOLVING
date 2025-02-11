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
