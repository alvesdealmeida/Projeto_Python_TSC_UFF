# AD2 - Questões 4 e 5 - Programa auxiliar 
#Aluno: Sebastiao Alves Polo: Sao Fidelis

import struct

nome_arquivo = input("Informe o nome do arquivo binário de números: ")
numeros = [110, 6, 109, 13, 78, 99, 2, 108, 25, 567];

try:
    with open(nome_arquivo, "wb") as arq:
        for num in numeros:
            arq.write(struct.pack("=i", num))
except IOError:
    print("Erro ar abrir ou manipular o arquivo.")
