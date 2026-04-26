import datetime as dt

def validacao(opcao):                                                 #Validacão da opção selecionada no menu.
    if opcao not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","10", "11"]:
        return False
    else:
        return True


def validacao_num(valor):                                             #Validação de entradas numéricas
    try:
        if float(valor) <= 0:
                print("\nValor inválido. O valor deve ser numérico e positivo.")
                raise ValueError
        else:
            return True              
    except ValueError:
            return False     
        

def validacao_ISBN(valor):
    verificacao = validacao_num(valor)
    if len(valor) != 13 or int(valor) <= 0:
        print("\nO código ISBN deve conter 13 caracteres e ser um numero positivo.")
    if verificacao and len(valor) == 13:
        return True
        

def validacao_ano(valor):
    try:
        int(valor)
        ano_atual = dt.date.today().year
        verificacao = validacao_num(valor)
        if verificacao:
            if int(valor) > ano_atual:
                print("\nAno informado inválido.\nO valor deve ser menor do que o ano atual.")
            if int(valor) <= ano_atual:
                return True
            else:
                return False
    except ValueError:
        print("\nA entrada deve ser numérica.")
            
    
def validacao_preco(valor):
    try:
        float(valor)
        verificacao = validacao_num(valor)
        if verificacao:
            return True
    except ValueError:
        print("\nA entrada deve ser numérica.")
        return False


def validacao_qtd(valor):
    try:
        int(valor)
        verificacao = validacao_num(valor)
        if verificacao:
            return True
    except ValueError:
        print("\nA quantidade deve ser um número inteiro.")
        return False
        
        
def validacao_vazio(valor):
    if len(valor) > 0:
        return True
    else:
        print("\nValor vazio, inválido!")
        return False
    

def validacao_filial(codigo, filiais):
    for filial in filiais:
        if filial.codigo == codigo:
            return True
    return False

def validacao_livro(codigo, livros):
    for livro in livros:
        if livro.codigo == codigo:
            return True
    return False
        
def duplicidade_livro(codigo, titulo, livros):
    check = True
    for livro in livros:
        if livro.codigo == codigo or livro.titulo == titulo:
            check = False
    return check

def voltar():
    while True:
        resposta = input("\nDeseja voltar ao menu principal? (S/N): ").strip().upper()
        if resposta == "S":
            return True
        elif resposta == "N":
            return False
        else:
            print("\nResposta inválida. Digite 'S' para sim ou 'N' para não.")

def valida_codigo_filial(codigo):
    try:
        float(codigo)
        verificacao = validacao_num(codigo)
        if verificacao and len(codigo) == 2:
            return True
    except ValueError:
        print("\nA entrada deve ser numérica e conter apenas dois digitos.")
        return False

def valida_telefone_filial(telefone):
    try:
        int(telefone)
        if len(telefone) == 10 or len(telefone) == 11:
            return True
        else:
            print("\nO número de telefone deve conter 10 ou 11 dígitos.")
            return False
    except ValueError:
        print("\nA entrada deve ser numérica.")
        return False