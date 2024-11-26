# Write a program to generate number patterns (e.g., sequential numbers in a matrix).

def generate_pattern(rows):
    num = 1

    # This loop is for each rows
    for i in range(1, rows + 1):

        # this loop is for Numbers in each row 
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1

        # New line after each row 
        print()


# Finally calling the function 
generate_pattern(4)


# rows = int(input("Enter the no of rows to generate pattern : "))
# print(f"{generate_pattern(rows)}")

