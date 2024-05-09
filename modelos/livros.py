class Livro:
    catalogo_de_livros = []

    def __init__(self, titulo, autor, genero):
        self.titulo = titulo.upper()
        self.autor = autor.upper()
        self.genero = genero.upper()
        self.disponivel = True
        Livro.catalogo_de_livros.append(self)

    def __str__(self) -> str:
        return f'Título: {self.titulo.ljust(20)} | Autor: {self.autor.ljust(20)} | Gênero: {self.genero.ljust(20)} | Disponibilidade: {self.status}'

    @property
    def status(self):
        return '✅' if self.disponivel else '❌'
    
    @property
    def emprestar_ou_devolver(self):
        self.disponivel = not self.disponivel

    @classmethod
    def mostrar_catalogo(cls):
        i = 0
        for livro in (cls.catalogo_de_livros):
            i += 1
            print(f'{i} - |{livro}')

    @staticmethod
    def filtro_genero(genero):
        livros_filtrados = [livro for livro in Livro.catalogo_de_livros if livro.genero == genero.upper()]
        return livros_filtrados

    @staticmethod
    def filtro_nome(nome):
        livros_filtrados = [livro for livro in Livro.catalogo_de_livros if livro.titulo == nome.upper()]
        return livros_filtrados

    @staticmethod
    def filtro_autor(autor):
        livros_filtrados = [livro for livro in Livro.catalogo_de_livros if livro.autor == autor.upper()]
        return livros_filtrados
    

livro1 = Livro('Neuromancer', 'William Gibson', 'Ficção') 
livro2 = Livro('A vida invisível de Addie Larue', 'V. E. Schwab', 'Fantasia')
livro3 = Livro('Trono de Vidro', 'Sarah J. Maas', 'Fantasia')
