from fastapi import FastAPI
from rotas import router
import conexao
import metodos
 
app = FastAPI()

app.include_router(router)




