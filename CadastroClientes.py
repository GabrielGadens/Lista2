class Data():
    def __init__(self,dia,mes,ano):
        self.dia=dia
        self.mes=mes
        self.ano=ano
    
    def retornaDia(self):
        return self.dia

    def retornaDataNasc(self):
        data=str('{}/{}/{}'.format(self.dia,self.mes,self.ano))
        return data
    
class Cliente():
    def __init__(self):
        self.__status = True
        self.__tentativa = 0
        self.nome=''
        self.sobrenome=''
        self.data=Data(0,0,0)
        self.__email=''
        self.__cpf=''
        self.__senha=''

    def alterarDataNascimento(self, dia, mes, ano):
        self.data = Data(dia,mes,ano)
        
    
    def setCliente(self,nome,sobrenome,dia,mes,ano,email,cpf,senha):
        self.nome=nome
        self.sobrenome=sobrenome
        self.alterarDataNascimento(dia,mes,ano)
        self.__email=email
        self.__cpf=cpf
        self.__senha=senha

    def diaNascimento(self):
        print('Ele nasceu no dia ',self.data.retornaDia())

    def login(self):
        if self.__status==True:    
            senha=input('Qual sua senha?')
            if senha==self.__senha:
                self.__tentativa=0
                print('senha correta!!!')
                print('Olá')
                print('Nome: ',self.nome,'',self.sobrenome)
                print('Data de nascimento: ',self.data.retornaDataNasc())
                print('E-mail: ',self.__email)
                print('CPF: ',self.__cpf)
            else:
                print('Senha Incorreta!!!')
                self.__tentativa=int(self.__tentativa)+1
                if self.__tentativa==3:
                    self.__status=False
                    print('Conta BLOQUEADA')
                    return False
                else:
                    return True
        else:
            print('Conta bloqueada!!!')
            
print('Bem vindo ao cadastro!')
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
dia = input('dia de nascimento: dd ')
mes = input('mes de nascimento: mm ')
ano = input('ano de nascimento: aaaa ')
email = input('E-mail: ')
cpf = input('CPF: ')
senha = input('Senha: ')

cliente = Cliente()
cliente.setCliente(nome,sobrenome,dia,mes,ano,email,cpf,senha)
i=True
while (i):
    i=cliente.login()
    

  
