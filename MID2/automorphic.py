num = int(input("Enter a number"))
square = num**2

str_num = str(num)
square_num = str(square)

if square_num.endswith(str_num):
    print("Number is Automorphic")
else:
    print("Number is not a Automorphic number")


