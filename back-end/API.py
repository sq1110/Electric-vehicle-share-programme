#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import numpy as np
import pandas as pd
from datetime import datetime
from flask_cors import *
import os
import json
from flask import Flask
import random
from flask import Flask, render_template, request, redirect, url_for, flash, session
from contextlib import closing


# In[2]:


#LOGIN REGISTER MODULE
app = Flask(__name__)

app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'
app.config.update(
    DATABASE = 'Project.db',
#     DEBUG=True,
)
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('Project.db', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = connect_db()
    cur = db.cursor()
    return db, cur

@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for('login'))

#register.html，login.html，menu.html
#username（user）password（pwd），is 'u' and 'p'
@app.route('/login',methods=['GET', 'POST'])
def login():  # login
#     if request.method =='POST':
        u = request.values.get("user", '')  # username
        p = request.values.get("pwd", '')  # password
        if u and p:
            db, cur = get_db()
            x = cur.execute("SELECT * FROM USERS WHERE user_name ='%s' and user_psw ='%s'" %(u,p)).fetchone()
            #c = UserInfo.objects.filter(user_name=u, user_psw=p).count()
            if x:
                session['logged_in'] = True
                session['username'] = u
                flash("You have logged in")
                ren = {'msg':"success","msg_code":200} #login successful
            else:
                login_massage ="Please input correct username and password"
                ren = {'msg':"input correct username and password","msg_code":500}
        else:
            login_massage = "Please input username and password!"
            ren = {'msg':"Please input username and password!","msg_code":500}
        return json.dumps(ren, ensure_ascii=False)

#     if request.method =='POST':  
#         u = request.form.get('user')# username
#         p = request.form.get("pwd")  # password
#         u = "zxc"
#         p = 123123
#         print(u,p)
#         with sqlite3.connect("Project.db") as db:
#             cursor = db.cursor()
        
#         cursor.execute("SELECT user_psw FROM USERS WHERE user_name = '{}'".format(u))
#         data = cursor.fetchall()
#         psw = data[0][0]
        
#         if psw == str(p):
#             ren = {'msg':"success","msg_code":200}
#         else:
#             ren = {'msg':"fail","msg_code":200}        
#         return json.dumps(ren, ensure_ascii=False)
        

        
        
        

#username（user）password（pwd），confirm password(c_pwd), is 'u' and 'p' and 'c_p'
@app.route('/register',methods=['GET', 'POST'])
def register(): #register
        u = request.values.get("user", '')  # username
        p = request.values.get("pwd", '')  # password
        c_p = request.values.get("c_pwd",'')  #confirm your password
        b=0
        if u and p and c_p:
            db, cur = get_db()
            x = cur.execute('SELECT * FROM USERS WHERE user_name = ?', [u])
            #c = UserInfo.objects.filter(user_name=u).count()
            if (x.fetchall()):
                register_massage = "Sorry, this name has been used"
                ren = {'msg':"fail","msg_code":500}
                
            else:
                if c_p==p:   # check if two passwords are same
                    # count = 1
                    # while count != 0:
                    #         id = str(random.randrange(00000, 99999))  #生成用户id
                    #         y = cur.execute('SELECT * FROM login_userinfo WHERE user_id = ?', [id])
                    #         if(y.fetchall()):
                    #             count=0
                        #user = UserInfo(user_id=id, user_name=u, user_psw=p)
                        #user.save()
                    cur.execute("INSERT INTO USERS (user_name, user_psw, user_balance) VALUES(?,?,?)", [u, p, b])
                    flash("successful!")
                    db.commit()
                    cur.close()
                    db.close()
                    session['logged_in'] = True
                    session['username'] = u
                    ren = {'msg':"success1","msg_code":200}


                else:
                    register_massage = "Please ensure that two passwords you input are same"
                    ren = {'msg':"Please ensure that two passwords you input are same","msg_code":500}

            register_massage = "Successful!"
            ren = {'msg':"success2","msg_code":200}
        else:
            register_massage = "Please input username and password"
            ren = {'msg':"Please input username and password","msg_code":500}
        return json.dumps(ren, ensure_ascii=False)

@app.route("/menu")  #after login, to redirection
def menu():
    if 'logged_in' in session:
        #print("login successful")
        return render_template("menu.html")
    else:
        #print("didnot login before")
        return redirect(url_for('login')) #redirection


