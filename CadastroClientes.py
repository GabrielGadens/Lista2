class Cliente():
    def __init__(self,nome,sobrenome,nasc,email,cpf,senha):
        self.status = True
        self.tentativa = 0
        self.nome=nome
        self.sobrenome=sobrenome
        self.nasc=nasc
        self.email=email
        self.cpf=cpf
        self.senha=senha

    def login(self):
        senha=input('Qual sua senha?')
        if senha==self.senha:
            self.tentativa=0
            print('senha correta!!!')
            print('Nome: ',self.nome,'',self.sobrenome)
            print('Data de nascimento: ',self.nasc)
            print('E-mail: ',self.email)
            print('CPF: ',self.cpf)
        else:
            print('Senha Incorreta!!!')
            self.tentativa=int(self.tentativa)+1
            if self.tentativa==3:
                self.status=False
                print('Conta BLOQUEADA')
                return False
            else:
                return True

print('Bem vindo ao cadastro!')
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
nasc = input('Data de nascimento: dd/mm/aaaa ')
email = input('E-mail: ')
cpf = input('CPF: ')
senha = input('Senha: ')

cliente = Cliente(nome,sobrenome,nasc,email,cpf,senha)
i=True
while (i):
    i=cliente.login()
    

            
    
