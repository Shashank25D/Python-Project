#Write a program to read and display the contents of Employee.csv created in the previous program?
import csv

with open("Employee.csv", "r") as fh:
    ereader = csv.reader(fh)
    print ("File Employee.csv contains:")
    for rec in ereader:
        print(rec)