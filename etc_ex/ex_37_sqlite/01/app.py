import sqlite3

def get_connection():
    conn = sqlite3.connect('example.db')
    return conn

def get_cursor(conn):
    c = conn.cursor()
    return c

def execute_query(conn, c):
    query = input('query 입력 : ')
    print('query 내용 확인 : ', query)    
    result = c.execute(query)
    get_dataList(result)
    conn.commit()

def get_dataList(result):
    for row in result:
        print(row)

def close_connection(conn):
    conn.close()

if __name__ == "__main__":
    while True:
        conn = get_connection()
        c = get_cursor(conn)
        execute_query(conn, c)
        close_connection(conn)