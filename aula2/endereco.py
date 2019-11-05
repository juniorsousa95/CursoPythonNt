class Endereco:
    logradouro = ''
    numero = ''
    complemento = ''
    bairro = ''
    cidade = ''
    cep = ''
    endereco = ''

    def cadastrar_endereço(self):
        self.logradouro = input('Digite seu logradouro: ')
        self.numero = input('Digite seu numero: ')
        self.complemento = input('Digite o complemento: ')
        self.bairro = input('Digite seu bairro: ')
        self.cidade = input('Digite sua cidade: ')
        self.cep = input('Digite seu cep: ')
        endereco = f'Logradouro: {self.logradouro} Numero: {self.numero} Complemento: {self.complemento} Bairro:  {self.bairro} Cidade:  {self.cidade} Cep:  {self.cep}'
        return endereco