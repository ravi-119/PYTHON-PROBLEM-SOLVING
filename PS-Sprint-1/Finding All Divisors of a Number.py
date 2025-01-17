# Finding All Divisors or factor of a Number

# Taking a number from user as an input
num = int(input(" Enter a number : "))
# init a factor variable to store factors 
factor = []

# iterating from one to num 
for i in range(1, num+1):
    # checking condition 
    if num % i == 0:
        factor.append(i)
# Printing the result 
print(factor)
