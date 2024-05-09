from modelos.livros import Livro
import os

def main():
    exibir_titulo_app()
    exibir_menu()
    escolher_opcao()

def exibir_titulo_app():
    os.system('cls')
    print('''
██████╗░██╗██████╗░██╗░░░░░██╗░█████╗░████████╗███████╗░█████╗░░█████╗░
██╔══██╗██║██╔══██╗██║░░░░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
██████╦╝██║██████╦╝██║░░░░░██║██║░░██║░░░██║░░░█████╗░░██║░░╚═╝███████║
██╔══██╗██║██╔══██╗██║░░░░░██║██║░░██║░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
██████╦╝██║██████╦╝███████╗██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝██║░░██║
╚═════╝░╚═╝╚═════╝░╚══════╝╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝
''')

def exibir_menu():
    print('1. Exibir catálogo de livros')
    print('2. Pesquisar livros')
    print('3. Adicionar livro')
    print('4. Remover livro')
    print('5. Emprestar/devolver livro')
    print('6. Fechar app\n')

def voltar_menu_principal():
    input('Aperte uma tecla para voltar ao menu: ')
    main()

def escolher_opcao():
    
    try:
        opcao = int(input('Escolha uma opção: \n'))
        os.system('cls')
        match opcao:
            case 1:
                Livro.mostrar_catalogo()
                
                voltar_menu_principal()

            case 2:
                pesquisa = int((input('''Quer filtrar por:
1. Titulo
2. Gênero
3. Autor
Escolha a opção: ''')))
                match pesquisa:
                    case 1:
                        os.system('cls')
                        pesquisar_nome(input('Digite o titulo: \n'))
                        print()
                        voltar_menu_principal()

                    case 2:
                        os.system('cls')
                        pesquisar_genero(input('Digite o genero: \n'))
                        print()
                        voltar_menu_principal()
                    case 3:
                        os.system('cls')
                        pesquisar_autor(input('Digite o autor: \n'))
                        print()
                        voltar_menu_principal()
            case 3:
                titulo = input('Título: ')
                autor = input('Autor: ')
                genero = input('Gênero: ')
                cadastrar_livro(titulo, autor, genero)
                
            case 4:
                Livro.mostrar_catalogo()
                i = int(input('Digite o índice do livro que deseja remover: '))
                del Livro.catalogo_de_livros[i - 1]
                voltar_menu_principal()

            case 5:
                Livro.mostrar_catalogo()
                i = int(input('Digite o índice do livro que deseja alterar: '))
                Livro.catalogo_de_livros[i - 1].emprestar_ou_devolver
                voltar_menu_principal()

            case 6:
                os.system('cls')
                print('Saindo do app...')

    except:
        os.system('cls')
        print('Opção não encontrada.\n')
        exibir_menu()
        escolher_opcao()


def pesquisar_nome(nome):
    livros_titulo = Livro.filtro_nome(nome)
    for livro in livros_titulo:
        print(livro)

def pesquisar_genero(genero):
    livros_genero = Livro.filtro_genero(genero)
    for livro in livros_genero:
        print(livro)

def pesquisar_autor(autor):
    livros_autor = Livro.filtro_autor(autor)
    for livro in livros_autor:
        print(livro)

def cadastrar_livro(titulo, autor, genero):
    Livro(titulo, autor, genero)
    voltar_menu_principal()


if __name__ == '__main__':
    main()

