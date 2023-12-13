# automorphic number 
num = int(input("Enter a number : "))
square = num ** 2


# change num and square into string 
str_num = str(num)
str_square = str(square)

if str_square.endswith(str_num):
    print("This is a automorphic number")
else:
    print("This is not a automorphic number")
