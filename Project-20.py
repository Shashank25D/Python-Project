#Write a python program to read a file named “article.txt”, count and print the following:
#(i) length of the file(total characters in file)
#(ii)total alphabets
#(iii) total upper case alphabets
#(iv) total lower case alphabets
#(v) total digits
#(vi) total spaces
#(vii) total special characters

def count():
    a=0
    ua=0
    la=0
    d=0
    sp=0
    spl=0
    with open("article.txt") as f:
        while True:
            c=f.read(1)
            if not c:
                break
            print(c)
            if((c>='A' and c<='Z') or (c>='a' and c<='z')):
                a=a+1
            if(c>='A' and c<='Z'):
                ua=ua+1
            else:
                la=la+1

            if(c>='0' and c<='9'):
                d=d+1
            if(c==''):
                sp=sp+1
            else:
                spl=spl+1
    print("total alphabets ",a)
    print("total upper case alphabets ",ua)
    print("total lower case alphabets ",la)
    print("total digits ",d)
    print("total spaces ",sp)
    print("total special characters ",spl)
# function calling
count()