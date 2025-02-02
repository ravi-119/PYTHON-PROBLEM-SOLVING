# Finding the Longest Substring Without Repeating Characters

# Initialize Variables
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    # Iterate Through the String left to right
    for right in range(len(s)):
        # Check for Duplicates
        while s[right] in char_set:
            # Remove the leftmost character
            char_set.remove(s[left])
            # Move left pointer to shrink the window
            left += 1
        # Expand the Window and Update Maximum Length
        # Add new unique character to the set
        char_set.add(s[right])
        # Update max_length
        max_length = max(max_length, right - left + 1)
    # Return the Result
    return max_length



# Example Usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3 ("abc")
