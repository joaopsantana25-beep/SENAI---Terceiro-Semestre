from fastapi import APIRouter
import metodos

router = APIRouter()

@router.get("/")
def homePage():
    return {"mensagem": "Bom dia"}

@router.get("/produtos/totalCategoria")
def totalCategoria():
    return metodos.valorTotalCategoria()

@router.get("/produtos")
def listarProdutos():
    return metodos.listarProdutosCadastrados()

@router.get("/saidas")
def listarSaidas():
    return metodos.listarTodasSaidas()

@router.get("/produtos/limiteEstoque")
def limiteEstoque():
    return metodos.listarProdutosLimite()

    
@router.get("/saidas/volumeSaida")
def volumeSaida():
        return metodos.listarVolumeSaida()

@router.post("/produtos/cadastrar")
def cadastrarProduto(nomeProduto:str,valorUnitario:float,categoria:str,unidadeMedida:str,quantidadeProduto:int):
    return metodos.cadastrarNovoProduto(nomeProduto, valorUnitario, categoria,unidadeMedida, quantidadeProduto)
            

@router.post("/entradas/cadastrar")
def cadastrarEntrada(idProduto:int, dataEntrada:str, quantidadeEntrada:int):
    return metodos.registrarEntradas(idProduto,dataEntrada,quantidadeEntrada)