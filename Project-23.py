import time
import mysql.connector

# Establish a database connection
connect = mysql.connector.connect(host="localhost", user="root", password="", database="")
cursor = connect.cursor()

# Create the table (with corrected SQL syntax)
query1 = "CREATE TABLE IF NOT EXISTS hotel_data_customer (name VARCHAR(100), contact varchar(10) , email varchar(200) , address varchar(200) , child int , adult int , no_of_days int , room_no int )"
cursor.execute(query1)
# check out function
def check_out(room_no):
    try:
        delete_query="DELETE FROM hotel_data_customer WHERE room_no = %s"
        cursor.execute(delete_query,(room_no,))
        connect.commit()
    finally:
        cursor.close()
# room booking function
def book_a_room():
    Name=input("First name : - ")
    contact=input("Contact number : -  ")
    email=input("Email id : - ")
    address=input("Address : - ")
    days=int(input("No of days : - "))
    child=int(input("No of child : - "))
    adult=int(input("No of adult : - "))
    room_no=int(input("room no : - "))
    query="insert into hotel_data_customer values(%s,%s,%s,%s,%s,%s,%s,%s)"
    data=(Name , contact , email , address, days , child , adult , room_no )
    cursor.execute(query,data)
    connect.commit()
    print("BOOKING SUCCESFULL")

# hotel status
def hotel_status():
    print("""
BOOKING TIMINGS ARE 5:00 AM - 12:00 AM
OTHERWISE SPECIAL ENTRY
FULLY BOOKED ON DIWALI
DISCOUNT AVAILABLE IN ICICI BANK ON UPI ALSO
THANK YOU
VISIT AGAIN""")
# creating login function 
def after_login():
    print("""
=======================================
||  WELCOME TO BANKING MANAGEMENT    ||
=======================================
|| YOU HAVE THESE OPTION AVAILABLE   ||
=======================================
|| 1 . BOOK A ROOM                   ||
=======================================
|| 2 . CHECK OUT                     ||
=======================================
|| 3 . HOTEL STATUS                  ||
=======================================
|| 4 . PAYMENT INFO                  ||
=======================================
|| 5 . CONTACT                       ||
=======================================
|| 6 . VIEW ROOM DETAILS             ||
=======================================""")
# billing function
def payment_info():
    name=input("Enter name ")
    query="select no_of_days from hotel_data_customer where name = %s"
    cursor.execute(query,(name,))
    result=cursor.fetchone()
    if result:
        number_of_days = result[0]
        print(f"Number of days for {search_name}: {number_of_days}")
        bill=number_of_days * 2000
        print("YOU ARE TOTAL BILLED OF ",bill)
    else:
        print(f"No data found for {search_name}.")

# CONTACT  FUNCTION
def contact():
    print("""
==================================================
|            YOU MAY CONTACT US ON               |
==================================================
| 1 . EMAIL - suyashkhatri911@gmail.com          |
==================================================
| 2 . PHONE NUMEBER - 8302426001                 |
==================================================
| 3 . ADDRESS - KHATRI BANK BARMER (344001)      |
==================================================
| 4 . MEETING TIME 10AM-8PM (MONDAY-FRIDAY)      |
==================================================
|                   THANK YOU                    |
==================================================""")

# room info of our hotel
def room_data():
    print("STILL TO BE UPDATED ")

# creating optional function
def first_option():
    option=int(input("Enter your option "))
    if option==1:
        book_a_room()
    if option==2:
        room_to_check_out=int(input("Enter room number to check out"))
        check_out(room_to_check_out)
    if option==3:
        hotel_status()
    if option==4:
        payment_info()
    if option==5:
        contact()
    if option==6:
        room_data()
    else:
        print("Wrong input ")


# Password login loop
while True:
    login = input("Enter password to unlock: ")
    if login == "123":
        line = "Logging in, please wait..."
        words = line.split()
        for word in words:
            print(word, end=' ', flush=True)
            time.sleep(0.5)
        after_login()
        first_option()
        
    else:
        print("Incorrect password. Try again.")

def room_data():
    print("STILL TO BE UPDATED ")