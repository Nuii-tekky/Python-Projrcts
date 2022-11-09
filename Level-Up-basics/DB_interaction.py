
# we can interact with sql databases like sqlite by importing it
# also postgresql which is sql for client-side server db

# to interact with the sql database we need to do five things
# 1. we have to establish a connnection with the database with a connection object
# we have to create a cursor object that will act as an access pointer to the data base table

# we can query the database for values and also push values to it

# we neeed to commit such changes to the DB
# Lastly we have to close the connection

import sqlite3

connection_object= sqlite3.connect('sample.db')
cursor_object= connection_object.cursor()
cursor_object.execute("CREATE TABLE IF NOT EXISTS goods (Description TEXT, Quantity INT, Price REAL, Total INT)")
cursor_object.execute("INSERT INTO goods VALUES('Cement',400,2000.05)")

connection_object.commit()
connection_object.close()