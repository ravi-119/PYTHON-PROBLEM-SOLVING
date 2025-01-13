# Generating a Square Matrix of a Given Size

def generate_square_matrix(size):
    if size <= 0:
        return "Size must be a positive integer."

    matrix = []
    number = 1

    for i in range(size):
        row = []
        for j in range(size):
            row.append(number)
            number += 1
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


size = int(input("Enter the size of the square matrix: "))
matrix = generate_square_matrix(size)
print("Generated Matrix:")
print_matrix(matrix)
