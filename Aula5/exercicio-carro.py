from flask import Flask, render_template, request #criação de rotas
from carro import Carro

nome_pagina = 'Veiculos' #nome da pagina do navegador
app = Flask (__name__) #

@app.route('/') #rota de acesso a pagina web
def inicio (): #metodo
    lista_veiculos = [] #lista
    with open ('Aula5/carros.txt' , 'r') as arquivo : #R de READ
        for l in arquivo:
            vetor = l.split (';')
            lista_veiculos.append(vetor)
    return render_template('index-carro.html', nome = nome_pagina, lista = lista_veiculos)

@app.route('/cadastrar') # rota de acesso a pagina web de cadastro
def cadastrar():
    return render_template('cadastro-carro.html', nome = nome_pagina)

@app.route ('/salvar')
def salvar():
    marca = request.args['marca']
    modelo = request.args['modelo']
    categoria = request.args['categoria']
    ano = request.args['ano']
    with open ('Aula5/carros.txt','a') as arq :
        arq.write(f'{marca};{modelo};{categoria};{ano}\n')
    return 'Veiculo Salvo'
app.run(debug=True)