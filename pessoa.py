class Pessoa: 
    

    def cadastrar_pessoa(self):
        nome = input('digite seu nome: ')
        sobrenome = input('digite seu sobrenome: ')
        data_nascimento = input('digite sua data de nascimento: ')
        email = input('digite seu email :')
        senha = input('digite sua senha : ')
        pessoa = f'Nome:{nome}\n Sobrenome : {sobrenome}\n DataNas : {data_nascimento }\n Email: {email}\n Senha {senha}'
        return pessoa