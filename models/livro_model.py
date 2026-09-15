from pydantic import BaseModel

class Livro(BaseModel):
    id: int | None = None # deixa vazio se receber None como parâmetro
    titulo: str
    autor: str
    estoque: int