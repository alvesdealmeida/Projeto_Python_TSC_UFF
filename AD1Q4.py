# AD1 - Quest�o 4
# Aluno: Sebasti�o Alves - S�o Fidelis

# Subprogramas
def repetir(texto, n):
    for _ in range(n):          # Uma forma mais "pythonica" de imprimir N repeti��es do mesmo texto � print(texto * n, end="")
        print(texto, end="")


def espacos(n):
    repetir(" ", n)


def hashtags(n):
    repetir("#", n)


def padrao1(n):
    for m in range(1, n + 1):  # Para cada uma das N linhas, indexadas por M igual a 1, 2, ..., N
        hashtags(m)            #     Imprimir M s�mbolos #
        print()                #     Quebrar linha
    print()                    # Deixar uma linha em branco no final


def padrao2(n):
    espacos(n - 1)                 # Imprimir s�mbolo # no topo do losango
    hashtags(1)                    # ..
    print()                        # Quebrar linha
    for m in range(2, n + 1):      # Para cada linha da parte superior do losango
        espacos(n - m)             #     Imprimir o s�mbolo # � esquerda
        hashtags(1)                #     ..
        espacos(2 * (m - 1) - 1)   #     Imprimir o s�mbolo # � direita
        hashtags(1)                #     ..
        print()                    #     Quebrar linha
    for m in range(n - 1, 1, -1):  # Para cada linha da parte inferior do losango
        espacos(n - m)             #     Imprimir o s�mbolo # � esquerda
        hashtags(1)                #     ..
        espacos(2 * (m - 1) - 1)   #     Imprimir o s�mbolo # � direita
        hashtags(1)                #     ..
        print()                    #     Quebrar linha
    if n != 1:                     # Se o losango possui mais que uma linha ent�o
        espacos(n - 1)             #     Imprimir s�mbolo # em baixo do losango
        hashtags(1)                #     ..
        print()                    #     Quebrar linha
    print()                        # Deixar uma linha em branco no final


def padrao3(n):
    repetir("     _ ", n)              # Imprimir topo da primeira linha de pe�as do quebra-cabe�a
    print()                            # ..
    espacos(2)                         # ..
    repetir(" _( )__", n)              # ..
    print()                            # ..
    for m in range(1, n + 1):          # Para cada linha de pe�as do quebra-cabe�a, indexadas de 1 at� N
        if m % 2 == 1:                 #     Se o �ndice da linha de pe�as for �mpar ent�o
            repetir(" _|    ", n + 1)  #         Imprimir padr�o de pe�as da linha �mpar do quebra-cabe�a
            print()                    #         ..
            repetir("(_   _ ", n)      #         ..
            print("(_")                #         ..
            espacos(1)                 #         ..
            repetir("|__( )_", n)      #         ..
            print("|")                 #         ..
        else:                          #     Se o �ndice da linha de pe�as for par ent�o
            repetir(" |_    ", n + 1)  #         Imprimir padr�o de pe�as da linha par do quebra-cabe�a
            print()                    #         ..
            repetir("  _) _ ", n)      #         ..
            print("  _)")              #         ..
            espacos(1)                 #         ..
            repetir("|__( )_", n)      #         ..
            print("|")                 #         ..
    print()                            # Deixar uma linha em branco no final


# Programa Principal
numero = int(input())
padrao1(numero)
padrao2(numero)
padrao3(numero)
