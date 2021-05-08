# AD2 - Questão 2
#Aluno: Sebastiao Alves Polo: Sao Fidelis

# Subprogramas

def localiza(codBuscado, nm):
    dados = open(nm, "r")
    achou = False
    for linha in dados:
        cod, qtdStr, precoStr= linha.strip().split("#")
        if cod == codBuscado:
            achou = True
            print("Produto Localizado:", cod)
            print("Preço Unitário: R$", precoStr)
            print("Quantidade Disponível:", qtdStr)
    dados.close()
    if not achou:
        print("código inexistente!!!")
    return None


# Programa Principal
codigoProcurado = input()
nomeArquivoMercado = input()
localiza(codigoProcurado, nomeArquivoMercado)