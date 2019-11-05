class Pessoa: 
    nome =''
    sobrenome =''
    data_nascimento = ''
    email = ''
    senha = ''
    

    def cadastrar_pessoa(self):
        self.nome = input('digite seu nome: ')
        self.sobrenome = input('digite seu sobrenome: ')
        self.data_nascimento = input('digite sua data de nascimento: ')
        self.email = input('digite seu email :')
        self.senha = input('digite sua senha : ')
        pessoa = f'Nome:{self.nome}\n Sobrenome : {self.sobrenome}\n DataNas :{self.data_nascimento }\n Email: {self.email}\n Senha {self.senha}'
        return pessoa