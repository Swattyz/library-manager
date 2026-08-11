import csv

def estoque_livro(titulo,mode,value): # Função para alterar o estoque do livro
    with open('livros.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        lines = []
        was_found = False

        for line in reader: # Para cada livro, se achar o livro com o título requerido, troca o valor da posição 4 (livros disponíveis) conforme o modo
            if line[0] == titulo:
                was_found = True
                if mode == "Aumentar":
                    line[4] = int(line[4]) + value # Se for aumentar o estoque, aumenta o valor dos livros disponíveis
                else:
                    if int(line[4])-value > 0: # Se for redução de estoque, verifica se tem menos livros no estoque que os livros que serão removidos do estoque
                        line[4] = int(line[4]) - value # Reduz os livros disponíveis
                    else:
                        return f"\nO livro '{line[0]}' possui apenas {line[4]} em estoque! Não foi possível reduzir {value} cópias dele."
            lines.append(line)

    with open('livros.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
        # Reescreve o .CSV com as linhas atualizadas

    if was_found:
        return f"\nO livro '{line[0]}' passou a ter {line[4]} cópias em estoque!"
    else:
        return f"\nO livro '{titulo}' não foi encontrado!"
    # Retorna resposta e validação do processo da função conforme é verificado se de fato foi encontrado um livro com tal título