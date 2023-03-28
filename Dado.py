import random
class Dado:
    def __init__(self, faces):
        self.faces = faces
    def rolar(self):
        return random.randint(1,self.faces)
i = True
while (i):
    faces = int(input('Número de faces? 6, 8 ou 12\n'))
    if faces == 6 or faces == 8 or faces == 12 :
        d1 = Dado(faces)
        print(d1.rolar())
        i=False
    else:
        print('Número inválido')

