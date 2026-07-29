from fastapi import FastAPI
import funcoes


app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Olá, mundo!"}

@app.get("/usuarios/{usuario_id}")
def obter_usuario(usuario_id: int):
    frutas = []
    for i in range (usuario_id):
        frutas.append(i)
    
    return {
        "id": frutas
    }

@app.get("/funcionarios")
def funcionarios():
    return funcoes.verTableFuncionarios()

@app.post("/usuarios")
def criar_usuario(nome: str):
    return {
        "mensagem": "Usuário criado com sucesso!",
        "nome": nome
    }