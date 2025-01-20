# Finding the Average of Numbers in an Array

# Defining a function to calculate average of numbers in a given array 
def calculate_average(numbers):
    # Handle empty array
    if len(numbers) == 0:
        return 0 
    # Step 1: Sum the elements 
    total_sum = sum(numbers) 
    # Step 2: Count the elements
    count = len(numbers) 
    # Step 3: Calculate the average     
    average = total_sum / count 
    return average


# Example usage:
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("The average is:", average)
