# amicable number
num1 = int(input("Enter the first num : "))
num2 = int(input("Enter the second num : "))
sum1 = 0
sum2 = 0

for i in range(1, num1):
    if num1 % i == 0:
        sum1 = sum1 + i

for i in range(1, num2):
    if num2 % i == 0:
        sum2 = sum2 + i 

if sum1 == num2 and sum2 == num1:
    print("This is amicable/friendly pairs number")
else:
    print("This is not amicable/friendly pairs number")