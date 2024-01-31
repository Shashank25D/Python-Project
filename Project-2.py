#Write a python program to maintain book details like book code, book title and price using stacks data structures? (implement push(), pop() and traverse() functions)

"""
push
pop
traverse
"""
book=[]

def push():
    bcode=input("Enter bcode ")
    btitle=input("Enter btitle ")
    price=input("Enter price ")
    bk=(bcode,btitle,price)
    book.append(bk)

def pop():
    if(book==[]):
        print("Underflow / Book Stack in empty")
    else:
        bcode,btitle,price=book.pop()
    print("poped element is ")
    print("bcode ",bcode," btitle ",btitle," price ",price)

def traverse():
    if not (book==[]):
        n=len(book)
        for i in range(n-1,-1,-1):
            print(book[i])
    else:
        print("Empty , No book to display")
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Traversal")
    print("4. Exit")

    ch=int(input("Enter your choice "))
    if(ch==1):
        push()
    elif(ch==2):
        pop()
    elif(ch==3):
        traverse()
    elif(ch==4):
        print("End")
        break
    else:
        print("Invalid choice")