#input a number
num = int(input("Enter a number: "))
# from 2 to num, foreach to check if num % i ==0, if num % i ==0, then num is not a prime number
isPrime = True
for i in range(2, num):
    if num % i == 0:
        isPrime = False
        break
if isPrime:
    print("Prime number")
else:
    print("Not a prime number")
