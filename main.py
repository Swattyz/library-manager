import os
import csv
os.system("cls")

estrutura = ['titulo', 'autor', 'ano', 'codigo', 'status']

def cadastrar_livro(titulo,autor,ano,codigo,status):
    with open('library-manager/sheet.csv','a',newline='') as f:
            produto = {'titulo':titulo, 'autor':autor, 'ano':ano, 'codigo':codigo, 'status':status}
            writer = csv.DictWriter(f,fieldnames=estrutura)
            writer.writerow(produto)

print ("==== SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ====")
while True:
    choice = int(input("\nBem vindo ao gerenciamento de livros da biblioteca, o que deseja fazer?" \
    "\n[1] --- CADASTRAR LIVRO" \
    "\n[2] --- REGISTRAR EMPRÉSTIMO" \
    "\n[3] --- REGISTRAR DEVOLUÇÃO" \
    "\n[4] --- LISTAR LIVROS" \
    "\n[5] --- BUSCA DE LIVRO" \
    "\n[6] --- ORDENAR LISTAGEM"))

    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass