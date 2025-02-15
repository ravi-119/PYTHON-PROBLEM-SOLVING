# Finding All Pairs of Elements in an Array that Add Up to a Given Sum

# Defining the function with two parameter that is array and target
def find_pairs(array, target):
    # Initializing an Empty List to Store Pairs
    pairs = []
    # Finding the length of Array 
    n = len(array)
    # Iterating Through all Elements using Nested loop
    for i in range(n):
        for j in range(i+1, n):
            # Checking the sum of two indexes sum is equal or not 
            if (array[i] + array[j] == target):
                # if the sum is equal to target then append the indexes element in pairs list 
                pairs.append((array[i], array[j]))
    # finally returning the pairs as final output
    return pairs
# Finally calling the function 
array = [1, 2, 3, 4, 5]
target = 5
print(find_pairs(array, target))

"""
Output
[(1, 4), (2, 3)]

"""


