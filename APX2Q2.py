# APX2 - Questão 2
#Aluno: Sebastiao Alves Polo: Sao Fidelis

# Subprogramas

def processa(nm):
    def localiza(p, tabMeds):
        for i in range(len(tabMeds)):
            if tabMeds[i][3] == p:
                return i
        return -1

    def insere(medal, vals):
        if medal == "ouro":
            return (vals[0] + 1, vals[1], vals[2], vals[3])
        elif medal == "prata":
            return (vals[0], vals[1] + 1, vals[2], vals[3])
        else:
            return (vals[0], vals[1], vals[2] + 1, vals[3])

    tabMedalhas = []
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        pais, medalha, modalidade = linha.split("#")
        onde = localiza(pais, tabMedalhas)
        if onde == -1:
            tabMedalhas.append(insere(medalha, (0, 0, 0, pais)))
        else:
            tabMedalhas[onde] = insere(medalha, tabMedalhas[onde])
    dados.close()
    return tabMedalhas


def mostra(vals):
    print("Tabela:")
    for x in sorted(vals, reverse=True):
        print(x)
    print()

# Programa Principal

nome = input()
tabela = processa(nome)
mostra(tabela)