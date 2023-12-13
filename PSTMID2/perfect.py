# perfect number 
num = int(input("Enter a number : "))
sumofdivisors = 0

for i in range(1, num):
    if num % i == 0:
        sumofdivisors = sumofdivisors + i

if sumofdivisors == num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")


    