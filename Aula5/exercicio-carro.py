from flask import Flask, render_template, request, redirect #criação de rotas
from carro import Carro

nome_pagina = 'Veiculos' #nome da pagina do navegador
app = Flask (__name__) #

@app.route('/') #rota de acesso a pagina web
def inicio (): #metodo
    carro = Carro()
    return render_template('index-carro.html', nome = nome_pagina, lista = carro.lista_todos() )

@app.route('/cadastrar') # rota de acesso a pagina web de cadastro
def cadastrar():
    return render_template('cadastro-carro.html', nome = nome_pagina)

@app.route ('/salvar')
def salvar():
    marca = request.args['marca']
    modelo = request.args['modelo']
    categoria = request.args['categoria']
    ano = request.args['ano']
    carro = Carro(marca, modelo, categoria, ano)
    carro.cadastrar()
    return redirect('/')
    
app.run(debug=True)