@app.route('/logout')  #logout
def logout():
#     if 'logged_in' in session:
        session.pop('logged_in', None)
        flash("You have logged out")
        #print("logout")
        ren = {'msg':"LOg off","msg_code":200}
        return json.dumps(ren, ensure_ascii=False)
#     else:
#         #print("please login!")
#         return redirect(url_for('login'))

@app.route('/change_psw',methods=['GET', 'POST'])  #change your password (and redirection)
def change_psw():
    if 'logged_in' in session:
        u = session['username']
        print(u)
        p = request.value.get("pwd", '')  # password
        c_p = request.value.get("c_pwd", '')  # confirm
        if p and c_p:
            if p==c_p:
                db, cur = get_db()
                cur.execute("UPDATE USERS SET user_psw =  ('%s') where user_name =  ('%s')"%(p,u))
                db.commit()
                flash("You have changed your password")
                return redirect(url_for('login'))
            else:
                register_massage = "Please ensure that two passwords you input are same"
                return render_template('change_psw.html', message=register_massage)
        else:
            register_massage = "Please input a new password"
            return render_template('change_psw.html', message=register_massage)
    else:
        # print("please login!")
        return redirect(url_for('login'))


# In[3]:


#RENTING RETURN MODULE
@app.route("/searchv", methods =[ "GET","POST"])
def getcontent():
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
#     print("opened database successfully!")
    
    sql = "SELECT * FROM VEHICLES"
    cursor.execute(sql)
    data = cursor.fetchall()
    
    para = []
    for i in data:
        text = {'ID':i[0], 'VehNo':i[1], 'vehType':i[2], 'Location':i[3], 'State':i[4],'Start':i[5],'End':i[6],'Timeused':i[7],'Fee':i[8],'Electric':i[9],}       
        para.append(text)
#     res['para'] = para    
    return json.dumps(para, ensure_ascii=False, indent=4)

@app.route('/rent/<int:no>',methods=['PUT'])
def renting(no):
    
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
#     print("opened database successfully!")
#     no = int(input("pls enter velno: "))
    time = datetime.now()
    
    try:       
        cursor.execute("UPDATE VEHICLES set STATE = 'Rented' where VEHNO = '{}'".format(no) )
        cursor.execute("UPDATE VEHICLES set STARTTIME = ? where VEHNO = ?",(time,no) )
        print("Successful rent of vehicle!")
        db.commit()
        db.close()
        
        ren = {'msg':"success","msg_code":200}
        return json.dumps(ren, ensure_ascii=False)
    except:
        print(0)

@app.route('/return/<int:no>/<string:loc>',methods=['PUT'])
def returning(no, loc):
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
    print("opened database successfully!")
#     location = input("Pls enter this vehicles station: ")
    time = datetime.now()
#     print(time.minute)
    cursor.execute("UPDATE VEHICLES set STATE = 'Free'where VEHNO = '{}' ".format(no))
    cursor.execute("UPDATE VEHICLES set LOCATION = ? where VEHNO = ? ",(loc,no))
    cursor.execute("UPDATE VEHICLES set ENDTIME = ? where VEHNO = ?",(time,no) )
    cursor.execute("SELECT STARTTIME FROM VEHICLES WHERE VEHNO = '{}'".format(no) )
    fetch = cursor.fetchall()
    for t in fetch:
        times = t
    s = ''.join(times)
    #times.second()
    #times = datetime(times)
    cursor.execute("SELECT ENDTIME FROM VEHICLES WHERE VEHNO = '{}'".format(no) )
    fetch = cursor.fetchall()
    for t in fetch:
        timee = t
    e = ''.join(timee)
    #timee = datetime(timee)
#     print(s,e)
    dates = datetime.strptime(s,'%Y-%m-%d %H:%M:%S.%f')
    datee = datetime.strptime(e,'%Y-%m-%d %H:%M:%S.%f')
#     print(dates,datee)
    timeused = (datee-dates).total_seconds()
    timeused = round (timeused,2)
#     print("timeused:",timeused)
    
    fee = timeused * 0.01
    fee = round (fee,2)
    
#     print("fee:",fee)
    cursor.execute("SELECT ELECTRIC FROM VEHICLES WHERE VEHNO = '{}'".format(no) )
    data = cursor.fetchall()
    electric = data[0][0]
    ele = electric - timeused * 0.005
    ele = round (ele,2)
        
    cursor.execute("UPDATE VEHICLES set TIMEUSED = ? where VEHNO = ?",(timeused,no) )
    cursor.execute("UPDATE VEHICLES set FEE = ? where VEHNO = ?",(fee,no) )
    cursor.execute("UPDATE VEHICLES set ELECTRIC = ? where VEHNO = ?",(ele,no) )
    print("Successful return of vehicle!")
    db.commit()
    db.close()
    ren = {'msg':"success","msg_code":200}
    return json.dumps(ren, ensure_ascii=False)


