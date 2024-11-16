# Write a program to create different star patterns (e.g., pyramid, diamond).

def pyramid(n):
    # The outer loop represents the no of rows 
    for i in range(1, n+1):

        # The first internal loop represents to print the no of spaces
        for j in range(n-i):
            print(" ", end="")

        # The second internal loop represents to print the no of astrisks 
        for k in range(1, 2*i):
            print("*", end="")

        print()

# And Finathelly caling  functions 
n = int(input("Enter no of height: "))
pyramid(n)




         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************








    


