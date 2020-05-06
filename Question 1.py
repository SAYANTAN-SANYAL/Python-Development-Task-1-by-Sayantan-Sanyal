# To accept 2 integer numbers from user and return their product
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
product = num1 * num2
print("Product of numbers is: ",product)
# if the product is greater than 1000 then return their sum
if (product > 1000):
    sum = num1 + num2
    print("sum of numbers is: ",sum)
