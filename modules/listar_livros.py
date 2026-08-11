import csv

def listar_livros(): # Faz uma lista organizada de todos os livros atuais no .CSV
    with open("livros.csv", "r") as file:
        reader = csv.DictReader(file)
        counter = 1 # Variável usada para contagem estética de cada livro "1. Livro X | 2. Livro Y ..."

        for line in reader:
            print(f"\n{counter}. '{line["titulo"]}' por {line["autor"]} em {line["ano"]} \nISBN: {line["isbn"]} | Disponíveis: {line["disponivel"]} | Emprestados: {line["emprestado"]}")
            # Mostra as informações do livro usando o dicionário lido do .CSV para cada livro
            counter += 1

        if counter == 1:
            return print("\nNão há livros cadastrados.")
        else:
            return print(f"\n{counter-1} livro(s) sendo mostrado(s).")
        # Verifica se houve livros mostrados: retorna quantos livros foram ou se nenhum foi mostrado