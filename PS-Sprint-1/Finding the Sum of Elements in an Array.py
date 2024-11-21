# Write a program to find the sum of elements in an array.

# Functions to calculate the sum of numbers in given in an array 
def sum_of_array(array):
    # initilize a variable to store the sum of numbers 
    total = 0 
    # iterating one by one element in the given array 
    for num in array:
        # After iterating one by one element with help of loop and adding in total simultenously 
        total = total + num
    # finally returning the total  
    return total 

# Finally calling the function 
array = [1, 2, 3, 4, 5]
result = sum_of_array(array)
print("Given array : ", array)
print("The toatal of the given number in an array : ", result )


