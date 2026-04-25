from validacoes import validacao, validacao_ISBN, validacao_ano, validacao_preco, validacao_qtd, validacao_vazio, validacao_filial

class Livraria:
    def __init__(self):
        self.livros = []             

    def cadastro(self, livro):
        self.livros.append(livro)

    def listar(self):
        for livro in self.livros:
            print(f"\n>>>Cod#{livro.codigo}"
                  f"\nTitulo/Editora: {livro.titulo}/{livro.editora}"
                  f"\nCategoria: {livro.area}"
                  f"\nAno: {livro.ano}"
                  f"\nValor: R$ {livro.valor:.2f}"
                  f"\nEstoque: {livro.qtd} unidades"
                  f"\nValor total em estoque: R$ {livro.valor * livro.qtd:.2f}"
                  )

    def busca_por_nome(self, nome):
        print(f"\nResultados para a sua busca de: {nome}")
        possui = 0
        for livro in self.livros:
            if livro.titulo.upper() == nome.upper():
                possui += 1
                print(f"\n>>>Cod#{livro.codigo}"
                  f"\nTitulo/Editora: {livro.titulo}/{livro.editora}"
                  f"\nCategoria: {livro.area}"
                  f"\nAno: {livro.ano}"
                  f"\nValor: R$ {livro.valor:.2f}"
                  f"\nEstoque: {livro.qtd} unidades"
                  f"\nValor total em estoque: R$ {livro.valor * livro.qtd:.2f}"
                  )
        if possui == 0:
            print("Sem resultados.")


    def busca_categoria(self, categoria):
        print(f"\nResultados para a sua busca na categoria: {categoria}")
        possui = 0
        for livro in self.livros:
            if livro.area.upper() == categoria.upper():
                possui += 1
                print(f"\n>>>Cod#{livro.codigo}"
                  f"\nTitulo/Editora: {livro.titulo}/{livro.editora}"
                  f"\nCategoria: {livro.area}"
                  f"\nAno: {livro.ano}"
                  f"\nValor: R$ {livro.valor:.2f}"
                  f"\nEstoque: {livro.qtd} unidades"
                  f"\nValor total em estoque: R$ {livro.valor * livro.qtd:.2f}"
                  )
        if possui == 0:
            print("Sem resultados.")


    def busca_valor(self, valor):
        print(f"\nResultados para a sua busca por valor menor que: R${valor:.2f}")
        possui = 0
        for livro in self.livros:
            if livro.valor < valor:
                possui += 1
                print(f"\n>>>Cod#{livro.codigo}"
                  f"\nTitulo/Editora: {livro.titulo}/{livro.editora}"
                  f"\nCategoria: {livro.area}"
                  f"\nAno: {livro.ano}"
                  f"\nValor: R$ {livro.valor:.2f}"
                  f"\nEstoque: {livro.qtd} unidades"
                  f"\nValor total em estoque: R$ {livro.valor * livro.qtd:.2f}"
                  )
        if possui == 0:
            print("Sem resultados.")


    def busca_estoque(self, estoque):
        print(f"\nResultados para a sua busca por estoque maior do que: {estoque}un.")
        possui = 0
        for livro in self.livros:
            if livro.qtd > estoque:
                possui += 1
                print(f"\n>>>Cod#{livro.codigo}"
                  f"\nTitulo/Editora: {livro.titulo}/{livro.editora}"
                  f"\nCategoria: {livro.area}"
                  f"\nAno: {livro.ano}"
                  f"\nValor: R$ {livro.valor:.2f}"
                  f"\nEstoque: {livro.qtd} unidades"
                  f"\nValor total em estoque: R$ {livro.valor * livro.qtd:.2f}"
                  )
        if possui == 0:
            print("Sem resultados.")


    def total_estoque(self):
        unidades = 0
        valor_total = 0
        for livro in self.livros:
            unidades += livro.qtd
            valor_total += livro.qtd * livro.valor
        if unidades == 0:
            print("Sem livros/valor em estoque.")
        else:
            print(f"\nValor total em estoque R$ {valor_total:.2f}"
                  f"\nQuantidade total de livros em estoque: {unidades}un.")


    def carrega_csv(self):
        self.livros = []         #Limpa a lista de livros para evitar duplicidade de registros.
        with open('db.csv', 'r') as estoque:
            for linha in estoque:
                livro = linha.split(',')
                codigo = livro[0]
                titulo = livro[1]
                ano = livro[2]
                categoria = livro[3]
                editora = livro[4]
                preco = float(livro[5].replace("R$",""))
                quantidade = livro[6]
                check_cod = validacao_ISBN(codigo)
                check_ano = validacao_ano(ano)
                check_preco = validacao_preco(preco)
                check_qtd = validacao_qtd(quantidade)
                if (check_cod and check_ano and check_preco and check_qtd):
                    livro = [titulo, codigo, editora, categoria, ano, preco, quantidade]
                    livro = Livro(titulo, codigo, editora, categoria, ano, preco, int(quantidade))
                    livraria.cadastro(livro)
                else:
                    print(f"Livro {livro}não cadastrado."
                          "\nVerificar erro especificado acima.")

    def atualiza_csv(self):
        with open('db.csv', 'w') as estoque:
            for livro in self.livros:
                linha = ",".join([livro.codigo,
                                 livro.titulo, 
                                 livro.ano,
                                 livro.area,
                                 livro.editora,
                                 f"{livro.valor:.2f}", str(livro.qtd),"\n"]
                                )
                estoque.write(linha)


