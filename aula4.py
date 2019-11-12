#abertura de arquivo texto para gravação

arquivo = open('alunos.txt','a')
arquivo.write('testando inserção\n')
arquivo.close()

#abertura do arquivo para leitura
arquivo = open('alunos.txt','r')
for d in arquivo:
    print(d)
arquivo.close()

#abertura do arquivo para gravação com fechamento automatico
with open ('alunos.txt','a') as arquivo:
    arquivo.write('testando fechamento automatico\n')
    