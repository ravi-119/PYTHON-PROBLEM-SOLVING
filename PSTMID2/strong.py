num = int(input("Enter a number : "))
sumoffactorial = 0
temp = num

while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit+1):
        factorial = factorial*i
    sumoffactorial = sumoffactorial + factorial
    temp //= 10

if sumoffactorial == num:
    print("It is a strong number")
else:
    print("It is not a strong number")



