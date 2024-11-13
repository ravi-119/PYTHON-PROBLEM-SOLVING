# Write a program to generate the Fibonacci series up to a given number.

num_terms = int(input(" Enter the number of terms : "))
a = 0
b = 1

if num_terms <= 0:
    print(" Please Enter a Valid number of terms ")

elif num_terms == 1:
    print("fibonacci serises up to ", num_terms,  "term : ")
    print(a)

else:
    print("fibonacci sequence :")
    for i in range(num_terms):
        print(a, end=" ")
        a,b = b, a+b 

