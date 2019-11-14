class Carro:
    def __init__(self, marca='' , modelo='', categoria='', ano=0):
        self.marca = marca
        self.modelo = modelo
        self.categoria = categoria
        self.ano = ano

    def lista_todos(self):
        lista_veiculos = [] #lista
        with open ('CursoPythonNt/Aula5/carros.txt' , 'r') as arquivo : #R de READ
            for c in arquivo:
                cl = c.strip().split(';')
                carro = Carro(cl[0], cl[1], cl[2], cl[3])
                lista_veiculos.append(carro)
        return lista_veiculos

    def cadastrar(self,):
        with open ('CursoPythonNt/Aula5/carros.txt','a') as arquivo :
            arquivo.write(f'{self.marca};{self.modelo};{self.categoria};{self.ano}\n')


   
# ----- Método para cadastro em arquivo texto

    def cadastrar(self):
        with open('CursoPythonNt/Aula5/carros.txt', 'a') as arquivo:
            # ----- Ao gravar a linha no arquivo texto f'{self}\n, o self, que é a própria classe ------ COMENTÁRIO ------
            # ----- é convertida em string, e ao ser convertida, é chamado o método __str__ declarado a baixo ------ COMENTÁRIO ------
            arquivo.write(f'{self}\n')

# -----------------------------------------------------------------------------------------

    # ----- Método de conversão da classe para string 
    # # ----- Sempre que a classe for convertida para string (str()) este método será chamado 
    def __str__(self):
        return f'{self.marca};{self.modelo};{self.categoria};{self.ano}'