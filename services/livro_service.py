# repository serve como base de dados, mas na vdd é apenas algumas arrays
class LivroService:
    def __init__(self, repository):
        self.repository = repository

    def criar_livro(self, livro):
        if livro.estoque < 0:
            raise ValueError("Estoque não pode ser negativo") # lança erro
        return self.repository.salvar(livro) # executa a inserção no repository com os dados q vieram dps de validar acima
    
    def listar_livro(self):
        return self.repository.listar() # apenas puxa os dados/livros do repository

    def emprestar_livro(self, livro_id):
        livro = self.repository.buscar_por_id(livro_id) # busca o livro no repository
        # validações
        if livro is None:
            raise ValueError("Livro não encontrado")
        if livro.estoque <= 0:
            raise ValueError("Livro sem exemplares disponíveis")
        
        livro.estoque -= 1
        return livro