# Write a program to find the largest and smallest numbers in an array.

def largest_smallest_num(numbers):

    largest = numbers[0]
    smallest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num 
    return largest, smallest

array = [10, 30, 45, 56, 89, 65]
largest, smallest = largest_smallest_num(array)
print(f"Largest and Smallest element in given array : {largest}")
print(f"Largest and Smallest element in given array : {smallest}")

