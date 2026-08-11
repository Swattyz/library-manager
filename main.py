import os
from modules.buscar_livros import buscar_livro
from modules.cadastrar_livros import cadastrar_livro
from modules.listar_livros import listar_livros
from modules.descadastrar_livro import descadastrar_livro
from modules.emprestar_devolver_livros import emprestimo_devolucao
from modules.ordernar_listagem import ordenar_listagem
from modules.checar_titulo import checar_titulo
from modules.estoque_livro import estoque_livro

# Importa as funções que serão usadas de uma pasta com os módulos

os.system("cls") # Limpa o conteúdo atual do terminal

estrutura = ['titulo', 'autor', 'ano', 'isbn', 'disponivel', 'emprestado'] # Estrutura-base da headline do arquivo .CSV para catálogo de livros

# CÓDIGO PRINCIPAL (onde ocorre o processamento do código e as funções são chamadas)

print ("==== SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ====" \
"\nBem vindo ao gerenciador de livros da biblioteca, o que deseja fazer?") # Entrada principal do menu do código

while True:
    try:
        choice = int(input("\n[1] --- CADASTRAR LIVRO" \
        "\n[2] --- REGISTRAR EMPRÉSTIMO" \
        "\n[3] --- REGISTRAR DEVOLUÇÃO" \
        "\n[4] --- LISTAR LIVROS" \
        "\n[5] --- BUSCA DE LIVRO" \
        "\n[6] --- ORDENAR LISTAGEM" \
        "\n[7] --- DESCADASTRAR LIVRO" \
        "\n[8] --- AUMENTAR ESTOQUE DE LIVRO" \
        "\n[9] --- REDUZIR ESTOQUE DE LIVRO" \
        "\n[0] --- SAIR" \
        "\n--> "))
        # Menu de opções do código para cada função
    except ValueError:
        print("Opção inválida!\n")
        continue

    match choice: # Switch-case para o uso das funções conforme o pedido escolhido
        case 1: # Cadastro de livro
            while True:
                titulo = input("\n- Título do livro: ")

                if titulo.strip() == "":
                    print("\nO título não pode ser vazio!")
                    continue

                elif checar_titulo(titulo):
                    print("\nJá está cadastrado um livro cujo título é exatamente igual!")
                    continue

                autor = input("- Autor do livro: ")

                if autor.strip() == "":
                    print("\nO nome do autor não pode ser vazio!")
                    continue

                try: 
                    ano = int(input("- Ano do livro: "))

                    if ano > 2026 or ano < 0: # Se o valor do ano de lançamento do livro for maior que 2026 (ano atual) ou negativo/menor que zero
                        print("Valor do ano muito alto ou muito baixo! Tente novamente.\n")
                        continue
                except ValueError:
                    print("\nValor inválido!")
                    continue

                try:
                    isbn = int(input("- ISBN do livro (13 dígitos): "))

                    if len(str(isbn)) != 13: # Verifica se o ISBN tem um tamanho correto (de acordo com pesquisas, ISBNs atuais obrigatoriamente possuem 13 dígitos)
                        print(f"Esse ISBN possui {len(str(isbn))} dígito(s), certifique de que seu ISBN tenha 13 dígitos!\n")
                        continue

                    break

                except ValueError:
                    print("Valor inválido!\n")

            print(cadastrar_livro(titulo,autor,ano,isbn)) # Chama a função de cadastro de livros
            input("\n(Pressione 'Enter' para continuar)\n")

        case 2 | 3: # Empréstimo e devolução de livro
            if choice == 2:
                mode = "Emprestimo"
            else:
                mode = "Devolucao"
            # Checagem e declaração do modo pedido
            
            while True:
                titulo = input("\n- Insira o título do livro: ")
                if titulo.strip() == "":
                    print("\nO título não pode ser vazio!")
                    continue

                print(emprestimo_devolucao(titulo, mode)) # Chama a função de empréstimo e devolução de livros
                input("\n(Pressione 'Enter' para continuar)\n")
                break

        case 4: # Listagem de livros
            listar_livros() # Chama a função de listagem de livros (sem parâmetros pois lê o arquivo todo e lista tudo sem especificações)
            input("\n(Pressione 'Enter' para continuar)\n")

        case 5: # Busca de livros
            while True:
                try:
                    mode = int(input("\nEscolha o tipo de característica do livro queira utilizar para realizar a busca: " \
                    "\n[0] ---> Buscar por título." \
                    "\n[1] ---> Buscar por autor." \
                    "\n[2] ---> Buscar por ano de lançamento." \
                    "\n[3] ---> Buscar por ISBN." \
                    "\n[4] ---> Buscar por disponível." \
                    "\n[5] ---> Buscar por indísponível." \
                    "\n--> "))
                    # Menu de opções sobre o tipo de busca a ser feita
                except ValueError:
                    print(f"O valor dado não é válido!\n")
                    continue

                if mode not in [0,1,2,3,4,5]: # Se não for nenhuma das opções mostradas no menu
                    print(f"'{mode}' inválido! Tente novamente.\n")
                    continue

                elif mode in [4,5]:
                    value = 0
                    # Se a busca for sobre status (disponível/indisponível), passa e não pede o "value"

                else:
                    value = input("\nDeclare o valor que queira buscar: ")

                    if value.strip() == "":
                        print("\nO valor não pode ser vazio!")
                        continue

                buscar_livro(value,mode) # Chama a função de buscar livro
                input("\n(Pressione 'Enter' para continuar)\n")
                break

        case 6: # Listagem ordenada de livros
            while True:
                try:
                    mode = int(input("\nQual ordem de listagem deseja?" \
                    "\n[0] ---> Ordem por título" \
                    "\n[1] ---> Ordem por autoria" \
                    "\n[2] ---> Ordem por ano" \
                    "\n --> "))
                    # Menu de opções sobre a ordem de listagem do catálogo
                except ValueError:
                    print("Valor inválido! Tente novamente.\n")
                    continue

                if mode not in [0,1,2]: # Se não for nenhuma das opções pedidas
                    print(f"'{mode}' inválido! Tente novamente.\n")
                    continue

                ordenar_listagem(mode) # Chama a função de listagem por ordem
                input("\n(Pressione 'Enter' para continuar)\n")
                break

        case 7: # Descadastro/remoção de livro do catálogo
            while True:
                titulo = input("\n- Insira o título do livro que deseja descadastrar: ")
                if titulo.strip() == "":
                    print("\nO título não pode ser vazio!")
                    continue

                print(descadastrar_livro(titulo)) # Chama a função de descadastro de livro
                input("\n(Pressione 'Enter' para continuar)\n")
                break

        case 8 | 9: # Alteração de estoque em algum livro
            if choice == 8: # Configura o modo para o uso da função
                mode = "Aumentar"
            else:
                mode = "Reduzir"

            while True:
                titulo = input("\n- Insira o título do livro que deseja alterar estoque: ")
                if titulo.strip() == "":
                    print("O título não pode ser vazio!\n")
                    continue

                try:
                    value = int(input("\n- Insira a quantidade que deseja alterar no estoque: "))
                except ValueError:
                    print("O valor inserido para a quantidade foi inválido!\n")

                print(estoque_livro(titulo,mode,value)) # Chama a função para alterar o estoque
                input("\n(Pressione 'Enter' para continuar)\n")
                break

        case 0: # Encerra o sistema com break, finalizando o loop e encerrando o programa
            print("\n- SISTEMA ENCERRADO -")
            break

        case _: # Se não for nenhuma das opções, retorna mensagem de erro e continua o loop de novo
            print("Opção inválida! Tente novamente.\n")


'''
NOTAS:

Os 'input("Pressione 'Enter' para continuar")' foram adicionados por mim a fim de deixar o código mais confortável pra ler com um ritmo mais lento
--> Por quê muitas vezes o menu/resposta aparecia logo depois e ocupava muito a tela antes de poder ler o que o código respondeu

Sobre o checar_titulo: Embora concordo que deve haver livros com títulos semelhantes, possibilitar tal ocorrência causaria erros e maior tempo para resolvê-los no código,
justamente devido ao caminho que escolhi de usar a quantidade de livros emprestados e disponíveis ao invés de cadastrar livro por livro no .CSV
Portanto precisava de alguma informação dos livros que seja única para encontrá-la e usá-la a fim de obter precisão e deixar o programa estável e claro

'''