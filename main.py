import os
import csv
os.system("cls")

estrutura = ['titulo', 'autor', 'ano', 'isbn', 'disponivel']

def cadastrar_livro(titulo,autor,ano):
    book_qty = int(0)
    
    with open('library-manager/sheet.csv', 'r') as file:
        for line in file:
            book_qty += 1
            isbn = int(9786599876500) + (book_qty-1)

    '''Sobre o ISBN (tentei me basear no sistema do código ISBN real):
    978 --> padrão de início de 3 dígitos para livros
    65 --> código que indica a região do livro (nesse caso, Brasil)
    998765 --> código-exemplo que indica editoras pequenas 
    00 --> código que indica qual livro é (o primeiro livro é 00, o segundo registrado será 01, etc.)'''

    with open('library-manager/sheet.csv','a',newline='') as f:
            produto = {'titulo':titulo, 'autor':autor, 'ano':ano, 'isbn':isbn, 'disponivel':"Disponivel"}
            writer = csv.DictWriter(f,fieldnames=estrutura)
            writer.writerow(produto)

    return "\nLivro cadastrado!"

def registrar_emprestimo(isbn):
    lines = []
    found = int(0)

    with open("library-manager/sheet.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for items in reader:
            if items[3] == isbn:
                found = int(1)
                if items[4] == "Disponivel":
                    items[4] = "Indisponivel"
                else:
                    return "\nEsse livro não está disponível!"
            lines.append(items)

    with open("library-manager/sheet.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

    if found == 1:
        return "\nLivro emprestado com sucesso."
    else:
        return "\nNenhum livro encontrado!"

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
        "\n[7] --- SAIR" \
        "\n--> "))
    except:
        print("Opção inválida!\n")
        continue

    match choice:
        case 1:
            titulo = input("\nTítulo do livro: ")
            autor = input("Autor do livro: ")

            while True:
                try: 
                    ano = int(input("Ano do livro: "))
                    if ano > 2026 or ano < 0:
                        print("Valor do ano muito alto ou muito baixo! Tente novamente.\n")
                        continue
                    break
                except:
                    print("Valor inválido!\n")
                    continue
            print(cadastrar_livro(titulo,autor,ano))

        case 2:
            while True:
                try:
                    isbn = int(input("Insira o ISBN do livro: "))
                except:
                    print("Não é um ISBN com formato válido!\n")
                    continue

                if len(str(isbn)) != 13:
                    print("ISBN inválido!\n")
                    continue
                break
            print(registrar_emprestimo(str(isbn)))
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            break
        case _:
            print("Opção inválida! Tente novamente.\n")