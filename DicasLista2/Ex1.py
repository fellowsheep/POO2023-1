import random

class Dado:
    def __init__(self,faces):
        self.faces = faces

    def rolar(self):
        return random.randint(1,self.faces)
    

d6 = Dado(6)
d8 = Dado(8)
d12 = Dado(12)

for i in range (3):
    print(d6.rolar())
    print(d8.rolar())
    print(d12.rolar())

