import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor()

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
#c.commit()

'''
#====Para fazer o select no banco de dados=========
# Executa o comando:
c.execute("SELECT nome, cpf FROM alunos WHERE id_aluno = 1 ")

# Recupera o resultado:
resultado = c.fetchall()

# Mostra o resultado:
print('ALUNO ')

for linha in resultado :
    print(linha)

# Finaliza a conexão
c.close()
#=====================================================
'''

#====Para fazer inserir no banco de dados=========
# Executa o comando:
c.execute("INSERT INTO alunos (id_aluno, nome, data_nascimento, endereco, cidade, estado, cpf) VALUES (DEFAUlT, 'João Pedro', '2000-01-01', 'Av das pedras, 123', 'Betim', 'MG', '12345678911')")

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
con.commit()

# Finaliza a conexão
con.close()
#=====================================================

