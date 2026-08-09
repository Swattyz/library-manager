import os
import csv
os.system("cls")

estrutura = ['titulo', 'autor', 'ano', 'isbn', 'disponivel']

# FUNÇÕES

def gerar_isbn():
    with open("livros.csv", "r") as file:
        livros = csv.DictReader(file) # Lê em formato de dicionário (desconsidera a headline dentro do .CSV)
        maior = 0

        if not livros: # Se a lista (conteúdo dentro do .CSV) estiver vazia (não tem livros cadastrados)

            '''Sobre o ISBN (tentei me basear no sistema do código ISBN real):
            978 --> padrão de início de 3 dígitos para livros
            65 --> código que indica a região do livro (nesse caso, Brasil)
            998765 --> código-exemplo que indica editoras pequenas 
            00 --> código que indica qual livro é (o primeiro livro é 00, o segundo registrado será 01, etc.)'''
            
            return 9786599876500 # Retorna o pádrão inicial

        else: # Caso tenha livros no .CSV
            for livro in livros:
                if int(livro["isbn"]) > maior:
                    maior = int(livro["isbn"])
            # Verifica o maior ISBN entre todos os livros dentro do .CSV

            return (maior) + 1 # Retorna o maior ISBN no .CSV, adicionando +1 para ser utilizado no cadastro de um livro

def cadastrar_livro(titulo,autor,ano):
    isbn = gerar_isbn() # Usa a função para gerar um ISBN novo que não exista

    with open('livros.csv','a',newline='') as f:
            produto = {'titulo':titulo, 'autor':autor, 'ano':ano, 'isbn':isbn, 'disponivel':"Disponivel"}
            writer = csv.DictWriter(f,fieldnames=estrutura)
            writer.writerow(produto)

    return "\nLivro cadastrado!"

