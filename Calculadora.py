class Calculadora():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def somar(self):
        return (self.num1+self.num2)
    def subtrair(self):
        return (self.num1-self.num2)
    def multiplicar(self):
        return (self.num1*self.num2)
    def dividir(self):
        if self.num1>0 and self.num2>0:
            return (self.num1/self.num2)
        else:
            return -1

nums1 = Calculadora(3,0)
print(nums1.somar())
print(nums1.subtrair())
print(nums1.multiplicar())
print(nums1.dividir())



