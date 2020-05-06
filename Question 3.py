# Given a number and to count the total number of digits in that number
number=int(input("Enter a number"))
count=0
while(number>0):
    number=number//10
    count=count+1
print("Number of digits in number is: ",count)