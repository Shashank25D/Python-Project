#Write a program to get roll numbers, names and marks of the students of a class (get from user) and store these details in a file called "Marks.txt".
count = int(input("How many students are there in the class?"))
fileout = open ("Marks.txt", "w")

for i in range(count):
    print("Enter details for student", (i+1), "below:")
    rollno = int(input("Rollno:"))
    name = input("Name:")
    marks = float(input("Marks:"))
    rec = str(rollno) + "," + name + "," + str(marks) +'\n'
    fileout.write(rec)
fileout.close()