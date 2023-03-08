import pymysql 
import time
table_name = "kv"
db_name = "test_db"
user = "unicorn"
pwd = "12345678"
host = "database-1.cw5kyi6zgy8d.us-east-1.rds.amazonaws.com"
mykey=1 
myvalue=1 
while True:
	db = pymysql.connect(host=host, user=user, password=pwd, database=db_name) 
	cursor = db.cursor() 
	try:
		sql = 'INSERT INTO kv(mykey,myvalue) VALUES(%s,%s)'
		args = (str(mykey),str(myvalue))
		cursor.execute(sql, args=args)
		db.commit()
		db.close() 
	except:
		print("error") 
	mykey+=1
	myvalue+=2
	time.sleep(30)