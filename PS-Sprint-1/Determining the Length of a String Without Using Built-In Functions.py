# Determining the Length of a String Without Using Built-In Functions

# Defining a function for checking the length of a string without using any in built function
def length_of_string(string):
    # init a variable count
    count = 0 
    # Itreating through every character in string 
    for s in string:
        # Updating the count variable 
        count += 1
    # Finally returning the count 
    return count

# calling the function 
s1 = str(input(" Enter a string : "))
print(f" The length of the string is : {length_of_string(s1)}")



