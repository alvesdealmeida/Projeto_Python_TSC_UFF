# APX2 - Questão 1
#Aluno: Sebastiao Alves Polo: Sao Fidelis

# Subprograma
def processa(nm):
    caracs = set()
    pals = set()
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        caracteres = linha.strip()
        ps = caracteres.split()
        for c in caracteres:
            caracs.add(c)
        for p in ps:
            pals.add(p)
    dados.close()
    return caracs, pals

def mostraOrdenado(msg, vals):
    print(msg)
    vals = ordena(vals)
    for v in vals:
        print(v)
    print()

def ordena(vals):
    def seleciona(p, vs):
        pos = p
        for i in range(p + 1, len(vs)):
            if vs[i] < vs[pos]:
                pos = i
        return pos

    vals = list(vals)
    for i in range(len(vals) - 1):
        posMenor = seleciona(i, vals)
        vals[i], vals[posMenor] = vals[posMenor], vals[i]
    return vals

# Programa Principal

nome = input()
caracteres, palavras = processa(nome)
mostraOrdenado("Caracteres encontrados no arquivo:", caracteres)
mostraOrdenado("Palavras encontradas no arquivo:", palavras)