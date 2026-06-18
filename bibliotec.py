def cadastrar_livro(biblioteca):
    print("\n--- CADASTRO DE NOVO LIVRO ---")

    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor (primeiro nome): ")
    ano = input("Digite o ano de publicação: ")
    codigo = input("Digite o código único: ")

    ja_existe = False
    for i in range(len(biblioteca)):
        if biblioteca[i][3] == codigo:
            ja_existe = True

    if ja_existe == True:
        print("Erro: Já existe um livro com este código. Cadastro cancelado.")
    else:
        novo_livro = [titulo, autor, ano, codigo, "Disponível"]
        biblioteca.append(novo_livro)
        print("Livro cadastrado com sucesso!")


def listar_livros(biblioteca):
    print("\n--- LISTA DE TODOS OS LIVROS ---")

    quantidade = 0
    for livro in biblioteca:
        quantidade = quantidade + 1

    if quantidade == 0:
        print("A biblioteca está vazia no momento.")
        return

    for i in range(quantidade):
        for j in range(0, quantidade - i - 1):
            if biblioteca[j][0] > biblioteca[j + 1][0]:
                auxiliar = biblioteca[j]
                biblioteca[j] = biblioteca[j + 1]
                biblioteca[j + 1] = auxiliar

    for i in range(quantidade):
        print("Título:", biblioteca[i][0], "| Ano:", biblioteca[i][2])


def consultar_livro(biblioteca):
    print("\n--- CONSULTA DE LIVRO ---")
    print("1. Consultar por Código")
    print("2. Consultar por Autor")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        busca_cod = input("Digite o código: ")
        encontrado = False
        for i in range(len(biblioteca)):
            if biblioteca[i][3] == busca_cod:
                print("\nLivro Encontrado:")
                print("Título:", biblioteca[i][0])
                print("Autor:", biblioteca[i][1])
                print("Ano:", biblioteca[i][2])
                print("Status:", biblioteca[i][4])
                encontrado = True
        if encontrado == False:
            print("Livro não encontrado.")

    elif opcao == "2":
        busca_aut = input("Digite o nome do autor: ")
        encontrado_autor = False
        for i in range(len(biblioteca)):
            if biblioteca[i][1] == busca_aut:
                print("\nLivro do Autor:")
                print("Título:", biblioteca[i][0], "| Código:", biblioteca[i][3])
                encontrado_autor = True
        if encontrado_autor == False:
            print("Nenhum livro encontrado para este autor.")


def alterar_dados(biblioteca):
    print("\n--- ALTERAR DADOS ---")
    cod_alterar = input("Digite o código do livro: ")

    encontrou = False
    for i in range(len(biblioteca)):
        if biblioteca[i][3] == cod_alterar:
            print("Livro encontrado! Digite os novos dados:")
            biblioteca[i][0] = input("Novo Título: ")
            biblioteca[i][1] = input("Novo Autor: ")
            biblioteca[i][2] = input("Novo Ano: ")
            print("Dados alterados com sucesso!")
            encontrou = True

    if encontrou == False:
        print("Livro não encontrado.")


def remover_livro(biblioteca):
    print("\n--- REMOVER LIVRO ---")
    cod_remover = input("Digite o código: ")

    posicao = -1
    for i in range(len(biblioteca)):
        if biblioteca[i][3] == cod_remover:
            posicao = i

    if posicao != -1:
        biblioteca.pop(posicao)
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado.")


def realizar_emprestimo(biblioteca):
    print("\n--- EMPRÉSTIMO ---")
    cod_emp = input("Digite o código: ")

    achou = False
    for i in range(len(biblioteca)):
        if biblioteca[i][3] == cod_emp:
            achou = True
            if biblioteca[i][4] == "Disponível":
                biblioteca[i][4] = "Emprestado"
                print("Empréstimo realizado!")
            else:
                print("Livro já está emprestado.")

    if achou == False:
        print("Código não encontrado.")


def realizar_devolucao(biblioteca):
    print("\n--- DEVOLUÇÃO ---")
    cod_dev = input("Digite o código: ")

    achou = False
    for i in range(len(biblioteca)):
        if biblioteca[i][3] == cod_dev:
            achou = True
            if biblioteca[i][4] == "Emprestado":
                biblioteca[i][4] = "Disponível"
                print("Devolução realizada!")
            else:
                print("O livro já estava disponível.")

    if achou == False:
        print("Código não encontrado.")


def menu():
    lista_biblioteca = []

    rodando = True
    while rodando == True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Alterar Dados")
        print("4. Remover Livro")
        print("5. Listar Todos")
        print("6. Realizar Empréstimo")
        print("7. Realizar Devolução")
        print("8. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_livro(lista_biblioteca)
        elif escolha == "2":
            consultar_livro(lista_biblioteca)
        elif escolha == "3":
            alterar_dados(lista_biblioteca)
        elif escolha == "4":
            remover_livro(lista_biblioteca)
        elif escolha == "5":
            listar_livros(lista_biblioteca)
        elif escolha == "6":
            realizar_emprestimo(lista_biblioteca)
        elif escolha == "7":
            realizar_devolucao(lista_biblioteca)
        elif escolha == "8":
            print("Saindo do sistema...")
            rodando = False
        else:
            print("Opção inválida!")


menu()