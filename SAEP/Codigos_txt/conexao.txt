import mysql.connector  

def criarConexao():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "saep"
    )

    return conexao


