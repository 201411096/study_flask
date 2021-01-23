# \t => '    '
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, distinct, case, between
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import pandas as pd
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

app = Flask(__name__)
CORS(app)

dbName = "kimyongseon"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/'+dbName
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


# snakeCase To camelCase
def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])

def makeTempTableName(tableName):
    # tempTableName = tableName[3].upper() + tableName[4:] #appspeed 사용시 ..
    tempTableName = tableName[0].upper() + tableName[1:]
    return tempTableName

def appendImportStringToFileContent(fileContent):
    fileContent += """"""
    return fileContent

def generateFile(tableName, tableComment):
    columnArray = []
    fileContent = """"""

    fileContent = appendImportStringToFileContent(fileContent)

    tempTableName = makeTempTableName(tableName)

    fileContent += 'class '+ to_camel_case(tempTableName) +'(Base):\n'
    fileContent += '    __tablename__ = ' + "'" + tableName + "' #"+ tableComment +" \n"
    fileContent += '    __table_args__ = {\n'
    fileContent += "            'comment' : '"+tableComment+"'\n"
    fileContent += "        }\n\n"

    tableStructures = db.session.execute('desc ' + tableName)
    pkFlag = True
    pkColumn = ''
    for tableStructure in tableStructures:
        print(tableStructure)
        queryForComment = "SELECT column_comment FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema = '{0}' AND TABLE_NAME = ".format(dbName)
        queryForComment += "'"+tableName+"' and COLUMN_NAME = '"+tableStructure[0]+"'"
        tempComment = db.session.execute(queryForComment)
        for temp in tempComment:
            tempComment = str(temp[0])
        
        fileContent += "    " 
        fileContent += '%-15s                      = Column(' % str(tableStructure[0]) 
        if(tableStructure[1][0:8]=='longtext'):
            fileContent+= 'TEXT, '
        elif(tableStructure[1][0:3]=='int'):
            fileContent+= 'Integer, '
        elif(tableStructure[1][0:6]=='double'):
            fileContent+= 'Numeric' + tableStructure[1][6:] +', '
        elif(tableStructure[1][0:7]=='decimal'):
            fileContent+= 'Numeric' + tableStructure[1][7:] +', '
        else:
            fileContent+= str(tableStructure[1]).upper()+', '
            
        if(pkFlag == True):
            pkFlag = False
            pkColumn = tableStructure[0]
            fileContent += 'primary_key=True, '
        elif(tableStructure[2]=='NO'):
            fileContent += 'nullable=False, '
        fileContent += "comment='%s') # %s" % (tempComment, tempComment)
        fileContent += "\n"
    fileContent += '\n    def __init__(self, %s, **kwargs):\n' % to_camel_case(pkColumn.lower())
    fileContent +='        self.'+pkColumn+' = '+to_camel_case(pkColumn.lower())+'\n\n'
    pkFlag = True

    tableStructures2 = db.session.execute('desc ' + tableName)
    for tableStructure2 in tableStructures2:
        if(pkFlag==True):
            pkFlag=False
            continue
        fileContent+='        '
        fileContent+='self.%-30s' % tableStructure2[0]
        fileContent+="= kwargs.get('%s', None)" % tableStructure2[0]
        fileContent+='\n'

    fileContent+='\n    def __repr__(self):\n'
    fileContent+='        return "{'

    pkFlag = True
    tableStructures3 = db.session.execute('desc ' + tableName)
    for tableStructure3 in tableStructures3:
        if(pkFlag == True):
            pkFlag = False
        else:
            fileContent+=', \\\n        '

        fileContent+="'"+tableStructure3[0]+"' : '%s'"
        columnArray.append(tableStructure3[0])
    fileContent+='}" % (\n'

    tableStructures4 = db.session.execute('desc ' + tableName)
    for tableStructure4 in tableStructures4:
        fileContent +='                    self.'+tableStructure4[0]
        if(columnArray[len(columnArray)-1] == tableStructure4[0]):
            continue
        else:
            fileContent +=',\n'

    fileContent+= ')'

    with open(to_camel_case(tempTableName)+'.py', 'w', encoding='utf-8') as f:
        f.write(fileContent)

    return Response(
        response = json.dumps({'test':'test'}),
        status = 200,
        mimetype="application/json"
    )

def getTableList():
    print('check in getTableList ...')
    query = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = '{0}'".format(dbName)
    result = db.session.execute(query)
    return result

def insertColumnComment():
    tableList = getTableList()
    commentList = [
      '게시판',
      '게시판리스트',
      '댓글',
      '파일',
      '그룹공통권한',
      '그룹별게시판권한',
      '회원',
      '회원그룹'
    ]
    if(len(commentList)==0):
        for i in range(len(getTableList().scalar())): # resultProxy.scalar() 사용시 rowcount가 됨, 하지만 result object가 closed되는 문제가 있어서 result object를 새로 받아옴
            commentList.append('')
    
    for idx, table in enumerate(tableList):
        if(commentList[idx]==''):
            commentList[idx]=='your_tableComment'
        generateFile(table[0], commentList[idx])

    return Response(
        response = json.dumps({'test':'test'}),
        status = 200,
        mimetype="application/json"
    )


if __name__ == '__main__':
    insertColumnComment()