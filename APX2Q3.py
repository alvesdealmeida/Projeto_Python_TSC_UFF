# APX2 - Questão 3 - Essa solução possui complexidade O(n^2), onde n = L*C. É possível resolver em complexidade O(N).
# Aluno: Sebastiao Alves Polo: Sao Fidelis

import struct

# Programa Principal

with open('bolo.bin', 'rb') as arq:
    # Ler dados de entrada vindos de um arquivo binário
    nlinhas_bolo = struct.unpack('=i', arq.read(4))[0]
    ncolunas_bolo = struct.unpack('=i', arq.read(4))[0]
    nlinhas_pedaco = struct.unpack('=i', arq.read(4))[0]
    ncolunas_pedaco = struct.unpack('=i', arq.read(4))[0]
    bolo = []
    for _ in range(nlinhas_bolo):
        linha = []
        for _ in range(ncolunas_bolo):
            linha.append(struct.unpack('=i', arq.read(4))[0])
        bolo.append(linha)

    # Inicializar o máximo conhecido com um valor muito pequeno
    maximo_conhecido = 0

    # Procurar a porção MxN com mais uvas-passas
    for lin_inicio in range(nlinhas_bolo-nlinhas_pedaco+1):
        for col_inicio in range(ncolunas_bolo-ncolunas_pedaco+1):
            soma = 0
            for lin_pedaco in range(nlinhas_pedaco):
                for col_pedaco in range(ncolunas_pedaco):
                    soma += bolo[lin_inicio+lin_pedaco][col_inicio+col_pedaco]
            if soma > maximo_conhecido:
                maximo_conhecido = soma

    # Exibir o resultado
    print(maximo_conhecido)
