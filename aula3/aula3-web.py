from flask import Flask, render_template
from aluno import Aluno
from avaliacoes import Avaliacao

aluno1 = Aluno()
aluno1.nome = 'Junior'
aluno1.sobrenome = 'Sousa'
aluno1.usuario = '123'
aluno1.senha = '123'

aluno2= Aluno()
aluno2.nome = 'joao'
aluno2.sobrenome = 'silva'
aluno2.usuario = '321'
aluno2.senha = '321'

avaliacao = Avaliacao()
avaliacao.data = '06/11/2019'
avaliacao.nome = 'matematica'
avaliacao.nota = '9,0'


avaliacao2 = Avaliacao()
avaliacao.data = '05-11-2019'
avaliacao.nome = 'Fisica'
avaliacao.nota = ' 5'

app = Flask(__name__)

nome_pagina = 'Pagina do joca1000'
lista_teste = [aluno1, aluno2]
lista_avaliacao = [avaliacao, avaliacao2]



@app.route('/')
def inicio():
    return render_template('home.html', nome=nome_pagina, lista = lista_teste) #só existe dentro desse contexto

@app.route('/contato')
def contatos():
    return render_template('contato.html', nome=nome_pagina, lista = lista_avaliacao)

app.run(debug=True)