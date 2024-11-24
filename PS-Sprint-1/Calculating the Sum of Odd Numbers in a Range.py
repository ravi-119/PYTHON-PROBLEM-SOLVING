# Write a program to find the sum of all odd numbers within a given range.

def sum_of_odd_numbers(start, end):
    # Ensure the start value is odd
    if start % 2 == 0:
        start += 1
    # Calculate the count of even numbers (n)
    n = ((end - start) // 2) + 1

    # Use the arithmetic series formula to calculate the sum
    # (start + (n - 1) * 2) formula for last term 
    total_sum = n * (start + (start + (n - 1) * 2)) // 2
    return total_sum




# Finally calling the function 

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start > end:
    print("Invalid range! Start should be less than or equal to End.")
else:
    odd_sum = sum_of_odd_numbers(start, end)
    print(f"The sum of all odd numbers between {start} and {end} is: {odd_sum}")


