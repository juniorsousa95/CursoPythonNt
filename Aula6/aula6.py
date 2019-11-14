from flask_mysqldb import MySQLdb


conexao = MySQLdb.connect(host='mysql.zuplae.com', user='zuplae04', passwd='lendas19', database='zuplae04')
cur = conexao.cursor()

cur.execute('SELECT * FROM Cliente')

for c in cur.fetchall():
    print(c)