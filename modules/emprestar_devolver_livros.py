import csv

def emprestimo_devolucao(titulo, mode): # Função flexível que registra empréstimo e devolução de livros no catálogo
    lines = []
    was_found = False # Identificador para checagem se foi de fato encontrado um livro ou não

    with open("livros.csv", "r", newline='') as file:
        reader = csv.reader(file) # Lê como lista
        for items in reader: # Para cada livro (uma lista que contém informações do livro) dentro do .CSV
            if items[0] == titulo: # Se a posição 0 da lista (que equivale ao título do livro) for igual ao título pedido
                was_found = True

                if mode == "Emprestimo": 
                    if int(items[4]) > 0:
                        items[4] = int(items[4]) - 1
                        items[5] = int(items[5]) + 1
                        # Se foi pedido empréstimo e se tal livro estiver disponível, troca o valor da posição 4 da lista do livro (que equivale aos disponíveis) e reduz 1
                    else:
                        return f"\nNão há '{items[0]}' disponíveis!"
                    
                else:
                    if int(items[5]) > 0:
                        items[5] = int(items[5]) - 1
                        items[4] = int(items[4]) + 1
                        # Faz o contrário, caso for pedido devolução, reduz 1 nos livros emprestados
                    else:
                        return f"\nNão há '{items[0]}' emprestados para devolver!"
                    
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