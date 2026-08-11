import csv

def checar_titulo(titulo): # Função que checa se o título que deseja adicionar já existe de forma igual
    found = False

    with open("livros.csv", "r", newline='') as file:
        reader = csv.reader(file)
        next(reader) # Pula headline
        for line in reader: # Para cada linha/lista/livro no .CSV, checa se a posição 0 (título) é o mesmo que o título
            if line[0] == titulo:
                found = True # Retorna falso se de fato encontrou um título igual
                break

        return found