# AP2X - Questão 3 - Programa auxiliar para escrever um aquivo de entrada 
# Aluno: Sebastiao Alves   Polo: Sao Fidelis

import struct

with open('bolo.bin', 'wb') as arq:
    nlinhas_bolo = int(input('Informe a quantidade de linhas do bolo: '))
    arq.write(struct.pack('=i', nlinhas_bolo))
    ncolunas_bolo = int(input('Informe a quantidade de colunas do bolo: '))
    arq.write(struct.pack('=i', ncolunas_bolo))
    nlinhas_pedaco = int(input('Informe a quantidade de linhas do pedaço: '))
    arq.write(struct.pack('=i', nlinhas_pedaco))
    ncolunas_pedaco = int(input('Informe a quantidade de colunas do pedaço: '))
    arq.write(struct.pack('=i', ncolunas_pedaco))
    for lin in range(nlinhas_bolo):
        for col in range(ncolunas_bolo):
            uvas = int(input('Informe a quantidade de uvas-passas na posição %d, %d: ' % (lin, col)))
            arq.write(struct.pack('=i', uvas))