# In[4]:


#CHARGE AND REPAIR Module

@app.route('/charge/<int:no>', methods=['PUT'])
def charge(no):
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
    print("opened database successfully!")
    try:
        # sql = "UPDATE electricQuantity SET electricQuantity = 100 WHERE electricQuantity = 10"
        # cursor.execute(sql)
        cursor.execute("UPDATE VEHICLES SET ELECTRIC = 100 WHERE VEHNO = '{}'".format(no))
        print("Successful charge the vehicle!")
        db.commit()
        db.close()
        ren = {'msg':"success","msg_code":200}
        return json.dumps(ren, ensure_ascii=False)
    except:
        print(0)
        
@app.route('/repair/<int:no>', methods=['PUT'])
def repair(no):
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
    print("opened database successfully!")

    try:

        cursor.execute("UPDATE repair SET vehStatu = 'good' WHERE vehNo = '{}'".format(no))
        print("Repair the vehicle successfully!")
        db.commit()
        db.close()
        ren = {'msg':"success","msg_code":200}
        return json.dumps(ren, ensure_ascii=False)
    except Exception as e:
        print(0)
        return jsonify({'message': 'Error: {}'.format(str(e)), 'code': '500'})
    
    
@app.route('/report/<int:no>', methods=['PUT'])
def report(no):
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
    print("opened database successfully!")

    try:

        cursor.execute("UPDATE repair SET vehStatu = 'damaged' WHERE vehno = '{}'".format(no))
        print("Report successfully!")
        db.commit()
        db.close()
        ren = {'msg':"success","msg_code":200}
        return json.dumps(ren, ensure_ascii=False)
    except Exception as e:
        print(0)
        return jsonify({'message': 'Error: {}'.format(str(e)), 'code': '500'})

@app.route("/showinfo", methods=["GET", "POST"])
def getrepair():
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
    print("opened database successfully!")

    sql = "SELECT * FROM repair"
    cursor.execute(sql)
    data = cursor.fetchall()

    para = []
    for i in data:
        text = {'vehNo': i[0], 'vehType': i[1], 'vehStatu': i[2], }
        para.append(text)
    #     res['para'] = para
    return json.dumps(para, ensure_ascii=False, indent=4)

    

# @app.route('/repair_tyre/<int:no>', methods=['PUT'])
# def repair_tyre(no):
#     with sqlite3.connect("Project.db") as db:
#         cursor = db.cursor()
#     print("opened database successfully!")

#     try:
#         cursor.execute("UPDATE repair SET tyre = 'good' WHERE tyre = '{}'".format(no))
#         print("Repair the vehicle successfully!")
#         db.commit()
#         db.close()
#         ren = {'msg':"success","msg_code":200}
#         return json.dumps(ren, ensure_ascii=False)
#     except:
#         print(0)

# @app.route('/spray_lacquer/<int:no>', methods=['PUT'])
# def spray_lacquer(no):
#     with sqlite3.connect("Project.db") as db:
#         cursor = db.cursor()
#     print("opened database successfully!")

#     try:
#         cursor.execute("UPDATE repair SET lacquer='good' WHERE lacquer = '{}'".format(no))
#         print("Repair the vehicle successfully!")
#         db.commit()
#         db.close()
#         ren = {'msg':"success","msg_code":200}
#         return json.dumps(ren, ensure_ascii=False)
#     except:
#         print(0)


# @app.route('/repair_engine/<int:no>', methods=['PUT'])
# def repair_engine(no):
#     with sqlite3.connect("Project.db") as db:
#         cursor = db.cursor()
#     print("opened database successfully!")

#     try:
#         cursor.execute("UPDATE repair SET engine='good' WHERE engine = '{}'".format(no))
#         print("Repair the vehicle successfully!")
#         db.commit()
#         db.close()
#         ren = {'msg':"success","msg_code":200}
#         return json.dumps(ren, ensure_ascii=False)
#     except:
#         print(0)


# @app.route('/maintenance/<int:no>', methods=['PUT'])
# def maintenance(no):
#     with sqlite3.connect("Project.db") as db:
#         cursor = db.cursor()
#     print("opened database successfully!")