def emprestimo_devolucao(isbn, mode):
    lines = []
    was_found = 0

    with open("livros.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for items in reader:
            if items[3] == isbn:
                was_found = 1

                if mode == "Emprestimo":
                    if items[4] == "Disponivel":
                        items[4] = "Indisponivel"
                    else:
                        return f"\nO livro '{items[1]}' não está disponível!"
                    
                else:
                    if items[4] == "Indisponivel":
                        items[4] = "Disponivel"
                    else:
                        return f"\nO livro '{items[1]}' já está disponível!"
                    
            lines.append(items)

    with open("livros.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

    if was_found == 1 and mode == "Emprestimo":
        return "\nLivro emprestado com sucesso."
    elif was_found == 1 and mode == "Devolucao":
        return "\nLivro devolvido com sucesso."
    else:
        return "\nNenhum livro encontrado!"

def listar_livros():
    with open("livros.csv", "r") as file:
        reader = csv.DictReader(file)
        counter = 1

        for line in reader:
            print(f"\n{counter}. '{line["titulo"]}' por {line["autor"]} em {line["ano"]} \nISBN: {line["isbn"]} | Status: {line["disponivel"]}")
            counter += 1

        if counter == 1:
            return print("\nNão há livros cadastrados.")
        else:
            return(f"\n{counter-1} livro(s) sendo mostrado(s).")

def buscar_livro(value,mode):
    with open("livros.csv", "r") as file:
        counter = 1
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            if str(line[mode]) == value:
                print (f"\n{counter}. '{line[0]}' por {line[1]} em {line[2]} \nISBN: {line[3]} | Status: {line[4]}")
                counter += 1

        if counter == 1:
            return print("\nLivro não encontrado.")
        else:
            return(f"\n{counter-1} livro(s) encontrado(s).")

def ordenar_listagem(mode):
    with open("livros.csv", "r") as file:
        counter = 1
        reader = csv.reader(file)
        next(reader)
        livros = list(reader)

        if mode == 2:
            livros.sort(key=lambda livros: int(livros[mode]))
        else:
            livros.sort(key=lambda livros: livros[mode])

        for line in livros:
            print (f"\n{counter}. '{line[0]}' por {line[1]} em {line[2]} \nISBN: {line[3]} | Status: {line[4]}")
            counter += 1

def descadastrar_livro(isbn):
    lines = []
    was_found = 0

    with open("livros.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for items in reader:
            if items[3] != str(isbn):
                lines.append(items)
            else:
                was_found = 1

    with open("livros.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

    if was_found == 0:
        return f"\nNão há livros encontrados com o ISBN '{isbn}'!"
    else:
        return f"\nLivro cujo ISBN é '{isbn}' foi removido do catálogo."

# CÓDIGO PRINCIPAL

print ("==== SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ====" \
"\nBem vindo ao gerenciador de livros da biblioteca, o que deseja fazer?")

while True:
    try:
        choice = int(input("\n[1] --- CADASTRAR LIVRO" \
        "\n[2] --- REGISTRAR EMPRÉSTIMO" \
        "\n[3] --- REGISTRAR DEVOLUÇÃO" \
        "\n[4] --- LISTAR LIVROS" \
        "\n[5] --- BUSCA DE LIVRO" \
        "\n[6] --- ORDENAR LISTAGEM" \
        "\n[7] --- DESCADASTRAR LIVRO" \
        "\n[8] --- SAIR" \
        "\n--> "))
    except:
        print("Opção inválida!\n")
        continue

    match choice:
        case 1:
            while True:
                titulo = input("\n- Título do livro: ")

                if titulo.strip() == "":
                    print("\nO título não pode ser vazio!")
                    continue

                autor = input("- Autor do livro: ")

                if autor.strip() == "":
                    print("\nO nome do autor não pode ser vazio!")
                    continue

                try: 
                    ano = int(input("- Ano do livro: "))
                    if ano > 2026 or ano < 0:
                        print("Valor do ano muito alto ou muito baixo! Tente novamente.\n")
                        continue
                    break

                except:
                    print("\nValor inválido!")
                    continue
            print(cadastrar_livro(titulo,autor,ano))
            input("\n(Pressione 'Enter' para continuar)\n")

        case 2 | 3:
            while True:
                if choice == 2:
                    mode = "Emprestimo"
                else:
                    mode = "Devolucao"
                
                try:
                    isbn = int(input("\n- Insira o ISBN do livro: "))
                except:
                    print(f"Não é um ISBN com formato válido!\n")
                    continue

                if len(str(isbn)) != 13:
                    print("ISBN inválido!\n")
                    continue

                print(emprestimo_devolucao(str(isbn), mode))
                input("\n(Pressione 'Enter' para continuar)\n")
                break

        case 4:
            listar_livros()
            input("\n(Pressione 'Enter' para continuar)\n")

        case 5:
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
                except:
                    print(f"O valor dado não é válido!\n")
                    continue

                if mode not in [0,1,2,3,4,5]:
                    print(f"'{mode}' inválido! Tente novamente.\n")
                    continue

                elif mode in [4,5]:
                    if mode == 4:
                        value = "Disponivel"

                    elif mode == 5:
                        mode = 4
                        value = "Indisponivel"

                else:
                    value = input("\nDeclare o valor que queira buscar: ")

                    if value.strip() == "":
                        print("\nO valor não pode ser vazio!")
                        continue

                buscar_livro(value,mode)
                input("\n(Pressione 'Enter' para continuar)\n")
                break

        case 6:
            while True:
                try:
                    mode = int(input("\nQual ordem de listagem deseja?" \
                    "\n[0] ---> Ordem por título" \
                    "\n[1] ---> Ordem por autoria" \
                    "\n[2] ---> Ordem por ano" \
                    "\n --> "))
                except:
                    print("Valor inválido! Tente novamente.\n")
                    continue

                if mode not in [0,1,2]:
                    print(f"'{mode}' inválido! Tente novamente.\n")
                    continue

                ordenar_listagem(mode)
                input("\n(Pressione 'Enter' para continuar)\n")
                break

        case 7:
                while True:
                    try:
                        isbn = int(input("\n- Insira o ISBN do livro: "))
                    except:
                        print(f"Não é um ISBN com formato válido!\n")
                        continue

                    if len(str(isbn)) != 13:
                        print("ISBN inválido!\n")
                        continue

                    print(descadastrar_livro(isbn))
                    input("\n(Pressione 'Enter' para continuar)\n")
                    break

        case 8:
            print("\n- SISTEMA ENCERRADO -")
            break

        case _:
            print("Opção inválida! Tente novamente.\n")


'''
Os input "Pressione 'Enter' para continuar" foram adicionados por mim a fim de deixar o código mais confortável pra ler com um ritmo mais lento
--> Por quê muitas vezes o menu/resposta aparecia logo depois e ocupava muito a tela antes de poder ler o que o código respondeu
'''