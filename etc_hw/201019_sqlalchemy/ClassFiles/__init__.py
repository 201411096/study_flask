import os

# print(__file__)
# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))

def getFileNameList(fileList):
    resultList = []
    for file in fileList:
        # print(file.split('.')[0])
        resultList.append(file.split('.')[0])
    return resultList

currentDir = os.path.dirname(__file__)
fileList = os.listdir(currentDir)
fileList = getFileNameList(fileList)

__all__ = fileList