class Livro:
    def __init__(self, titulo, codigo, editora, area, ano, valor, qtd_estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.qtd = qtd_estoque


class Filial(Livraria):
    def __init__(self, codigo, nome, endereco, contato):
        super().__init__()
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
    

if __name__ == '__main__':

    livraria = Livraria()
    filiais = []

    flag_sistema = True

    while flag_sistema != False:
        print("\n-LIVRO STORE-\n")
        menu = input("-Início-\nDigite a opção desejada:"
                     "\n1-Cadastrar novo livro"
                     "\n2-Listar livros"
                     "\n3-Buscar livros por nome"
                     "\n4-Buscar livros por categoria"
                     "\n5-Buscar livros por preço"
                     "\n6-Busca por quantidade em estoque"
                     "\n7-Valor total no estoque"
                     "\n8-Carregar estoque"
                     "\n9-Atualizar arquivo de estoque"
                     "\n10-Cadastrar nova filial"
                     "\n0-Encerrar atividades\n\n").strip()

        check = validacao(menu)                                         #Validação da entrada/seleção opção menu.

        if check == False:
            print("\n\nENTRADA INVÁLIDA, SELECIONE UMA DAS OPÇÕES ABAIXO.\n")

        if check and menu == "1":                                #Cadastro de livros.
            print("\n--Cadastro de livros--\n")
            flag_titulo = True
            while flag_titulo:
                titulo = input("\nDigite o título do livro: ").strip()
                verificacao = validacao_vazio(titulo)
                if verificacao:
                    flag_titulo = False
                else: 
                    print("\nDigite novamente.")

            flag_codigo = True                                           #Flag e Loop para validação do código ISBN.
            while flag_codigo:    
                codigo = input("\nDigite o código do livro: ").strip()
                verificacao = validacao_ISBN(codigo)
                if verificacao:
                    flag_codigo = False
                else: 
                    print("\nDigite novamente.")

            flag_editora = True
            while flag_editora:
                editora = input("\nDigite a editora do livro: ").strip()
                verificacao = validacao_vazio(editora)
                if verificacao:
                    flag_editora = False
                else: 
                   print("\nDigite novamente.")

            flag_categoria = True
            while flag_categoria:
                categoria = input("\nDigite a categoria do livro: ").strip()
                verificacao = validacao_vazio(categoria)
                if verificacao:
                    flag_categoria = False
                else: 
                   print("\nDigite novamente.")
            
            flag_ano = True                                            #Flag e Loop para validação do ano.
            while flag_ano:
                ano = input("\nDigite o ano de lançamento do livro: ").strip()
                verificacao = validacao_ano(ano)
                if verificacao:
                    flag_ano = False
                else:
                    print("\nDigite novamente.")

            flag_preco = True                                          #Flag e Loop para validação do preço.
            while flag_preco:
                preco = input("\nDigite o preço unitário do livro: ").replace(",", ".")
                verificacao = validacao_preco(preco)
                if verificacao:
                    preco = float(preco)
                    flag_preco = False
                else:
                    print("\nDigite novamente.")
                
            flag_qtd = True                                            #Flag e Loop para validação da quantidade.
            while flag_qtd:
                quantidade = input("\nDigite a quantidade de livros: ")
                verificacao = validacao_qtd(quantidade)
                if verificacao:
                    quantidade = int(quantidade)
                    flag_qtd = False
                else:
                    print("\nDigite novamente.")
                
            flag_filial = True
            while flag_filial:
                filial_livro = input("\nDigite o código da filial onde o livro será cadastrado: ").strip()
                verificacao = validacao_filial(filial_livro, filiais)
                if verificacao:
                    flag_filial = False
                else:
                    print("\nFilial não encontrada. Digite novamente.")
                            
            for filial in filiais:
                if filial.codigo == filial_livro:
                    filial.cadastro(Livro(titulo,
                                          codigo,
                                          editora,
                                          categoria,
                                          ano,
                                          preco,
                                          quantidade)
                                    )
                    print(f"\nLivro cadastrado com sucesso na filial {filial.nome}!\n")
                    
            # livro = Livro(titulo, codigo, editora, categoria, ano, preco, quantidade)
            # livraria.cadastro(livro)
            # print("\nLivro cadastrado com sucesso!\n")


        if check and menu == "2":                            #Listagem de livros cadastrados.
                if len(livraria.livros) == 0:
                    print("\nNão existem livros cadastrados.")
                else:
                    print("\n--Lista de livros cadastrados--\n")
                    livraria.listar()

        if check and menu == "3":                             # Busca por nome/titulo.
            print("\n--Buscar livros por nome--\n")
            nome = input("\nDigite o nome/título do livro: ").strip()
            livraria.busca_por_nome(nome)

        if check and menu == "4":                             # Busca por categoria.
            print("\n--Buscar livros por categoria--\n")
            categoria = input("\nDigite a categoria desejada: ").strip()
            livraria.busca_categoria(categoria)

        if check and menu == "5":                             # Busca por preço.
            print("\n--Buscar livros com preço menor do que o indicado--\n")
            valor = float(input("\nDigite o preço acima do que deseja: "))
            livraria.busca_valor(valor)

        if check and menu == "6":                             # Busca por estoque.
            print("\n--Buscar livros com estoque maior do que o indicado--\n")
            estoque = int(input("\nDigite o estoque abaixo do que deseja: "))
            livraria.busca_estoque(estoque)

        if check and menu == "7":                             # Consulta valor total do estoque
            print("\n--Valor total em estoque--\n")
            livraria.total_estoque()

        if check and menu == "8":                             # Carrega produtos cadastrados no estoque CSV
            print("\n--Carregar estoque--\n")
            livraria.carrega_csv()
            print("\nEstoque carregado com sucesso!\n")

        if check and menu == "9":                             # Salva as novas alterações/cadastros realizados no estoque CSV
            print("\n--Atualizar arquivo de estoque--\n")
            livraria.atualiza_csv()
            print("\nAlterações salvas com sucesso!\n")

        if check and menu == "10":                              # Cria a filial e adiciona na lista atual de filiais
            print("\n--Cadastro de filial--\n")
            codigo = input("\nDigite o código da filial: ").strip()
            nome = input("\nDigite o nome da filial: ").strip()
            endereco = input("\nDigite o endereço da filial: ").strip()
            contato = input("\nDigite o contato/telefone da filial: ").strip()
            filial = Filial(codigo, nome, endereco, contato)
            filiais.append(filial)
            print("\nFilial cadastrada com sucesso!\n")

        if check and menu == "0":                             # Fechar sistema e verifica se deseja salvar alterações
            flag_encerramento = True
            while flag_encerramento:
                opcao = input("\nDeseja salvar as alterações realizadas no arquivo de estoque? S ou N\n")
                if opcao.upper() == 'S':
                    livraria.atualiza_csv()
                    print("\nAs alterações salvas com sucesso!\n") 
                    flag_encerramento = False
                if opcao.upper() == 'N':
                    print("\nAs alterações foram descartadas.\n") 
                    flag_encerramento = False
                else:
                    print("\nEntrada inválida. Digite novamente.")
            print("\nEncerrando o sistema...\n")
            flag_sistema = False
