class Endereco:


    def cadastrar_endereço(self):
        logradouro = input('Digite seu logradouro: ')
        numero = input('Digite seu numero: ')
        complemento = input('Digite o complemento: ')
        bairro = input('Digite seu bairro: ')
        cidade = input('Digite sua cidade: ')
        cep = input('Digite seu cep: ')
        endereco = f'Logradouro: {logradouro} Numero: {numero} Complemento: {complemento} Bairro:  {bairro} Cidade:  {cidade} Cep:  {cep}'
        return endereco