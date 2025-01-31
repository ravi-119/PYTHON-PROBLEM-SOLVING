# Finding the Second Largest Number in an Array

def find_second_largest_number(arr):
    if len(arr) < 2:
        return "Array must have at least two elements"

    # Remove duplicates from the array
    unique_arr = list(set(arr))

    # Sort the array in descending order
    unique_arr.sort(reverse = True )

    # Return the second largest number
    if len(unique_arr) >= 2:
        return unique_arr[1]
    else:
        return " No second largest element "

# Calling the function 
arr = [10, 20, 4, 45, 99]
second_largest = find_second_largest_number(arr)
print(f"The second largest number is: {second_largest}")