#Write a python program to take input for 3 numbers, check and print the largest number?
a=int(input("Enter 1st no "))
b=int(input("Enter 2nd no "))
c=int(input("Enter 3rd no "))
if(a>b and a>c):
    m=a
else:
    if(b>c):
        m=b
    else:
        m=c
print("Max no = ",m)
