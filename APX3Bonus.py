# APX3 - Questão Bônus
# Aluno: Sebastiao alves   Polo: São Fidelis

# Subprograma

def ordenar_tuplas(lista):
    # Usar bubble sort para ordenar por quantidade de ajudas e depois por identificador do funcionário
    for tamanho in range(len(lista)-1, 0, -1):
        for i in range(tamanho):
            tupla1 = lista[i]
            tupla2 = lista[i+1]
            if (tupla1[0] > tupla2[0]) or (tupla1[0] == tupla2[0] and tupla1[1] > tupla2[1]):  # A condição pode ser escrita como tupla1 > tupla2, apenas
                lista[i], lista[i+1] = lista[i+1], lista[i]

# Programa Principal

t = 1
f, a = map(int, input().split())
# Para cada caso de testes...
while f != 0 and a != 0:
    # Contar quantas vezes cada funcionário prestou ajuda
    ajudas = [0] * f
    for i in range(a):
        f1, f2 = map(int, input().split())
        ajudas[f1-1] += 1
        ajudas[f2-1] += 1
    # Associar a quantidade de ajudas prestadas ao identificado do funcionário
    for i in range(f):
        ajudas[i] = (ajudas[i], i + 1)
    # Ordenar a lista por quantidade de ajudas e depois por identificado do funcionário
    ordenar_tuplas(ajudas)
    # Identificadores no final da lista indicam quem prestou a maior quantidade de ajudas. A ordenação é quem nos deu essa informação!
    mais_ajudas = ajudas[f-1][0]
    i = f - 2
    while i >= 0 and mais_ajudas == ajudas[i][0]:
        i -= 1
    i += 1
    # Mostrar os funcionários no final da lista
    print('Teste', t)
    while i < f:
        print(ajudas[i][1], end=' ')
        i += 1
    print('\n')
    # Ir para o próximo caso de testes
    t += 1
    f, a = map(int, input().split())

