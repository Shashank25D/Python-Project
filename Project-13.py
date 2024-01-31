#write a program to crate a CSV file to store student dat (Rollno, Name, Marks). Optain data from user and write 5 records into the file?
import csv
fh = open("Student.csv", "w")           #open file
stuwriter = csv.writer(fh)
stuwriter.writerow(['Rollno', 'Name', 'Marks'])      #write hader row

for i in range(5):
    print("Student record", (i+1))
    rollno = int(input("Enter rollno:"))
    name = input ("Enter name:")
    marks = float(input("Enter marks:"))
    sturec = [rollno, name, marks]             #create sequence of user data
    stuwriter.writerow(sturec)