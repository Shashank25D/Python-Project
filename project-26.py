#Write a function to search a record stored in a table using python  and MySQL interface.

def search_roll():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",user="root",passwd="",database="")
    try:
        z=0
        roll=int(input("Enter roll no to search "))
        c = db.cursor()
        sql='select * from student;'
        c.execute(sql)
        countrow=c.execute(sql)
        print("number of rows : ",countrow)
        data=c.fetchall()
        for eachrow in data:
            r=eachrow[0]
            n=eachrow[1]
            p=eachrow[2]
        if(r==roll):
            z=1
            print(r,n,p)
        if(z==0):
            print("Record is not present")
    except:
        db.rollback()
        db.close()
# function calling
search_roll()