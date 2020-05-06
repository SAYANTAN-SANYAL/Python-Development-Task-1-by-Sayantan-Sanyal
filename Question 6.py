# to print fibonacci series
nterms = int(input("Enter the number of terms: "))
a,b = 0, 1
count = 0
if (nterms <= 0):
   print("Please enter a positive integer")
elif (nterms == 1):
   print("Fibonacci sequence upto",nterms,":")
   print(a)
else:
   print("Fibonacci sequence:")
   while (count < nterms):
       print(a)
       c = a + b
       a = b
       b = c
       count = count + 1

# to check if a given input number is fibonacci or not
import math
def checkPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    if (pow(sqrt, 2) == n):
        return True
    else:
        return False
def isFibonacciNumber(n):
    res1 = 5 * n * n + 4
    res2 = 5 * n * n - 4
    if (checkPerfectSquare(res1) or checkPerfectSquare(res2)):
        return True
    else:
        return False
num = int(input("Enter an integer number: "))
if (isFibonacciNumber(num)):
    print ("Yes,", num, "is a Fibonacci number")
else:
    print ("No,", num, "is not a Fibonacci number")