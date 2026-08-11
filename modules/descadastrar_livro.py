import csv

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