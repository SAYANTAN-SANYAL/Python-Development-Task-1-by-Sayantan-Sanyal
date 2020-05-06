# to print all prime numbers in a given interval
lower = int(input("Enter the lower range number: "))
upper = int(input("Enter the upper range number: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if(num > 1):
       for i in range(2, num):
           if ((num % i) == 0):
               break
       else:
           print(num)

# to check if a given input number is prime or not
n = int(input("Enter a number: "))
if (n > 1):
    for i in range(2,n):
        if ((n % i) == 0):
            print(n, "is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is not a prime number as it is less than 1")