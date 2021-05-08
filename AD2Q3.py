# AD2 - Questão 3
#Aluno: Sebastiao Alves Polo: Sao Fidelis


# Subprogramas
def insere(partida, tabJogos):
    timeA, golsA, timeB, golsB = partida.split("#")
    if tabJogos.get(timeA) == None:
        tabJogos[timeA] = 0
    if tabJogos.get(timeB) == None:
        tabJogos[timeB] = 0
    golsA, golsB = int(golsA), int(golsB)
    if golsA > golsB:
        tabJogos[timeA] += 3
    elif golsA < golsB:
        tabJogos[timeB] += 3
    else:
        tabJogos[timeA] += 1
        tabJogos[timeB] += 1


def mostraOrdenado(qtd, tabJogos):
    print("Tabela após", qtd, "partida(s):")
    for time, pontos in sorted(tabJogos.items()):
        print(time, pontos, "ponto(s)")
    print()


# Programa Principal
tabela = dict()
jogo = input()
qtdJogos = 0
while jogo != "":
    qtdJogos += 1
    insere(jogo, tabela)
    mostraOrdenado(qtdJogos, tabela)
    jogo = input()