
# we can interact with sql databases like sqlite by importing it
# also postgresql which is sql for client-side server db

# to interact with the sql database we need to do five things
# 1. we have to establish a connnection with the database with a connection object
# we have to create a cursor object that will act as an access pointer to the data base table

# we can query the database for values and also push values to it

# we neeed to commit such changes to the DB
# Lastly we have to close the connection

import sqlite3
def create_table():
  connection_object= sqlite3.connect('sample.db')
  cursor_object= connection_object.cursor()
  cursor_object.execute("CREATE TABLE IF NOT EXISTS goods (description TEXT, Quantity INT, Price REAL)")
  connection_object.commit()
  connection_object.close()

def insert_values(description,quantity,price):
  connection_object= sqlite3.connect('sample.db')
  cursor_object= connection_object.cursor()
  cursor_object.execute("INSERT INTO goods VALUES(?,?,?)",(description,quantity,price))
  connection_object.commit()
  connection_object.close()

insert_values('Cement',10,2600)
insert_values('paint_brush',5,200)
insert_values('Mopstick',7,450)

def view_db():
  connection_object= sqlite3.connect('sample.db')
  cursor_object= connection_object.cursor()
  cursor_object.execute("SELECT * FROM goods")
  rows_object= cursor_object.fetchall()
  connection_object.close()
  return rows_object

if type(view_db())== 'list':
  for entry in view_db():
    print(entry)
else:
  print(view_db())    

  


