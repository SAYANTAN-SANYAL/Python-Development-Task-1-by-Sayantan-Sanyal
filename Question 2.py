# To accept a n number from user
# and to calculate sum of all numbers between 1 and n including n
n=int(input("Enter a number"))
sum=0
while(n>1):
    sum=sum+n
    n=n-1
print("Sum of numbers is: ",sum)