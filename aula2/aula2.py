from pessoa import Pessoa
from endereco import Endereco

print('='*50)
print('\n'*2)

pessoa = Pessoa() 
endereco = Endereco()
pessoa.cadastrar_pessoa()
endereco.cadastrar_endereço()

print(pessoa.nome)
print('\n')
print(endereco.logradouro)

