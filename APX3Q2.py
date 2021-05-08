# APX3 - Quest�o 2
# Aluno: Sebastiao Alves   Polo: Sao Fidelis

# Subprogramas

def quebrar_expressao(expressao):
    OPERADORES = ['*', '/', '+', '-']   # Os quatro operadores est�o odenados de modo que o �ndice menor significa prioridade maior
    # Buscar pelo operador de menor prioridade, tomando o cuidado de ignorar o conte�do dos par�nteses, pois esse conte�do tem maior prioridade na avalia��o
    pos_operador = -1
    parenteses_abertos = 0
    for pos in range(len(expressao)):
        if expressao[pos] == '(':
            parenteses_abertos += 1
        elif expressao[pos] == ')':
            parenteses_abertos -= 1
        elif parenteses_abertos == 0 and expressao[pos] in OPERADORES:
            if pos_operador == -1 or OPERADORES.index(expressao[pos]) >= OPERADORES.index(expressao[pos_operador]):
                pos_operador = pos
    # Caso nenhum operador tenha sido encontrado fora de par�nteses ent�o a �nica explica��o � que a express�o toda est� envolta por par�nteses
    if pos_operador == -1:
        return quebrar_expressao(expressao[1:-1])  # Nesse caso, � preciso "descascar" os parenteses da express�o. Faremos isso com uma chamada recusiva desta fun��o, ignorando o primeiro e �ltimo elementos da express�o dada como argumento de entrada
    else:
        return expressao[:pos_operador], expressao[pos_operador+1:], expressao[pos_operador] # Caso contr�rio, retornar as subexpress�es que s�o os operandos e o pr�prio operador


def resolver_expressao(expressao):
    # Essa fun��o recursiva espera como entrada uma lista de strings
    if len(expressao) == 1:
        # Caso a express�o possua apenas um elemento, ent�o ela obrigatoriamente � um valor inteiro que representa o pr�prio resultado
        return int(expressao[0])
    else:
        # Caso contr�rio � preciso identificar a opera��o com menor prioridade e avaliar cada um de seus operandos recursivamete
        esquerda, direita, operador = quebrar_expressao(expressao)
        esquerda = resolver_expressao(esquerda)  # Chamada recursiva para avaliar a subexpress�o � esquerda do operador
        direita = resolver_expressao(direita)  # Chamada recursiva para avaliar a subexpress�o � direita do operador
        if operador == '+':
            return esquerda + direita  # Avaliar adi��o
        elif operador == '-':
            return esquerda - direita  # Avaliar subtra��o
        elif operador == '*':
            return esquerda * direita  # Avaliar multiplica��o
        else:
            return esquerda / direita  # Avaliar divis�o


# Programa Principal
linha = input()
while linha != '0':
    resultado = resolver_expressao(linha.split())
    print('%1.2f' % resultado)
    linha = input()

