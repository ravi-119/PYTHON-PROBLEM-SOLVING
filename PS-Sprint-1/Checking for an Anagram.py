# Checking for an Anagram

def is_anagram(str1, str2):
    # Remove spaces and convert into lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Short the Characters and compare
    return sorted(str1) == sorted(str2) 

# Calling the function 
string1 = str(input(" Enter string1: "))
string2 = str(input(" Enter string2: "))
if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")


    