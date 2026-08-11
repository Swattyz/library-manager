import csv

def cadastrar_livro(titulo,autor,ano, isbn): # Cadastra um novo livro no catálogo dentro do arquivo .CSV
        estrutura = ['titulo', 'autor', 'ano', 'isbn', 'disponivel', 'emprestado'] # Estrutura-base da headline do arquivo .CSV para catálogo de livros

        with open('livros.csv','a',newline='') as f:
                produto = {'titulo':titulo, 'autor':autor, 'ano':ano, 'isbn':isbn, 'disponivel':0, 'emprestado':0}
                # Cria um dicionário com as informações do futuro livro

        writer = csv.DictWriter(f,fieldnames=estrutura) # Lê o .CSV como um dicionário
        writer.writerow(produto)
        # Escreve/adiciona "produto" (o novo livro a ser cadastrado) dentro do .CSV após todas as linhas usando o modo "append" do open()

        return "\nLivro cadastrado!"