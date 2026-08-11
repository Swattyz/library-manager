import csv

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
                        print (f"\n{counter}. '{line[0]}' por {line[1]} em {line[2]} \nISBN: {line[3]} | Disponíveis: {line[4]} | Emprestados: {line[5]}")
                        counter += 1

        elif mode in [4,5]:
            for line in reader:
                if int(line[mode]) > 0:
                    print (f"\n{counter}. '{line[0]}' por {line[1]} em {line[2]} \nISBN: {line[3]} | Disponíveis: {line[4]} | Emprestados: {line[5]}")
                    counter += 1
        # Se for buscar por livros disponíveis ou indisponíveis, vê se há esses livros, e então os mostra

        else:
            for line in reader:
                if line[mode] == value:
                    print (f"\n{counter}. '{line[0]}' por {line[1]} em {line[2]} \nISBN: {line[3]} | Disponíveis: {line[4]} | Emprestados: {line[5]}")
                    counter += 1
        # Para cada livro dentro do .CSV em formato de lista: se o valor da característica do livro escolhida for igual ao que foi pedido na busca, o livro é mostrado

        if counter == 1:
            return print("\nLivro não encontrado.")
        else:
            return print(f"\n{counter-1} livro(s) encontrado(s).")
        # Verificação padrão se houve livros encontrados ou não.