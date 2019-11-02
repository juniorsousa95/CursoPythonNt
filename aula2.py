from pessoa import Pessoa
from endereco import Endereco

print('='*50)
print('\n'*2)

pessoa = Pessoa()
endereco = Endereco()

print(pessoa.cadastrar_pessoa())
print('\n')
print(endereco.cadastrar_endereço())
