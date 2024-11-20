# Write a program to sort an array of numbers in ascending order.

# Function Definition
def sort(numbers):
    # Finding the Length of the Array
    n = len(numbers)

    # Outer Loop 
    # This is used to determine the range for iteration.
    for i in range(n):

        # Inner Loop
        # The inner loop iterates through the unsorted portion of the array.
        # n - i - 1 ensures that the sorted portion (end of the array) is excluded from comparisons.
        for j in range(0, n - i - 1):

            # Comparing Adjacent Elements
            if numbers[j] > numbers[j + 1]:

                # Swapping Elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Returning the Sorted Array            
    return numbers

array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = sort(array)
print("Sorted array is : ", sorted_array)

