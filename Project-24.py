import mysql.connector

def insert_data():
    # Establish a connection to the MySQL server
    db = mysql.connector.connect(host="localhost", user="root", password="", database="")

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Take input for the details and then save the record in the database
    r = int(input("Enter roll no "))
    n = input("Enter name ")
    p = int(input("Enter per "))

    try:
        # Insert the record into the table
        cur.execute("insert into student (roll, name, per) values (%s, %s, %s)", (r, n, p))

        # Commit the changes
        db.commit()

        print("Record saved")

    except:
        # Rollback the changes in case of any errors
        db.rollback()

        # Close the connection
        db.close()

# Function calling
insert_data()