# Classe que representa um livro na biblioteca.
class Livro:
    # Inicializa um novo livro com título, autor, ano, código e status.
    def __init__(self, titulo, autor, ano, codigo, status):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.codigo = codigo
        self.status = status

# Cadastrar livro
def cadastrar_livro(biblioteca):
    print("\n--- CADASTRAR LIVRO ---")
    codigo = input("Código (ID único): ")
   
    # Verifica se o código já existe
    ja_existe = 0
    for livro in biblioteca:
        if livro.codigo == codigo:
            ja_existe = 1
            break
           
    if ja_existe == 1:
        print("Erro: Já existe um livro com este código.")
    else:
        # Solicita os dados do novo livro e o adiciona à biblioteca
        titulo = input("Título: ")
        autor = input("Autor (apenas o primeiro nome): ")
        ano = input("Ano de publicação: ")
        novo_livro = Livro(titulo, autor, ano, codigo, "disponível")
        biblioteca.append(novo_livro)
        print("Livro cadastrado com sucesso!")

# Consultar livro
def consultar_livro(biblioteca):
    print("\n--- CONSULTAR LIVRO ---")
    print("1. Por código")
    print("2. Por autor")
    opcao = input("Opção: ")
   
    encontrado = 0
    if opcao == "1":
        cod_busca = input("Digite o código: ")
        for livro in biblioteca:
            if livro.codigo == cod_busca:
                print(f"Livro encontrado: {livro.titulo} - {livro.autor} ({livro.status})")
                encontrado = 1
                break
    elif opcao == "2":
        aut_busca = input("Digite o autor: ")
        for livro in biblioteca:
            if livro.autor == aut_busca:
                print(f"Obra: {livro.titulo} | Código: {livro.codigo} | Status: {livro.status}")
                encontrado = 1
    else:
        print("Opção inválida.")
        return

    if encontrado == 0:
        print("Livro não encontrado")

# Alterar dados
def alterar_dados(biblioteca):
    print("\n--- ALTERAR DADOS ---")
    codigo = input("Digite o código do livro: ")
    achou = 0
    # Busca o livro pelo código e atualiza seus dados
    for livro in biblioteca:
        if livro.codigo == codigo:
            livro.titulo = input(f"Novo Título (atual: {livro.titulo}): ")
            livro.autor = input(f"Novo Autor (atual: {livro.autor}): ")
            livro.ano = input(f"Novo Ano (atual: {livro.ano}): ")
            print("Dados alterados com sucesso!")
            achou = 1
            break
   
    if achou == 0:
        print("Livro não encontrado")

# Remover livro
def remover_livro(biblioteca):
    print("\n--- REMOVER LIVRO ---")
    codigo = input("Digite o código para remover: ")
    posicao = -1
    for i in range(len(biblioteca)):
        if biblioteca[i].codigo == codigo:
            posicao = i
            break
           
    if posicao != -1:
        biblioteca.pop(posicao)
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado")

# Listar todos
def listar_todos(biblioteca):
    print("\n--- LISTAR TODOS OS LIVROS (ORDEM ALFABÉTICA) ---")
    
    if len(biblioteca) == 0:
        print("A biblioteca está vazia.")
        return

    temp_lista = []
    for item in biblioteca:
        temp_lista.append(item)

    # Implementação do Bubble Sort para ordenar por título
    n = len(temp_lista)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if temp_lista[j].titulo > temp_lista[j+1].titulo:
                auxiliar = temp_lista[j]
                temp_lista[j] = temp_lista[j+1]
                temp_lista[j+1] = auxiliar
            j = j + 1
        i = i + 1

    for livro in temp_lista:
        print(f"Título: {livro.titulo} - Ano: {livro.ano}")

# Realizar empréstimo
def realizar_emprestimo(biblioteca):
    print("\n--- REALIZAR EMPRÉSTIMO ---")
    codigo = input("Código do livro: ")
    achou = 0
    # Busca o livro pelo código e tenta realizar o empréstimo
    for livro in biblioteca:
        if livro.codigo == codigo:
            achou = 1
            if livro.status == "disponível":
                livro.status = "emprestado"
                print("Empréstimo realizado!")
            else:
                print("Livro já emprestado")
            break
   
    if achou == 0:
        print("Livro não encontrado")

# Realizar devolução
def realizar_devolucao(biblioteca):
    print("\n--- REALIZAR DEVOLUÇÃO ---")
    codigo = input("Código do livro: ")
    achou = 0
    # Busca o livro pelo código e tenta realizar a devolução
    for livro in biblioteca:
        if livro.codigo == codigo:
            achou = 1
            if livro.status == "emprestado":
                livro.status = "disponível"
                print("Devolução realizada!")
            else:
                print("Livro não estava emprestado ou não está disponível.")
            break
   
    if achou == 0:
        print("Livro não encontrado")

# Menu
def menu_principal():
    acervo = []  # Lista para armazenar os livros
    rodando = 1  # Controle do loop do menu
   
    while rodando == 1:
        print("\n=== SISTEMA DE CONTROLE DE BIBLIOTECA ===")
        print("1. Cadastrar livro")
        print("2. Consultar livro")
        print("3. Alterar dados")
        print("4. Remover livro")
        print("5. Listar todos")
        print("6. Realizar empréstimo")
        print("7. Realizar devolução")
        print("8. Sair")
       
        escolha = input("Selecione uma opção: ")
       
        # Chama a função correspondente à escolha do usuário
        if escolha == "1":
            cadastrar_livro(acervo)
        else:
            if escolha == "2":
                consultar_livro(acervo)
            else:
                if escolha == "3":
                    alterar_dados(acervo)
                else:
                    if escolha == "4":
                        remover_livro(acervo)
                    else:
                        if escolha == "5":
                            listar_todos(acervo)
                        else:
                            if escolha == "6":
                                realizar_emprestimo(acervo)
                            else:
                                if escolha == "7":
                                    realizar_devolucao(acervo)
                                else:
                                    if escolha == "8":
                                        print("Finalizando programa...")
                                        rodando = 0
                                    else:
                                        print("Opção inválida!")

# Bloco principal de execução do script.
if __name__ == "__main__":
    menu_principal()
