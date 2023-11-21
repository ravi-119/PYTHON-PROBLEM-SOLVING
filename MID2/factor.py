# program for factor 
num = int(input("Enter a number"))
factor = []
for i in range(1, num + 1):
    if num % i == 0:
        factor.append(i)
    print(factor)



