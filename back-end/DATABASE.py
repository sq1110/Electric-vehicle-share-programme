#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


#VEHICLES database
with sqlite3.connect("Project.db") as db:
    cursor = db.cursor()
print("opened database successfully!")

cursor.execute(""" CREATE TABLE IF NOT EXISTS VEHICLES(
id integer PRIMARY KEY,
vehNo integer,
vehType text,
location text,
state text,
starttime text,
endtime text,
timeused text,
fee integer,
electric integer); """)

# REPAIR database
cursor.execute("""CREATE TABLE IF NOT EXISTS repair(
vehNo integer PRIMARY KEY,
vehType text,
vehStatu text NOT NULL);""")

#LOGIN REGESTER
cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
user_id integer PRIMARY KEY,
user_name text,
user_psw text,
user_balance integer);""")





print("Create table successfully!")
db.commit()
db.close()


# In[3]:


#DEFAULT DATA
with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
print("opened database successfully!")

#TEST DATA      
cursor.execute("INSERT INTO VEHICLES (VEHNO,VEHTYPE,LOCATION,STATE,STARTTIME,ENDTIME,TIMEUSED,FEE,ELECTRIC)    VALUES(?, ?, ?, ?, ? , ?, ?, ? ,?)",(1001,"E-car","G1","Free",None,None,None,None,100))
cursor.execute("INSERT INTO VEHICLES (VEHNO,VEHTYPE,LOCATION,STATE,STARTTIME,ENDTIME,TIMEUSED,FEE,ELECTRIC)    VALUES(?, ?, ?, ?, ? , ?, ?, ? ,?)",(1002,"E-car","G2","Free",None,None,None,None,100))
cursor.execute("INSERT INTO VEHICLES (VEHNO,VEHTYPE,LOCATION,STATE,STARTTIME,ENDTIME,TIMEUSED,FEE,ELECTRIC)    VALUES(?, ?, ?, ?, ? , ?, ?, ? ,?)",(2001,"E-Scooter","G3","Free",None,None,None,None,100))
cursor.execute("INSERT INTO VEHICLES (VEHNO,VEHTYPE,LOCATION,STATE,STARTTIME,ENDTIME,TIMEUSED,FEE,ELECTRIC)    VALUES(?, ?, ?, ?, ? , ?, ?, ? ,?)",(2002,"E-Scooter","G4","Free",None,None,None,None,100))

cursor.execute("""INSERT OR IGNORE INTO repair(vehNo, vehType, vehStatu)
VALUES ("1001", "E-car", "damaged")""")
db.commit()
cursor.execute("""INSERT OR IGNORE INTO repair(vehNo, vehType, vehStatu)
VALUES ("1002", "E-car", "good")""")
db.commit()
cursor.execute("""INSERT OR IGNORE INTO repair(vehNo, vehType, vehStatu)
VALUES ("2001", "E-Scooter", "good")""")
db.commit()
cursor.execute("""INSERT OR IGNORE INTO repair(vehNo, vehType, vehStatu)
VALUES ("2002", "E-Scooter", "good")""")
db.commit()

cursor.execute("""INSERT OR IGNORE INTO USERS(user_name, user_psw, user_balance)
VALUES ("qwe", 123123, 0)""")
cursor.execute("""INSERT OR IGNORE INTO USERS(user_name, user_psw, user_balance)
VALUES ("asd", 123123, 0)""")
cursor.execute("""INSERT OR IGNORE INTO USERS(user_name, user_psw, user_balance)
VALUES ("zxc", 123123, 100)""")


db.commit()
db.close()


# In[ ]:




