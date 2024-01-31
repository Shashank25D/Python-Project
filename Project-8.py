#Write a python program to take input for 2 numbers and an operator (+ , – , * , / ). Based on the operator calculate and print the result?
a=int(input("Enter 1st no "))
b=int(input("Enter 2nd no "))
op=input("Enter the operator (+,-,*,/) ")
if(op=="+"):
    c=a+b
    print("Sum = ",c)
elif(op=="*"):
    c=a*b
    print("Product = ",c)
elif(op=="-"):
    if(a>b):
        c=a-b
    else:
        c=b-a
    print("Difference = ",c)
elif(op=="/"):
    c=a/b
    print("Division = ",c)
else:
    print("Invalid operator")