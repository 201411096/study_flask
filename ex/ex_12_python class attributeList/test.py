class AA():
    def __init__(self):
        self.attA = 'a'
        self.attB = 'b'
        self.attC = 'c'

a = AA()
print(a.__dict__)
print(a.__dict__.keys())