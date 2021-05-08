# AD2 - Questões 4 (ordenação) e 5 (busca binária)
#Aluno: Sebastiao Alves Polo: Sao Fidelis


import struct

# Subprogramas
def ordenar(arq):
    arq.seek(0, 2)
    tam = arq.tell()

    for i in range(1, tam // 4):
        j = i
        arq.seek((j - 1) * 4, 0)
        num_anterior = struct.unpack("=i", arq.read(4))[0]
        num_atual = struct.unpack("=i", arq.read(4))[0]
        while j > 0 and num_anterior > num_atual:
            arq.seek((j - 1) * 4, 0)
            arq.write(struct.pack("=i", num_atual))
            arq.write(struct.pack("=i", num_anterior))
            j = j - 1
            if j > 0:
                arq.seek((j - 1) * 4, 0)
                num_anterior = struct.unpack("=i", arq.read(4))[0]


def buscar(arq, num):
    arq.seek(0, 2)
    tam = arq.tell()

    esq = 0
    dir = (tam // 4) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        arq.seek(meio * 4, 0)
        atual = struct.unpack("=i", arq.read(4))[0]
        if atual < num:
            esq = meio + 1
        elif atual > num:
            dir = meio - 1
        else:
            return meio

    return -1


# Programa Principal
nome_arquivo = input("Informe o nome do arquivo binário de números: ")

try:
    with open(nome_arquivo, "rb+") as numeros:
        ordenar(numeros)
        valor = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
        while valor != -1:
            pos = buscar(numeros, valor)
            if pos != -1:
                print("O número está na posição %d." % pos)
            else:
                print("O número não foi encontrado")
            valor = int(input("Favor informar o valor a ser encontrado (-1 para sair): "))
except IOError:
    print("Erro ar abrir ou manipular o arquivo.")
