#Write a python program to maintain employee details like empno,name and salary using Queues data structure? (implement insert(), delete() and traverse() functions)

#queue implementation (using functions)
#program to create a queue of employee(empno,name,sal).
"""
add employee
delete employee
traverse / display all employees
"""
employee=[]
def add_element():
    empno=input("Enter empno ")
    name=input("Enter name ")
    sal=input("Enter sal ")
    emp=(empno,name,sal)
    employee.append(emp)

def del_element():
    if(employee==[]):
        print("Underflow / Employee Stack in empty")
    else:
        empno,name,sal=employee.pop(0)
        print("poped element is ")
        print("empno ",empno," name ",name," salary ",sal)

def traverse():
    if not (employee==[]):
        n=len(employee)
        for i in range(0,n):
            print(employee[i])
    else:
        print("Empty , No employee to display")

while True:
    print("1. Add employee")
    print("2. Delete employee")
    print("3. Traversal")
    print("4. Exit")
    ch=int(input("Enter your choice "))
    if(ch==1):
        add_element()
    elif(ch==2):
        del_element();
    elif(ch==3):
        traverse()
    elif(ch==4):
        print("End")
        break
    else:
        print("Invalid choice")