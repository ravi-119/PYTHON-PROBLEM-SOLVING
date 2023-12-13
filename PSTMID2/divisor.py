# find out divisor of a number // proper factor
num = int(input("Enter a number : "))
sumofdivisors = []

for i in range(1, num):
    if num % i == 0:
        sumofdivisors.append(i)
print(sumofdivisors)


