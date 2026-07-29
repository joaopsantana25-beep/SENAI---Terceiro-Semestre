#Conexão com o Banco de dados
conexao = None

def criarconexao():
    import mysql.connector 

    global conexao

    conexao=mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root"
    )

    print("Conexão Criada")
    return conexao 
    

#Criar Banco

def criarBanco(nomeBanco):
    conexao = criarconexao()
    cursor=conexao.cursor()

    cursor.execute(f'Create DATABASE IF NOT EXISTS {nomeBanco}')
    print("Banco criado com sucesso")

   

def criarTableFuncionarios():
    conexao = criarconexao()
    cursor = conexao.cursor()

    cursor.execute("""
    USE GLOW;
    Create Table if NOT EXISTS FUNCIONARIOS(
        id_funcionario int auto_increment primary key,
        nome varchar(100) not null
        )
    """)

    print("Tabela de funcionários criada com sucesso")


#Função adicionar funcionario

def adicionarFuncionario(nomeFuncionario):
    conexao = criarconexao()
    cursor = conexao.cursor()
    cursor.execute("USE GLOW")
    
    comando_sql = " INSERT INTO funcionarios (nome) values (%s)"



    cursor.execute(comando_sql,(nomeFuncionario,))
    conexao.commit()
    print("Dados Inseridos")


#Ver a tabela funcionarios

def verTableFuncionarios():
    conexao = criarconexao()
    cursor = conexao.cursor()
    cursor.execute("USE GLOW")

    comando_sql = """
    Select *
    from funcionarios; """

    cursor.execute(comando_sql)
    funcionarios = cursor.fetchall()

    lista=[]

    for p in funcionarios:
       lista.append({
           "id": p[0],
           "nome": p[1]
       })

    return lista