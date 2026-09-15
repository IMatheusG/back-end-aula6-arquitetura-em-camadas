class LivroRepository:
    def __init__(self):
        self.livros = []
        self._proximo_id = 1 # o _ serve pra mostrar q é privado, mas não muda nada no código, apenas visual

    def salvar(self, livro): # cadastro d livro
        livro.id = self._proximo_id
        self._proximo_id += 1
        self.livros.append(livro)
        # print(self.livros)
        return livro

    def listar(self):
        return self.livros

    def buscar_por_id(self, livro_id):
        for livro in self.livros:
            if livro.id == livro_id:
                return livro
        return None
            