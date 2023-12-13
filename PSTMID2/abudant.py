# Abudant number 
num = int(input("Enter a number : "))
sumofproperfactor = 0

for i in range(1, num):
    if num % i == 0:
        sumofproperfactor = sumofproperfactor + i

if sumofproperfactor > num:
    print("It is a Abudant number")
else:
    print("It is not a Abudant number")


