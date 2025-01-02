# write a program to Finding the Largest Palindrome in a String

# Function Definition
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]
               

def find_largest_palindrome(s):
    if len(s) == 0:
        return ""

    largest_palindrome = ""
    
    for i in range(len(s)):
        # Check for odd-length palindromes (single center)
        odd_palindrome = expand_around_center(s, i, i)
        # Check for even-length palindromes (double center)
        even_palindrome = expand_around_center(s, i, i + 1)

        # Get the larger of the two
        larger_palindrome = odd_palindrome if len(odd_palindrome) > len(even_palindrome) else even_palindrome

        # Update the result if the new palindrome is larger
        if len(larger_palindrome) > len(largest_palindrome):
            largest_palindrome = larger_palindrome

    return largest_palindrome



# Example usage
if __name__ == "__main__":
    test_string = "babad"
    result = find_largest_palindrome(test_string)
    print(f"Largest palindrome in '{test_string}' is: '{result}'")


