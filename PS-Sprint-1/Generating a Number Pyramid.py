# Generating a Number Pyramid

# This line prompts the user to input the number of rows they want in the pattern.
rows = int(input(" Enter the rows : "))
# This is the outer loop that controls the number of rows in the pattern.
for i in range(rows):
    # This is the inner loop that controls the numbers printed on each row.
    for j in range(i+1):
        # This prints the number j+1  on the current row, without moving to the next line.
        print(j+1, end=" ")
    print()

"""
Output 
1 
1 2 
1 2 3 
1 2 3 4 

"""