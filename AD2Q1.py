# AD2 - Questão 1
#Aluno: Sebastiao Alves Polo: Sao Fidelis

# Subprogramas

def procura(nm):
    def localizaNoVetor(pals):
        if pals == []:
            return ""
        else:
            pal = pals[0]
            for p in pals:
                if len(p) > len(pal):
                    pal = p
            return pal

    dados = open(nm, "r")
    palavras = dados.readline().strip().split()
    qualLinha = contagemDeLinhasLidas= 1
    maior = localizaNoVetor(palavras)
    for linha in dados:
        contagemDeLinhasLidas += 1
        maiorAtual = localizaNoVetor(linha.strip().split())
        if len(maiorAtual) > len(maior):
            maior = maiorAtual
            qualLinha = contagemDeLinhasLidas
    dados.close()

    return maior, qualLinha


# Programa Principal

nome = input()
maiorPalavra, posicaoDaLinha = procura(nome)
print("Palavra mais comprida contida no arquivo:", maiorPalavra)
print("Comprimento:", len(maiorPalavra), "caracter(es)")
print("Localizada na linha", posicaoDaLinha,"do arquivo")