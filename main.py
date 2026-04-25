from validacoes import validacao, validacao_ISBN, validacao_ano, validacao_preco, validacao_qtd, validacao_vazio, validacao_filial, duplicidade_livro, voltar

class Livraria:
    def __init__(self):
        self.filiais = []
        self.livros = []             

    def cadastro(self, livro):
        self.livros.append(livro)

    def listar(self):
        print(f"\n\n-- Filial {self.nome} --")
        self.total_estoque()
        print("\n- Livros cadastrados -")
        if len(self.livros) == 0:
            print("\nNão existem livros cadastrados.")
        else:
            for livro in self.livros:
                print(f"\n>>>Cod#{livro.codigo}"
                    f"\nTitulo/Editora: {livro.titulo}/{livro.editora}"
                    f"\nCategoria: {livro.area}"
                    f"\nAno: {livro.ano}"
                    f"\nValor: R$ {livro.valor:.2f}"
                    f"\nEstoque: {livro.qtd} unidades"
                    f"\nValor total em estoque: R$ {livro.valor * livro.qtd:.2f}"
                    )

    def listar_filiais(self):
        print("\n\n--Filiais--")
        for filial in self.filiais:
            print(f"\n>>>Código: {filial.codigo}"
                  f"\nLoja: {filial.nome}"
                  f"\nEndereço: {filial.endereco}"
                  f"\nContato: {filial.contato}"
                  )

    def busca_por_nome(self, nome):
        print(f"\nResultados para a sua busca de: {nome}")
        possui = 0
        for filial in self.filiais:
            for livro in filial.livros:
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
            print("\nSem resultados.")


    def busca_categoria(self, categoria):
        print(f"\nResultados para a sua busca na categoria: {categoria}")
        possui = 0
        for filial in self.filiais:
            for livro in filial.livros:
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
            print("\nSem resultados.")


    def busca_valor(self, valor):
        print(f"\nResultados para a sua busca por valor menor que: R${valor:.2f}")
        possui = 0
        for filial in self.filiais:
            for livro in filial.livros:
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
        for filial in self.filiais:
            for livro in filial.livros:
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
        self.filiais = []         #Limpa a lista de filiais para evitar duplicidade.
        with open('db.csv', 'r', encoding='utf-8') as estoque:
            filial = None
            for leitura in estoque:
                checagem = leitura.split(',')
                if checagem[0][0] == "#":                #Identifica se a linha lida é referente a uma filial ou livro.
                    codigo = checagem[0].replace("#FL","").strip()
                    nome = checagem[1].strip()
                    endereco = checagem[2].strip()
                    contato = checagem[3].strip().strip()
                    filial = Filial(codigo, nome, endereco, contato)
                    self.filiais.append(filial)
                else:
                    livro = leitura.split(',')
                    codigo = livro[0].strip()
                    titulo = livro[1].strip()
                    ano = livro[2].strip()
                    categoria = livro[3].strip()
                    editora = livro[4].strip()
                    preco = float(livro[5].strip().replace("R$",""))
                    quantidade = livro[6].strip()
                    check_cod = validacao_ISBN(codigo)
                    check_ano = validacao_ano(ano)
                    check_preco = validacao_preco(preco)
                    check_qtd = validacao_qtd(quantidade)
                    if (check_cod and check_ano and check_preco and check_qtd):
                        livro = [titulo, codigo, editora, categoria, ano, preco, quantidade]
                        filial.cadastro(Livro(titulo,
                                              codigo,
                                              editora,
                                              categoria,
                                              ano, preco,
                                              int(quantidade)
                                              )
                                        )
                    else:
                        print(f"Livro {livro}não cadastrado."
                            "\nVerificar erro especificado acima.")

    def atualiza_csv(self):
        with open('db.csv', 'w', encoding='utf-8') as estoque:
                for filial in self.filiais:                  #Cadastra as filiais e seus respectivos livros no arquivo CSV.
                    linha = ",".join([f"#FL{filial.codigo}",
                                    filial.nome,
                                    filial.endereco,
                                    filial.contato]
                                    )
                    estoque.write(linha) 
                    estoque.write("\n")
                    for livro in filial.livros:
                        linha = ",".join([livro.codigo,
                                        livro.titulo, 
                                        livro.ano,
                                        livro.area,
                                        livro.editora,
                                        f"{livro.valor:.2f}", str(livro.qtd)]
                                        )
                        estoque.write(linha)
                        estoque.write("\n")


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

    flag_sistema = True

    while flag_sistema != False:
        print("\n\n-LIVRO STORE-\n")
        menu = input("-Início-\nDigite a opção desejada:"
                     "\n1-Cadastrar novo livro"
                     "\n2-Listagem de estoque"
                     "\n3-Buscar livros por nome"
                     "\n4-Buscar livros por categoria"
                     "\n5-Buscar livros por preço"
                     "\n6-Busca por quantidade em estoque"
                     "\n7-Busca por código ISBN (todas as filiais)"
                     "\n8-Valor total no estoque"
                     "\n9-Carregar estoque"
                     "\n10-Atualizar arquivo de estoque"
                     "\n11-Cadastrar nova filial"
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
            livraria.listar_filiais()                              #Lista as filiais existentes para o cadastro do livro.
            while flag_filial:
                filial_livro = input("\nDigite o código da filial onde o livro será cadastrado: ").strip()
                verificacao = validacao_filial(filial_livro, livraria.filiais)
                if verificacao:
                    for filial in livraria.filiais:
                        if filial.codigo == filial_livro:
                            verificacao_duplicidade = duplicidade_livro(codigo, titulo, livraria.livros)
                            if verificacao_duplicidade:
                                filial.cadastro(Livro(titulo,
                                                    codigo,
                                                    editora,
                                                    categoria,
                                                    ano,
                                                    preco,
                                                    quantidade)
                                                )
                                print(f"\nLivro cadastrado com sucesso na filial {filial.nome}!\n")
                                flag_filial = False
                            else:
                                print("\nLivro já cadastrado nesta filial.")
                                voltar_menu = voltar()
                                if voltar_menu:
                                    flag_filial = False
                                
                else:
                    print("\nFilial não encontrada. Digite novamente.")


        if check and menu == "2":                            #Listagem de livros cadastrado por filial.
                    flag_listagem = True
                    while flag_listagem:
                        print("\n--Lista de livros cadastrados--\n")
                        codigo_filial = input("\nDigite o código da filial em que deseja realizar a consulta: ").strip()
                        verificacao = validacao_filial(codigo_filial, livraria.filiais)
                        if verificacao:
                            for filial_cadastrada in livraria.filiais:
                                if filial_cadastrada.codigo == codigo_filial:
                                    filial_cadastrada.listar()
                                    flag_listagem = False
                        else:
                            print("\nFilial não encontrada.")

        if check and menu == "3":                             # Busca por nome/titulo individualmente por filial.
            flag_busca = True
            while flag_busca:
                        print("\n--Buscar livros por nome--\n")
                        codigo_filial = input("\nDigite o código da filial em que deseja realizar a consulta: ").strip()
                        verificacao = validacao_filial(codigo_filial, livraria.filiais)
                        if verificacao:
                            nome = input("\nDigite o nome/título do livro: ").strip()
                            livraria.busca_por_nome(nome)
                            flag_busca = False
                        else:
                            print("\nFilial não encontrada.")
            
        if check and menu == "4":                                    # Busca por categoria individualmente por filial.
            flag_busca = True
            while flag_busca:
                print("\n--Buscar livros por categoria--\n")
                codigo_filial = input("\nDigite o código da filial em que deseja realizar a consulta: ").strip()
                verificacao = validacao_filial(codigo_filial, livraria.filiais)
                if verificacao:
                    categoria = input("\nDigite a categoria desejada: ").strip()
                    livraria.busca_categoria(categoria)
                    flag_busca = False
                else:
                    print("\nFilial não encontrada.") 
                                                                                               
        if check and menu == "5":   
            flag_busca = True                                                        # Busca por preço individualmente por filial.
            while flag_busca:
                print("\n--Buscar livros com preço menor do que o indicado--\n")
                codigo_filial = input("\nDigite o código da filial em que deseja realizar a consulta: ").strip()
                verificacao = validacao_filial(codigo_filial, livraria.filiais)
                if verificacao:
                    valor = float(input("\nDigite o preço acima do que deseja: ").strip())
                    livraria.busca_valor(valor)
                    flag_busca = False
                else:
                    print("\nFilial não encontrada.")
                        
        if check and menu == "6":  
            flag_busca = True                                                        # Busca por quantidade no estoque individualmente por filial.
            while flag_busca:
                print("\n--Buscar livros com estoque maior do que o indicado--\n")
                codigo_filial = input("\nDigite o código da filial em que deseja realizar a consulta: ").strip()
                verificacao = validacao_filial(codigo_filial, livraria.filiais)
                if verificacao:
                    estoque = int(input("\nDigite o estoque abaixo do que deseja: ").strip())
                    livraria.busca_estoque(estoque)
                    flag_busca = False
                else:
                    print("\nFilial não encontrada.")                                                     
            
        if check and menu == "7":
            flag_busca = True                                                        # Busca por código ISBN (em todas as filiais).
            while flag_busca:
                ocorrencias = []
                total_estoque = 0
                print("\n--Buscar livros por código ISBN--\n")
                codigo_ISBN = input("\nDigite o código ISBN do livro: ").strip()
                verificacao = validacao_ISBN(codigo_ISBN)
                if verificacao:
                    for filial in livraria.filiais:
                        for livro in filial.livros:
                            if livro.codigo == codigo_ISBN:
                                if len(ocorrencias) == 0:
                                    print(f"\n>>>Cod#{livro.codigo}"
                                        f"\nTitulo/Editora: {livro.titulo}/{livro.editora}"
                                        f"\nCategoria: {livro.area}"
                                        f"\nAno: {livro.ano}")
                                total_estoque += livro.qtd * livro.valor
                                ocorrencias.append([livro.valor, filial.nome , livro.qtd])

                if len(ocorrencias) == 0:
                    print("\nLivro não encontrado.")
                    flag_busca = False
                else:
                    for ocorrencia in ocorrencias:
                        print(f"Valor: R$ {ocorrencia[0]:.2f}"
                              f">>>Filial: {ocorrencia[1]},"
                              f"estoque: {ocorrencia[2]} unidades")
                        print(f"Valor total em estoque: R$ {total_estoque:.2f}")
                        flag_busca = False
                            

        if check and menu == "8":                                             # Consulta valor total do estoque da filial individualmente.
            flag_busca = True                                                       
            while flag_busca:
                print("\n--Valor total em estoque--\n")
                codigo_filial = input("\nDigite o código da filial em que deseja realizar a consulta: ").strip()
                verificacao = validacao_filial(codigo_filial, livraria.filiais)
                if verificacao:
                    for filial_cadastrada in livraria.filiais:
                        if filial_cadastrada.codigo == codigo_filial:
                            filial_cadastrada.total_estoque()
                            flag_busca = False                        
                else:
                    print("\nFilial não encontrada.")                                                     
            
        if check and menu == "9":                             # Carrega produtos cadastrados no estoque CSV
            print("\n--Carregar estoque--\n")
            livraria.carrega_csv()
            print("\nEstoque carregado com sucesso!\n")

        if check and menu == "10":                             # Salva as novas alterações/cadastros realizados no estoque CSV
            print("\n--Atualizar arquivo de estoque--\n")
            livraria.atualiza_csv()
            print("\nAlterações salvas com sucesso!\n")

        if check and menu == "11":                              # Cria a filial e adiciona na lista atual de filiais
            print("\n--Cadastro de filial--\n")
            codigo = input("\nDigite o código da filial: ").strip()
            nome = input("\nDigite o nome da filial: ").strip()
            endereco = input("\nDigite o endereço da filial: ").strip()
            contato = input("\nDigite o contato/telefone da filial: ").strip()
            filial = Filial(codigo, nome, endereco, contato)
            livraria.filiais.append(filial)
            print("\nFilial cadastrada com sucesso!\n")

        if check and menu == "0":                             # Fechar sistema e verifica se deseja salvar alterações
            flag_encerramento = True
            while flag_encerramento:
                opcao = input("\nDeseja salvar as alterações realizadas no arquivo de estoque? S ou N\n")
                if opcao.upper() == 'S':
                    livraria.atualiza_csv()
                    print("\nAs alterações salvas com sucesso!\n") 
                    flag_encerramento = False
                elif opcao.upper() == 'N':
                    print("\nAs alterações foram descartadas.\n") 
                    flag_encerramento = False
                else:
                    print("\nEntrada inválida. Digite novamente.")
            print("\nEncerrando o sistema...\n")
            flag_sistema = False
