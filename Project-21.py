#Write a python program to read a file named “article.txt”, count and print total alphabets in the file?

def count_alpha():
    lo=0
    with open("article.txt") as f:
        while True:
            c=f.read(1)
            if not c:
                break
            print(c)
            if((c>='A' and c<='Z') or (c>='a' and c<='z')):
                lo=lo+1
        print("total lower case alphabets ",lo)
#function calling
count_alpha()
def count_alpha():
    lo=0
    with open("article.txt") as f:
        while True:
            c=f.read(1)
            if not c:
                break
            print(c)
            if((c>='A' and c<='Z') or (c>='a' and c<='z')):
                lo=lo+1
        print("total lower case alphabets ",lo)
#function calling
count_alpha()