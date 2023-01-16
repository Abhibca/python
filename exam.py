import MySQLdb
conn = MySQLdb.connect(user='root',passwd='', db='test', host='127.0.0.1')
cursor = conn.cursor()
str = "Insert into emp(empno, ename, salary) values (123, 'Mac', 5000.00)"
try:
 cursor.execute(str)
 conn.commit() # Save changes to database
 print('1 row inserted')
except:
 conn.rollback() # rollback if any error
cursor.close()
conn.close()
"""from sqlite3 import Cursor
import MySQLdb
conn = MySQLdb.connect(user='root',password='',db='test',host='localhost')

cursor=conn.cursor()

str = "Insert into emp(empno,ename,salary) values (1,'abhi',25000.00)"

cursor.execute(str)
print("insert Successfully")

cursor.close()
conn.close()
"""