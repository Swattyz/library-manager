import os
import csv # Importa funções do .CSV para dentro do código
os.system("cls") # Limpa o conteúdo atual do terminal

estrutura = ['titulo', 'autor', 'ano', 'isbn', 'disponivel'] # Estrutura-base da headline do arquivo .CSV para catálogo de livros

# FUNÇÕES DO CÓDIGO (são chamadas e usadas durante o funcionamento)

def cadastrar_livro(titulo,autor,ano, isbn): # Cadastra um novo livro no catálogo dentro do arquivo .CSV
    with open('livros.csv','a',newline='') as f:
            produto = {'titulo':titulo, 'autor':autor, 'ano':ano, 'isbn':isbn, 'disponivel':"Disponivel"}
            # Cria um dicionário com as informações do futuro livro

            writer = csv.DictWriter(f,fieldnames=estrutura) # Lê o .CSV como um dicionário
            writer.writerow(produto)
            # Escreve/adiciona "produto" (o novo livro a ser cadastrado) dentro do .CSV após todas as linhas usando o modo "append" do open()

    return "\nLivro cadastrado!"

def checar_isbn(isbn): # Função que checa se o ISBN já existe ou não
    with open('livros.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        x = False

        for line in reader: # Para cada linha (lista de cada livro)
            if line[3] == str(isbn): # Se o ISBN (posição 3 da lista) for igual ao ISBN
                x = True # Coloca X pra Falso e retorna ele depois

        return x

def emprestimo_devolucao(isbn, mode): # Função flexível que registra empréstimo e devolução de livros no catálogo
    lines = []
    was_found = False # Identificador para checagem se foi de fato encontrado um livro ou não

    with open("livros.csv", "r", newline='') as file:
        reader = csv.reader(file) # Lê como lista
        for items in reader: # Para cada livro (uma lista que contém informações do livro) dentro do .CSV
            if items[3] == isbn: # Se a posição 3 da lista (que equivale ao ISBN do livro) for igual ao ISBN pedido
                was_found = True

                if mode == "Emprestimo": 
                    if items[4] == "Disponivel":
                        items[4] = "Indisponivel"
                        # Se foi pedido empréstimo e se tal livro estiver disponível, troca o valor da posição 4 da lista do livro (que equivale ao status) para indisponível
                    else:
                        return f"\nO livro '{items[0]}' não está disponível!"
                    
                else:
                    if items[4] == "Indisponivel":
                        items[4] = "Disponivel"
                        # Faz o contrário, caso for pedido devolução, troca de indisponível para disponível
                    else:
                        return f"\nO livro '{items[0]}' já está disponível!"
                    
            lines.append(items) # Adiciona o livro após toda a checagem na lista vazia após cada linha lida pelo for loop

    with open("livros.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
        # Usa o modo write para apagar todo o conteúdo do CSV e reescreve o conteúdo novo com os valores já atualizados usando a lista preenchida pelo for loop

    if was_found and mode == "Emprestimo":
        return "\nLivro emprestado com sucesso."
    elif was_found and mode == "Devolucao":
        return "\nLivro devolvido com sucesso."
    else:
        return "\nNenhum livro encontrado!"
    # Essa parte apenas verifica usando o identificador "was_found" se o livro foi de fato encontrado e retorna resposta

def listar_livros(): # Faz uma lista organizada de todos os livros atuais no .CSV
    with open("livros.csv", "r") as file:
        reader = csv.DictReader(file)
        counter = 1 # Variável usada para contagem estética de cada livro "1. Livro X | 2. Livro Y ..."

        for line in reader:
            print(f"\n{counter}. '{line["titulo"]}' por {line["autor"]} em {line["ano"]} \nISBN: {line["isbn"]} | Status: {line["disponivel"]}")
            # Mostra as informações do livro usando o dicionário lido do .CSV para cada livro
            counter += 1

        if counter == 1:
            return print("\nNão há livros cadastrados.")
        else:
            return print(f"\n{counter-1} livro(s) sendo mostrado(s).")
        # Verifica se houve livros mostrados: retorna quantos livros foram ou se nenhum foi mostrado

def buscar_livro(value,mode): # Busca livros com base em alguma característica específica
    with open("livros.csv", "r") as file:
        counter = 1
        reader = csv.reader(file)
        next(reader) # Pula a primeira linha (ignorando a headline do .CSV)

        if mode in [0,1]: # Caso a busca esteja sendo por autoria ou título
            words = value.lower().split() # Cria uma lista com todas as palavras que foram buscadas

            for line in reader: # Para cada livro(lista) dentro do .CSV
                book = line[mode].lower().split() # Cria uma lista que contém todas as palavras do título de cada livro (altera todo loop)
                found = True

                for word in words: # Para cada palavra na lista de palavras que foram buscadas
                    if word not in book: # Verifica se cada uma das palavras está ou não entre as palavras do título do livro
                        found = False # Se qualquer palavra buscada não for encontrada no livro atual, retorna falso e acaba o loop imediatamente
                        break

                if found: # Se o livro for encontrado, mostra o livro
                        print (f"\n{counter}. '{line[0]}' por {line[1]} em {line[2]} \nISBN: {line[3]} | Status: {line[4]}")
                        counter += 1
        else:
            for line in reader:
                if line[mode] == value:
                    print (f"\n{counter}. '{line[0]}' por {line[1]} em {line[2]} \nISBN: {line[3]} | Status: {line[4]}")
                    counter += 1
        # Para cada livro dentro do .CSV em formato de lista: se o valor da característica do livro escolhida for igual ao que foi pedido na busca, o livro é mostrado

        if counter == 1:
            return print("\nLivro não encontrado.")
        else:
            return print(f"\n{counter-1} livro(s) encontrado(s).")
        # Verificação padrão se houve livros encontrados ou não.

def ordenar_listagem(mode): # Ordena uma listagem com base em alguma característica em ORDEM ALFABÉTICA
    with open("livros.csv", "r") as file:
        counter = 1
        reader = csv.reader(file)
        next(reader) # Ignora a primeira linha (headline)
        livros = list(reader) # Transforma em lista

        if mode == 2: # Caso o modo de busca for por ano (valores inteiros), organiza porém com valores inteiros invés de string
            livros.sort(key=lambda livros: int(livros[mode]))
        else:
            livros.sort(key=lambda livros: livros[mode])
        # Usa .sort() para organizar a lista em ordem alfabética pelo próprio Python
        # Usa key=lambda para pedir para o .sort() usar a ordem alfabética em apenas um item específico da lista ("mode")
        # invés de usar a ordem em todos os itens da lista com um .sort() comum
        # É organizada com base na característica que foi pedida ("mode")

        for line in livros:
            print (f"\n{counter}. '{line[0]}' por {line[1]} em {line[2]} \nISBN: {line[3]} | Status: {line[4]}")
            counter += 1
            # Com a lista já organizada em ordem, lista os livros

def descadastrar_livro(isbn): # Descadastra/remove um livro do catálogo do .CSV
    lines = []
    was_found = 0

    with open("livros.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for items in reader:
            if items[3] != str(isbn):
                lines.append(items)
            else:
                was_found = 1
        # Para todo livro que não for o ISBN pedido, é colocado dentro da lista

    with open("livros.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    # Como a lista contém todos os livros exceto o livro com o ISBN requisitado, a mesma lista é escrita no .CSV novamente usando o modo "write"

    if was_found == 0:
        return f"\nNão há livros encontrados com o ISBN '{isbn}'!"
    else:
        return f"\nLivro cujo ISBN é '{isbn}' foi removido do catálogo."
    # Verifica e retorna se houve livros encontrados ou não

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
        "\n[8] --- SAIR" \
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
                    isbn = int(input("- ISBN do livro: "))

                    if len(str(isbn)) > 13: # Verifica se o ISBN não é grande demais
                        print("Esse ISBN é muito grande!\n")
                        continue

                    elif checar_isbn(isbn): # Checa se o ISBN já existe ou não
                        print("Esse ISBN já existe!\n")
                        continue

                    break

                except ValueError:
                    print("Valor inválido!\n")

            print(cadastrar_livro(titulo,autor,ano, isbn)) # Chama a função de cadastro de livros
            input("\n(Pressione 'Enter' para continuar)\n")

        case 2 | 3: # Empréstimo e devolução de livro
            while True:
                if choice == 2:
                    mode = "Emprestimo"
                else:
                    mode = "Devolucao"
                # Checagem e declaração do modo pedido
                
                try:
                    isbn = int(input("\n- Insira o ISBN do livro: "))
                except ValueError:
                    print(f"Não é um ISBN com formato válido!\n")
                    continue

                print(emprestimo_devolucao(str(isbn), mode)) # Chama a função de empréstimo e devolução de livros
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
                    if mode == 4:
                        value = "Disponivel"

                    elif mode == 5:
                        mode = 4
                        value = "Indisponivel"
                    # Se a busca for sobre status (disponível/indisponível), já declara valor da característica (pois não existiria outras opções além dos dois)

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
                    try:
                        isbn = int(input("\n- Insira o ISBN do livro: "))
                    except ValueError:
                        print(f"Não é um ISBN com formato válido!\n")
                        continue

                    print(descadastrar_livro(isbn)) # Chama a função de descadastro de livro
                    input("\n(Pressione 'Enter' para continuar)\n")
                    break

        case 8: # Encerra o sistema com break, finalizando o loop e encerrando o programa
            print("\n- SISTEMA ENCERRADO -")
            break

        case _: # Se não for nenhuma das opções, retorna mensagem de erro e continua o loop de novo
            print("Opção inválida! Tente novamente.\n")


'''
Os input "Pressione 'Enter' para continuar" foram adicionados por mim a fim de deixar o código mais confortável pra ler com um ritmo mais lento
--> Por quê muitas vezes o menu/resposta aparecia logo depois e ocupava muito a tela antes de poder ler o que o código respondeu
'''