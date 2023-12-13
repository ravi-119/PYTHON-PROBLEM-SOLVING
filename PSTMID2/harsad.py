# Harsad number
num = int(input("Enter a number : "))
sumofdigit = 0
temp = num

while temp > 0:
    digit = temp % 10
    sumofdigit = sumofdigit + digit
    temp = temp // 10

if num % sumofdigit == 0:
    print("It is a Harsad number")
else:
    print("It is not a Harsad number")
