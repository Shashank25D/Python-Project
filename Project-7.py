#Write a python program to take input for a number and print its table?

num=int(input("Enter any no "))
i=1
while(i<=10):
    table=num*i
    print(num," * ",i," = ",table)
    i=i+1