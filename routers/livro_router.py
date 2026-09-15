from fastapi import APIRouter, HTTPException, Depends
from models.livro_model import Livro
from services.livro_service import LivroService
from repositories.livro_repository import LivroRepository

router = APIRouter()

def get_livro_service():
    return LivroService(LivroRepository())

@router.post("/livros")
def criar_livro(livro: Livro, service: LivroService = Depends(get_livro_service)): # instancia o service, fazendo ele ser dependente do get_livro_service
    try: # tenta executar
        return service.criar_livro(livro)
    except ValueError as e: # caso receba valueError q é só um txt pra quando dá erro
        raise HTTPException(400, e) # dá o erro no http

@router.get("/livros")
def listar_livros(service: LivroService = Depends(get_livro_service)):
    return service.listar_livro()

@router.post("/livros/{livro_id}/emprestar")
def emprestar_livro(livro_id: int, service: LivroService = Depends(get_livro_service)):
    try:
        return service.emprestar_livro(livro_id)
    except ValueError as e:
        raise HTTPException(400, e)