# AP3X - Questão 1
# Aluno: Sebastiao Alves  Polo: Sao Fidelis

# Subprogramas

def processaEstado(cA, cB, nomeEstado, qtdDels, vts, delsA, delsB):
    dadosEst = open(nomeEstado, "r")
    votosEstado = dict()
    votosEstado[cA] = 0
    votosEstado[cB] = 0
    for linha in dadosEst:
        votosEstado[linha.strip("\n")] += 1
    dadosEst.close()
    vts[cA] += votosEstado[cA]
    vts[cB] += votosEstado[cB]
    if votosEstado[cA] < votosEstado[cB]:
        delsB.add((nomeEstado, qtdDels))
    elif votosEstado[cA] > votosEstado[cB]:
        delsA.add((nomeEstado, qtdDels))
    else:
        delsA.add((nomeEstado, qtdDels))
        delsB.add((nomeEstado, qtdDels))


def mostraDelegadosOrdenadosETotaliza(nmC, conjEstsDels, vs):
    print(nmC, "conquistou Delegado(s) no(s) Estado(s):")
    total = 0
    for estado, qtdDels in sorted(conjEstsDels):
        print("\t", estado+":", qtdDels)
        total += qtdDels
    print("Total de Delegados para", nmC + ":", total)
    print("Total de Votos para", nmC + ":", vs[nmC])
    print("X" * 40, "\n")


def mostra(nmCA, nmCB, vts, delsA, delsB):
    mostraDelegadosOrdenadosETotaliza(nmCA, delsA, vts)
    mostraDelegadosOrdenadosETotaliza(nmCB, delsB, vts)


def processaEleicoes(candA, candB, nmArq):
    votos = dict()
    votos[candA] = 0
    votos[candB] = 0
    delegadosA = set()
    delegadosB = set()
    dados = open(nmArq, "r")
    for linha in dados:
        estado, qtdDelegados = linha.split("#")
        qtdDelegados = int(qtdDelegados)
        processaEstado(candA, candB, estado, qtdDelegados, votos, delegadosA, delegadosB)
    dados.close()
    mostra(candA, candB, votos, delegadosA, delegadosB)

# Programa Principal

primeiroCandidato = input()
segundoCandidato = input()
nomeArq = input()
processaEleicoes(primeiroCandidato, segundoCandidato, nomeArq)
