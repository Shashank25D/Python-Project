#Write a program to get student data (roll no., name and marks) from user and write onto a binary file. The program should be able to get data from the user and write onto the file as the user wants?
import pickle
stu = {}              # declare empty dictionary
stufile = open('Stu.dat', 'wb')             # open file
# get data to write onto the file
ans = 'y'
while ans == 'y':
    rno = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    # add read data into dictionary
    stu['Rollno'] = rno
    stu['Name'] = name
    stu['Marks'] = marks
    # now write into the file
    pickle.dump(stu, stufile)
    ans = input("Want to enter more records? (y/n)...")
stufile.close()                       # close file