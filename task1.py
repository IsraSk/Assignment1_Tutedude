'''Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
'''

print("\nHello!  Let's perform basic mathematical operations on two numbers!")

num1 = int(input('\nEnter first number: '))
num2 = int(input('Enter second number: '))

num3 = num1 + num2
print("\nAddition for both numbers is : ",num3)

num3 = num1 - num2
print("\nSubtraction for both numbers is : ",num3)

num3 = num1 * num2
print("\nMultiplication for both numbers is : ",num3)

num3 = num1 / num2
print("\nDivision for both numbers is : ",num3)

print('\n')