#     try:
#         cursor.execute("UPDATE repair SET maintenance='good' WHERE maintenance = '{}'".format(no))
#         print("Repair the vehicle successfully!")
#         db.commit()
#         db.close()
#         ren = {'msg':"success","msg_code":200}
#         return json.dumps(ren, ensure_ascii=False)
#     except:
#         print(0)


# In[5]:


@app.route("/showuser/<string:username>", methods=["GET", "POST"])
def getusers(username):
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
    print("opened database successfully!")

    cursor.execute("SELECT * FROM USERS WHERE user_name = '{}'".format(username) )
    data = cursor.fetchall()

    para = []
    for i in data:
        text = {'user_id': i[0], 'user_name': i[1],'user_psw': i[2], 'user_balance': i[3], }
        para.append(text)
    #     res['para'] = para
    return json.dumps(para, ensure_ascii=False, indent=4)



#Recharge and pay module
@app.route('/recharge/<string:username>', methods=['PUT'])
def recharge(username):
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
#     print("opened database successfully!")
    try:
#         Get the input data from the front end
#         recharge = request.values.get("recharge", '')
#         test 
        recharge = 100

        cursor.execute("SELECT user_balance FROM USERS WHERE user_name = '{}'".format(username) )
        data = cursor.fetchall()
        balance = data[0][0]

        balance = balance + recharge
        
        cursor.execute("UPDATE USERS set user_balance = ? where user_name = ?",(balance,username))
#         print("Recharge successfully!")
        db.commit()
        db.close()
        ren = {'msg':"success","msg_code":200}
        return json.dumps(ren, ensure_ascii=False)
    except:
        print(0)
        
        
@app.route('/pay/<int:userid>/<int:no>', methods=['PUT'])
def payment(userid, no):
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
#     print("opened database successfully!")
    try:
        cursor.execute("SELECT user_balance FROM USERS WHERE user_id = '{}'".format(userid) )
        data = cursor.fetchall()
        balance = data[0][0]
        
        cursor.execute("SELECT FEE FROM VEHICLES WHERE VEHNO = '{}'".format(no) )
        data1 = cursor.fetchall()
        fee = data1[0][0]
        
        balance = balance - fee
        
        cursor.execute("UPDATE USERS set user_balance = ? where user_id = ?",(balance,userid))
        print("Payment success!")
        db.commit()
        db.close()
        ren = {'msg':"success","msg_code":200}
        return json.dumps(ren, ensure_ascii=False)
    except:
        print(0)


# In[6]:


# with sqlite3.connect("Project.db") as db:
#     cursor = db.cursor()
# #     print("opened database successfully!")
# userid = 3
# no = 1001

# cursor.execute("SELECT user_balance FROM USERS WHERE user_id = '{}'".format(userid) )
# data = cursor.fetchall()
# balance = data[0][0]
# print(balance)
# print(type(balance))
        
# cursor.execute("SELECT FEE FROM VEHICLES WHERE VEHNO = '{}'".format(no) )
# data1 = cursor.fetchall()
# fee = data1[0][0]
# print(fee)
# print(type(fee))        
# balance = balance - fee
        
# cursor.execute("UPDATE USERS set user_balance = ? where user_id = ?",(balance,userid))
# print("Payment success!")


# In[ ]:


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5590)


# In[ ]:


def test():
    
    u = "zxc"
    p = 123123        
    with sqlite3.connect("Project.db") as db:
        cursor = db.cursor()
    
    cursor.execute("SELECT user_psw FROM USERS WHERE user_name = '{}'".format(u))
    data = cursor.fetchall()
    psw = data[0][0]
    
    if psw == str(p):
        ren = {'msg':"success","msg_code":200}
    
    else:
        ren = {'msg':"fail","msg_code":200}  
        
    return json.dumps(ren, ensure_ascii=False)
    


# In[ ]:


# with sqlite3.connect("Project.db") as db:
#     cursor = db.cursor()
# #     print("opened database successfully!")

# #         Get the input data from the front end
# recharge = request.values.get("recharge", '')
# #         test 
# #         recharge = 50

# cursor.execute("SELECT user_balance FROM USERS WHERE user_name = '{}'".format(username) )
# data = cursor.fetchall()
# balance = data[0][0]

# balance = balance + recharge
        
# cursor.execute("UPDATE USERS set user_balance = ? where user_name = ?",(balance,username))
# #         print("Recharge successfully!")
# db.commit()
# db.close()


# In[ ]:




