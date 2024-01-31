#Write a python program to take input for a number and print its factorial?

n=int(input("Enter any no "))
i=1
f=1
while(i<=n):
    f=f*i
    i=i+1
print("Factorial = ",f)