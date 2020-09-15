from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, DateTime
import datetime
# error mysqldb
# ㄴ pip install mysqlclient
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/ex_flask_sqlalchemy'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Table1(db.Model):
    __tablename__ = 'kys'
    col_string = db.Column(db.String(100), primary_key=True)
    col_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    col_text = db.Column(db.Text)
    col_int = db.Column(db.Integer)
    col_numeric = db.Column(db.Float)
    col_bit = db.Column(db.Boolean)
    
    # def __init__(self, col1, col2, col3, col4, col5, col6):
    #     self.col_string = col1
    #     self.col_date = col2
    #     self.col_text = col3
    #     self.col_int = col4
    #     self.col_numeric = col5
    #     self.col_bit = col6
if __name__ == '__main__':
    samples = Table1.query.all()
    print('samples ----')
    print(samples)
    print('samples ----')
    for sample in samples:
        print('------------------------------------------------------------------')
        print('type :' + str(type(sample)))
        print('string : ' + sample.col_string)
        print('date : ' + str(sample.col_date))
        print('text : ' + sample.col_text)
        print('int : ' + str(sample.col_int))
        print('numeric : ' + str(sample.col_numeric))
        print('bit : ' + str(sample.col_bit))
    answer = 0
    while(True):
        print('selectAll : 0')
        print('insert : 1')
        print('update : 2')
        print('delete : 3')
        print('select : 4')
        print('exit : -1')
        answer = input('option :')
        if(answer=='-1'):
            print(answer)
            break
        if(answer=='0'):
            samples = Table1.query.all()
            for sample in samples:
                print('------------------------------------------------------------------')
                print('type :' + str(type(sample)))
                print('string : ' + sample.col_string)
                print('date : ' + str(sample.col_date))
                print('text : ' + sample.col_text)
                print('int : ' + str(sample.col_int))
                print('numeric : ' + str(sample.col_numeric))
                print('bit : ' + str(sample.col_bit))
        if(answer=='1'):
            col1 = input('string 입력')
            col2 = input('date 입력')
            col3 = input('text 입력')
            col4 = input('int 값 입력')
            col5 = input('float 입력')
            col6 = input('bit 입력')
            temp = Table1(col_string=col1, col_date=col2, col_text=col3, col_int=col4, col_numeric=col5, col_bit=bool(int(col6)))
            db.session.add(temp)
            db.session.commit()
        if(answer=='2'):
            keyword = input('검색 col_string 입력')
            temp = Table1.query.filter_by(col_string=keyword).first()
            col2 = input('date 입력')
            col3 = input('text 입력')
            col4 = input('int 값 입력')
            col5 = input('float 입력')
            col6 = input('bit 입력')
            temp.col_date=col2
            temp.col_text=col3
            temp.col_int=col4
            temp.col_numeric=col5
            col_bit=bool(int(col6))
            db.session.commit()
        if(answer=='3'):
            keyword = input('검색 col_string 입력')
            temp = Table1.query.filter_by(col_string=keyword).first()
            db.session.delete(temp)
            db.session.commit()
        if(answer=='4'):
            keyword = input('검색 col_string 입력')
            temp = Table1.query.filter_by(col_string=keyword).first()
            print(temp.col_string)
            print(temp.col_date)
            print(temp.col_text)
            print(temp.col_int)
            print(temp.col_numeric)
            print(temp.col_bit)
            




