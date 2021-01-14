import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Bmt113@2",
  database="BMT"
)



csv_op = open('E:/customer.csv')
csv_data = csv.reader(csv_op)

cursor = mydb.cursor()

cursor.execute("DROP TABLE IF EXISTS roww")

sql ='''CREATE TABLE roww(
   customerid CHAR(100),
   firstname CHAR(100),
   lastname CHAR(100),
   companyname CHAR(100),
   billingaddress1 CHAR(100),
   billingaddress2 CHAR(100),
   city CHAR(100),
   state CHAR(100),
   postalcode CHAR(100),
   country CHAR(100),
   phonenumber CHAR(100),
   emailaddress CHAR(100),
   createddate CHAR(100)
)'''
cursor.execute(sql)

for row in csv_data:

  insert_data = (
    'INSERT INTO roww(customerid,firstname,lastname,companyname,billingaddress1,billingaddress2,city,state,postalcode,country,phonenumber,emailaddress,createddate )' 
    'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                  )
  cursor.execute(insert_data, row)


mydb.commit()
cursor.close()
print("Done")
