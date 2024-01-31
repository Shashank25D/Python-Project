#Write a python program to take input for a number and print its factorial using recursion?

#Factorial of a number using recursion
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
#for fixed number
num = 7
#using user input
num=int(input("Enter any no "))
#check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))