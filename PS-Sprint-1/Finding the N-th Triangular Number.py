# Finding the N-th Triangular Number

def nth_triangular_number(num):
    """
    Calculate the N-th triangular number.

    Parameters:
    n (num): The position of the triangular number.

    Returns:
    int: The N-th triangular number.
    """

    if num < 1:

        return " N must be a positive integer."
    return num * (num + 1) // 2
    
num = int(input(" Enter a number to finding N-th triangular number : "))
print(f" The N-th triangular number is {nth_triangular_number(num)}")