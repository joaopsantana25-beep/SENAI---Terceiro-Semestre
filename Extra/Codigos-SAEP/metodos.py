import mysql
from conexao import criarConexao


def valorTotalCategoria():
    conexao = criarConexao()
    cursor = conexao.cursor()

    try: 
        comando_sql="""
            SELECT 
            categoria,
            sum(quantidade_produto*valor_unitario) as "Valor Categoria"
            from produtos
            GROUP BY categoria;
        """

        cursor.execute(comando_sql)
        valorTotal = cursor.fetchall()

        listaValoresTotais = []

        for valor in valorTotal:
            listaValoresTotais.append({
                valor[0] : valor[1]
            })

        return listaValoresTotais

    except Exception as erro:
        return "Erro ao carregar tabela"

    finally:
        cursor.close()
        conexao.close()
        
def listarProdutosCadastrados():
    conexao = criarConexao()
    cursor = conexao.cursor()

    try:
        comando_sql=""" 
            SELECT *
            FROM produtos;
        """

        cursor.execute(comando_sql)
        produtos = cursor.fetchall()

        listaProdutosCadastrados = []

        for produto in produtos:
            listaProdutosCadastrados.append({
                "id":produto[0],
                "nome_produto":produto[1],
                "valor_unitario":produto[2],
                "categoria":produto[3],
                "unidade_medida":produto[4],
                "quantidade_produto":produto[5]
            })

        return listaProdutosCadastrados

    except Exception as erro:
        return "Erro ao carregar tabela"

    finally:
        cursor.close()
        conexao.close()


def listarTodasSaidas():
    conexao = criarConexao()
    cursor = conexao.cursor()

    try:
        comando_sql="""
            SELECT *
            from saidas
            order by data_saida DESC;
        """

        cursor.execute(comando_sql)
        saidas = cursor.fetchall()

        listaTodasSaidas=[]

        for saida in saidas:
            listaTodasSaidas.append({
                "id_saida":saida[0],
                "id_produto":saida[1],
                "data_saida":saida[2],
                "quantidade_saida":saida[3]
            })

        return listaTodasSaidas


    except Exception as erro:
        return "Erro ao carregar tabela"

    finally:
        cursor.close()
        conexao.close()


def cadastrarNovoProduto(nomeProduto, valorUnitario, categoria,unidadeMedida, quantidadeProduto):
    unMedida = unidadeMedida
    qtdProduto = quantidadeProduto

    if not nomeProduto or not nomeProduto.strip():
        return "Nome Inválido"

    if not valorUnitario or valorUnitario<=0:
        return "Valor do produto inválido"

    if not categoria or not categoria.strip():
        return "Categoria Inválida"

    if not unidadeMedida or not unidadeMedida.strip():
        unMedida = None

    if not quantidadeProduto:
        qtdProduto=0

    if quantidadeProduto<0 or quantidadeProduto>100:
        return "Quantidade Inválida"

    try:
        conexao = criarConexao()
        cursor = conexao.cursor()

        valores = (nomeProduto, valorUnitario, categoria,unMedida,qtdProduto)

        comando_sql = """
            INSERT INTO produtos(nome_produto,valor_unitario,categoria,unidade_medida,quantidade_produto)
            values (%s,%s,%s,%s,%s)
        """

        cursor.execute(comando_sql,valores)
		cursor.commit()

        return "Valores Inseridos com Sucesso"

    except Exception as erro:
        return "Falha ao inserir valores"

    finally:
        cursor.close()
        conexao.close()

def registrarEntradas(idProduto,dataEntrada,quantidadeEntrada):
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) from produtos")
    quantidadeProdutos = cursor.fetchall()[0][0]

    cursor.close()
    conexao.close()

    if idProduto>quantidadeProdutos or idProduto<=0:
        return "Id Inválido"

    if quantidadeEntrada>100 or quantidadeEntrada<=0  :
        return "Quantidade Inválida"

    try: 
        conexao=criarConexao()
        cursor = conexao.cursor()

        comando_sql = """
            INSERT INTO entradas(id_produto,data_entrada,quantidade_entrada)
            values (%s,%s,%s) 
        """

        valores = (idProduto,dataEntrada,quantidadeEntrada)

        cursor.execute(comando_sql,valores)
		cursor.commit()

        return "Valores inseridos com sucesso"

    except Exception as erro:
        return "Erro ao registrar entrada"

    finally:
        cursor.close()
        conexao.close()


def listarProdutosLimite():
    conexao = criarConexao()
    cursor = conexao.cursor()

    try:
        comando_sql="""
            SELECT 
            nome_produto,
            quantidade_produto,
            (quantidade_produto/100) as "Percentual do Estoque"
            FROM PRODUTOS
            WHERE quantidade_produto = 0 or quantidade_produto=100;
        """

        cursor.execute(comando_sql)

        produtos = cursor.fetchall()

        listaProdutos = []

        for produto in produtos:
            listaProdutos.append({
                "nome_produto":produto[0],
                "quantidade":produto[1],
                "percentual":produto[2]
            })

        return listaProdutos

    except Exception as erro:
        return "Erro ao carregar tabela"

    finally:
        cursor.close()
        conexao.close()


def listarVolumeSaida():
    conexao = criarConexao()
    cursor = conexao.cursor()

    try:
        comando_sql = """
            SELECT 
            produtos.nome_produto,
            COUNT(*) as "Quantidade Total de Saida",
            SUM(saidas.quantidade_saida*produtos.valor_unitario) as "Valor Total Financeiro"
			from saidas
            inner join produtos
            on produtos.id_produto = saidas.id_produto
			group by saidas.id_produto, produtos.nome_produto
            order by COUNT(*) DESC LIMIT 3;
        
        """

        cursor.execute(comando_sql)

        volumeSaida = cursor.fetchall()

        listaVolumeSaida = []

        for saida in volumeSaida:
            listaVolumeSaida.append({
                "nome do produto":saida[0],
                "quantidade total de saída": saida[1],
                "valor total financeiro": saida[2]
            })


        return listaVolumeSaida

    except Exception as erro:
        return "Erro ao carregar a tabela"

    finally:
        cursor.close()
        conexao.close()







    
