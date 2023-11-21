num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
sum1 = 0
sum2 = 0
for i in range(1, num1):
    if num1 % i == 0:
        sum1 += i

for i in range(1, num2):
    if num2 % i == 0:
        sum2 += i

if sum1 == num2 and sum2 == num1:
    print("Amicable number")
else:
    print("Not a Amicable number")





num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_divisors_num1 = 0
sum_divisors_num2 = 0

for i in range(1, num1):
    if num1 % i == 0:
        sum_divisors_num1 += i

for i in range(1, num2):
    if num2 % i == 0:
        sum_divisors_num2 += i

if num1 == sum_divisors_num2 and num2 == sum_divisors_num1:
    print("amicable number")
else:
    print("Not amicable number")
