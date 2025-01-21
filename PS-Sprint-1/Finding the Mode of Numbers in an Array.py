# Finding the Mode of Numbers in an Array

# Importing Counter method from collections 
from collections import Counter

# Defining a function for finding mode 
def find_mode(arr):
    # Count occurrences of each number
    count = Counter(arr)
    # Find the maximum frequency
    max_frequency = max(count.values())
    # Find all numbers with the maximum frequency
    mode = [num for num, freq in count.items() if freq == max_frequency]
    return mode


# Example usage
numbers = [1, 2, 2, 3, 3, 4]
modes = find_mode(numbers)
print("Mode(s):", modes)