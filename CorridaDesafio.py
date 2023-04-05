import random
class Competidor:
    def __init__(self):
        self.__nome = ''
        self.__pos = 0
    
    def setNome(self,nome):
        self.__nome=nome
    def atualizar(self):
        numero = random.randint(1,6)
        self.__pos+=numero
        
        if self.__pos%5==0:
            self.__pos-=1
            print('Número sorteado ',numero,'   Seguindo a regra dos multiplos de 5 o ',self.__nome,' ficou na casa Nº',self.__pos)
            return self.__pos
        elif self.__pos==7 or self.__pos==17:
            self.__pos+=2
            print('Número sorteado ',numero,'   Seguindo a regra do 7 e 17 o ',self.__nome,' ficou na casa Nº',self.__pos)
            return self.__pos
        elif self.__pos==13:
            self.__pos==0
            print('Número sorteado ',numero,'   Seguindo a regra do 13 o ',self.__nome,' retona na casa Nº',self.__pos)
            return self.__pos
        if self.__pos>=20:
            print(self.__nome,' Ganhou!!!!')
            print('Número sorteado ',numero,'   chegando a casa ',self.__pos)
            return self.__pos
            
        else:
            print('Número sorteado ',numero,'   ',self.__nome,' ficou na casa Nº',self.__pos)
            return self.__pos
            
c1=Competidor()
c2=Competidor()
c3=Competidor()
c4=Competidor()
c1.setNome('sonic')
c2.setNome('papa léguas')
c3.setNome('flash')
c4.setNome('ligeirinho')
fim=1
i=[0,0,0,0]
while(fim!=0):
    print('\nRODADA Nº',fim)
    i[0]=c1.atualizar()
    i[1]=c2.atualizar()
    i[2]=c3.atualizar()
    i[3]=c4.atualizar()
    fim+=1
    for x in range(0,4):
        if i[x]>=20:
            fim=0
