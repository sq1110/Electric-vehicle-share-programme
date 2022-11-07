import os
import sqlite3
BASEDIR = os.path.dirname(os.path.abspath(__file__))
SQLLITEDB = os.path.join(BASEDIR, 'rentcar.db')

"""
database:connection
"""
# build connection
def get_con():
    try:
        conn = sqlite3.connect(SQLLITEDB)
        cur = conn.cursor()
    except Exception as e:
        print("Error! :{}".format(e))
        return None, None
    return conn, cur

def close_db(conn, cur):
    try:
        cur.close()
        conn.close()
    except Exception as e:
        print("Error! :{}".format(e))


def query(sql, *args):
    conn, cursor = get_con()
    cursor.execute(sql, *args)
    res = cursor.fetchall()
    close_db(conn, cursor)
    return res

