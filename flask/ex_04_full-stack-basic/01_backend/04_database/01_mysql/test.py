import pymysql

db_connection = pymysql.connect(
        host='localhost', 
        port=3306, 
        user='root', 
        passwd='0000', 
        db='test', 
        charset='utf8')

myCursor = db_connection.cursor()

def createTable_userInfo():
    sql = """
    CREATE TABLE IF NOT EXISTS user_info (
        USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
        USER_EMAIL VARCHAR(100) NOT NULL,
        BLOG_ID CHAR(4),
        PRIMARY KEY(USER_ID)
    );
    """
    myCursor.execute(sql)
    db_connection.commit()

def printTables():
    sql = 'show tables;'
    tableCnt = myCursor.execute(sql)
    print('tableCnt :', tableCnt)    

def dropTable_userInfo():
    sql = 'DROP TABLE user_info;'
    myCursor.execute(sql)
    db_connection.commit()

def insertData_userInfo(dataList):
    for data in dataList:
        sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (str(data['user_email']), str(data['blog_id']))
        myCursor.execute(sql)
    db_connection.commit()

def selectData_userInfo():
    sql = "SELECT * FROM user_info"
    myCursor.execute(sql)
    results = myCursor.fetchall()
    return results    

def deleteData_userInfo(user_id):
    sql = "DELETE FROM user_info WHERE USER_ID = %d" % (user_id)
    print('deleteRowCnt : ', myCursor.execute(sql))
    db_connection.commit()

print('================================================================================')
printTables()
print('================================================================================')
createTable_userInfo()
printTables()
print('================================================================================')
dropTable_userInfo()
printTables()
print('================================================================================')
createTable_userInfo()
dataList = [ {"user_email":"a@a.com", "blog_id":"aa"}, {"user_email":"b@b.com", "blog_id":"bb"}, {"user_email":"c@c.com", "blog_id":"cc"} ]
insertData_userInfo(dataList)
resultList = selectData_userInfo()
for row in resultList:
    print(row)
print('================================================================================')
deleteData_userInfo(1)
resultList = selectData_userInfo()
for row in resultList:
    print(row)
