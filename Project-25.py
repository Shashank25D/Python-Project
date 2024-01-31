#Write a function to display all the records stored in a table using python  and MySQL interface.

def display_all():
    import mysql.connector
    db = mysql.connector.connect(host='localhost',user='root',password='',database='')
    try:
        c = db.cursor()
        sql='select * from student;'
        c.execute(sql)
        countrow=c.execute(sql)
        print("number of rows : ",countrow)
        data=c.fetchall()
        print("=========================")
        print("Roll No Name Per ")
        print("=========================")
        for eachrow in data:
            r=eachrow[0]
            n=eachrow[1]
            p=eachrow[2]
            print(r,' ',n,' ',p)
            print("=========================")
    except:
        db.rollback()
        db.close()
# function calling
display_all()