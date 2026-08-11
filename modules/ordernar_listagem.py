import csv

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
            print (f"\n{counter}. '{line[0]}' por {line[1]} em {line[2]} \nISBN: {line[3]} | Disponíveis: {line[4]} | Emprestados: {line[5]}")
            counter += 1
            # Com a lista já organizada em ordem, lista os livros