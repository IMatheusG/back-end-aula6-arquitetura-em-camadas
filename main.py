from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Minha primeira API com FastAPI!"}