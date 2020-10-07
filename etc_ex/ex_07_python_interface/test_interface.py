from abc import *
 
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
 
    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    # 구현이 안되는 메소드가 있을 경우 오류 발생
    def study(self):
        print('공부하기')    
    def go_to_school(self):
        print('학교')
 
james = Student()
james.study()