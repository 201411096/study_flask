import pymongo

username = ''
password = ''
ip_address = 'localhost'
connection = pymongo.MongoClient()
connection = pymongo.MongoClient('mongodb://%s' % (ip_address))

blog_session_db = connection.blog_session_db    # connection.database_name
blog_ab = blog_session_db.blog_ab               # connection.database_name.table_name

print('================================================================================')
print(connection.admin.command('ismaster'))
print('================================================================================')
print(connection.server_info())
print('================================================================================')
blog_ab.insert_one({'emailid':'a@a.com'})
print(blog_ab.find_one( {'emailid':'a@a.com'}))
blog_ab.delete_one( {'emailid':'a@a.com'})
print('================================================================================')
blog_logs = blog_ab.find()
for log in blog_logs:
    print(log)
print('================================================================================')