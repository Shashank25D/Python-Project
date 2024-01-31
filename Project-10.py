#Write a python program to take input for 2 numbers, calculate and print their sum, product and difference?
a=int(input("Enter 1st no "))
b=int(input("Enter 2nd no "))
s=a+b
p=a*b
if(a>b):
    d=a-b
else:
    d=b-a
print("Sum = ",s)
print("Product = ",p)
print("Difference = ",d)
