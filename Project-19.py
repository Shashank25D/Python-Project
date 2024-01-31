#Write a python program to read a file named “article.txt”, count and print total words starting with “a” or “A” in the file?

def count_words():
    w=0
    with open("article.txt") as f:
        for line in f:
            for word in line.split():
                if(word[0]=="a" or word[0]=="A"):
                    print(word)
                    w=w+1
        print("total words starting with 'a' are ",w)
# function calling
count_words()