# Generating a Pascal’s Triangle
def generate_pascals_trangle(rows):
    trangle = []
    for i in range(rows):

        # Every row starts with 1
        row = [1]

        # If the triangle is not empty (i > 0)
        if trangle:

            # Get the last row
            last_row = trangle[-1]

            # Generate the middle values by summing pairs from the last row
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j+1])

            # End each row with 1
            row.append(1)

        # Add the new row to the triangle
        trangle.append(row)

    return trangle

# calling function to print pascal's trangle 
row = 4
trangle = generate_pascals_trangle(row)
for row in trangle:
    print(' '.join(map(str, row)))



    