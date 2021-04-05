class AA():
    def __init__(self):
        self.attA = 'a'
        self.attB = 'b'
        self.attC = 'c'

a = AA()
print(a.attC)
# print(a.c) 여기서는 오류 발생 (해당 속성이 존재하지 않음)
setattr(a, 'attC', 5) # 속성값을 변경해줌
setattr(a, 'c', 5)  # 속성을 만들어서 넣어줌
print(a.attC)
print(a.c)