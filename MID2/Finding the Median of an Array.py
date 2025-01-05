# Finding the Median of an Array

# Defining a function to find median of odd numbers in an array
def find_median(arr):

    # sorting the array 
    arr.sort()

    # Checking the length of array 
    n = len(arr)

    # Finding the median value for odd numbers 
    if n % 2 == 1:
        return arr[ n // 2 ]
    
# calling Function 
array1 = [ 7, 3, 1, 9, 5 ]
print(" median of array1 : ", find_median(array1))

# Defining a function to find median of even numbers in an array
def find_median(arr):

    # sorting the array 
    arr.sort()

    # Checking the length of array 
    n = len(arr)

    # Finding the median value for even numbers 
    mid1 = arr[ n // 2-1 ]
    mid2 = arr[ n // 2 ] 
    return ( mid1 + mid2 ) // 2
  
    
# calling Function 
array1 = [ 8, 4, 6, 10 ]
print(" median of array1 : ", find_median(array1))


# Defining a function to find median of odd and even numbers in an array
def find_median(arr):

    # sorting the array 
    arr.sort()

    # Checking the length of array 
    n = len(arr)

    # Finding the median value for odd numbers 
    if n % 2 == 1:
        return arr[ n // 2 ]
    
    # Finding the median value for even numbers 
    else:
        mid1 = arr [ n // 2-1 ]
        mid2 = arr [ n // 2 ]
        return (mid1 + mid2 ) // 2
    
# calling Function 
array1 = [ 7, 3, 1, 9, 5 ]
array2 = [ 8, 4, 6, 10 ]

print(" median of array1 : ", find_median(array1))
print(" median of array2 : ", find_median(array2))