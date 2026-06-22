# Classe que define a estrutura de um objeto 'Livro'
class Livro:
    # O método __init__ inicializa os atributos do livro quando um novo objeto é criado
    def __init__(self, titulo, autor, ano, codigo, status):
        self.titulo = titulo  # Armazena o nome da obra
        self.autor = autor    # Armazena o nome do autor
        self.ano = ano        # Armazena o ano de lançamento
        self.codigo = codigo  # Armazena o identificador único (ID)
        self.status = status  # Armazena se está 'disponível' ou 'emprestado'

# Cadastrar livro
def cadastrar_livro(biblioteca):
    print("\n--- CADASTRAR LIVRO ---")
    codigo = input("Código (ID único): ")
   
    # Percorre a lista para garantir que não existam dois livros com o mesmo código
    ja_existe = 0
    for livro in biblioteca:
        if livro.codigo == codigo:
            ja_existe = 1
            break
           
    # Se o código for único, solicita os dados e adiciona o novo objeto à lista
    if ja_existe == 1:
        print("Erro: Já existe um livro com este código.")
    else:
        titulo = input("Título: ")
        autor = input("Autor (apenas o primeiro nome): ")
        ano = input("Ano de publicação: ")
        # Cria a instância da classe Livro e a insere na lista 'biblioteca'
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
    # Opção 1: Busca o código informado
    if opcao == "1":
        cod_busca = input("Digite o código: ")
        for livro in biblioteca:
            if livro.codigo == cod_busca:
                print(f"Livro encontrado: {livro.titulo} - {livro.autor} ({livro.status})")
                encontrado = 1
                break
    else:
        # Opção 2: Busca por autor (comparação exata de strings
        if opcao == "2":
            aut_busca = input("Digite o autor: ")
            for livro in biblioteca:
                if livro.autor == aut_busca:
                    print(f"Obra: {livro.titulo} | Código: {livro.codigo} | Status: {livro.status}")
                    encontrado = 1
        else:
            print("Opção inválida.")
            return

    # Exibe mensagem caso nenhum registro satisfaça o critério de busca
    if encontrado == 0:
        print("Livro não encontrado")

# Alterar dados
def alterar_dados(biblioteca):
    print("\n--- ALTERAR DADOS ---")
    codigo = input("Digite o código do livro: ")
    achou = 0
    # Localiza o livro pelo código e permite a sobrescrita dos atributos de texto
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
    # Identifica o índice numérico do livro na lista para possibilitar a remoção
    for i in range(len(biblioteca)):
        if biblioteca[i].codigo == codigo:
            posicao = i
            break
           
    # Se encontrado, usa o pop() para excluir o item da lista pelo índice
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

    # Cria uma cópia da lista original para não alterar a ordem de inserção do biblio
    temp_lista = []
    for item in biblioteca:
        temp_lista.append(item)

    # compara pares adjacentes e os troca se estiverem fora de ordem
    n = len(temp_lista)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            # Compara os títulos para definir a ordem alfabética
            if temp_lista[j].titulo > temp_lista[j+1].titulo:
                auxiliar = temp_lista[j]
                temp_lista[j] = temp_lista[j+1]
                temp_lista[j+1] = auxiliar
            j = j + 1
        i = i + 1

    # Exibe a lista já organizada
    for livro in temp_lista:
        print(f"Título: {livro.titulo} - Ano: {livro.ano}")

# Realizar empréstimo
def realizar_emprestimo(biblioteca):
    print("\n--- REALIZAR EMPRÉSTIMO ---")
    codigo = input("Código do livro: ")
    achou = 0
    # Verifica se o livro existe e se o status atual permite o empréstimo
    for livro in biblioteca:
        if livro.codigo == codigo:
            achou = 1
            if livro.status == "disponível":
                livro.status = "emprestado"  # Atualiza o estado do objeto
                print("Empréstimo realizado!")
            else:
                print("Livro já emprestado")
            break
   
    if achou == 0:
        print("Livro não encontrado")

# Realizar devolução e menu
def realizar_devolucao(biblioteca):
    print("\n--- REALIZAR DEVOLUÇÃO ---")
    codigo = input("Código do livro: ")
    achou = 0
    # Localiza o livro e altera o status de volta para 'disponível'
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

# Função que gerencia o fluxo principal do programa
def menu_principal():
    biblio = []  # Lista que funcionará como banco de dados em memória
    rodando = 1  # Variável que mantém o programa em execução
   
    # Loop que exibe as opções e processa a entrada do usuário até que ele escolha sair
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
       
        # Estrutura de decisão para rotear a execução para a função correta
        if escolha == "1":
            cadastrar_livro(biblio)
        else:
            if escolha == "2":
                consultar_livro(biblio)
            else:
                if escolha == "3":
                    alterar_dados(biblio)
                else:
                    if escolha == "4":
                        remover_livro(biblio)
                    else:
                        if escolha == "5":
                            listar_todos(biblio)
                        else:
                            if escolha == "6":
                                realizar_emprestimo(biblio)
                            else:
                                if escolha == "7":
                                    realizar_devolucao(biblio)
                                else:
                                    if escolha == "8":
                                        print("Finalizando programa...")
                                        rodando = 0  # Quebra a condição do loop while
                                    else:
                                        print("Opção inválida!")

# Inicia o programa chamando o menu principal
if __name__ == "__main__":
    menu_principal()
