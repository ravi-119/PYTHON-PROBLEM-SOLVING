# Generating a Multiplication Table for a Range

# Defining the function with parameter like starting ending and upto 
def generate_multiplication_table_given_range(start, end, upto):

    # iterating through starting point to ending point 
    for num in range(start, end+1):

        # Printing this statement 
        print(f"\n multiplication table for {num} : \n" + "-" * 25)

        # Iterating through 1 to given upto number 
        for i in range(1, upto+1):

            # Finally Printing the multiplication table 
            print(f"{num} x {i} = {num * i}")

        # Printing a line to sepeate the table 
        print("-"*25)
        
# Finally calling the function to print the table 
start_num = int(input("Enter the start num : "))
end_num = int(input("Enter the ending num : "))
upto = int(input("Enter the upto num : "))
generate_multiplication_table_given_range(start_num, end_num, upto)


"""
Enter the start num : 1
Enter the ending num : 5
Enter the upto num : 10

 multiplication table for 1 : 
-------------------------
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
-------------------------

 multiplication table for 2 : 
-------------------------
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
-------------------------

 multiplication table for 3 : 
-------------------------
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
-------------------------

 multiplication table for 4 : 
-------------------------
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
-------------------------

 multiplication table for 5 : 
-------------------------
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
-------------------------
"""


