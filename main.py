from fastapi import FastAPI
from routers import livro_router # importando o livro_router

app = FastAPI()
app.include_router(livro_router.router) # incluindo as rotas definidas no livro_router

# @app.get("/")
# def raiz():
#     return {"mensagem": "Minha primeira API com FastAPI!"}