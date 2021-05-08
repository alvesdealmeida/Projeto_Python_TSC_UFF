# APX3 - Questão 2
# Aluno: Sebastiao Alves   Polo: Sao Fidelis

# Subprogramas

def quebrar_expressao(expressao):
    OPERADORES = ['*', '/', '+', '-']   # Os quatro operadores estão odenados de modo que o índice menor significa prioridade maior
    # Buscar pelo operador de menor prioridade, tomando o cuidado de ignorar o conteúdo dos parênteses, pois esse conteúdo tem maior prioridade na avaliação
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
    # Caso nenhum operador tenha sido encontrado fora de parênteses então a única explicação é que a expressão toda está envolta por parênteses
    if pos_operador == -1:
        return quebrar_expressao(expressao[1:-1])  # Nesse caso, é preciso "descascar" os parenteses da expressão. Faremos isso com uma chamada recusiva desta função, ignorando o primeiro e último elementos da expressão dada como argumento de entrada
    else:
        return expressao[:pos_operador], expressao[pos_operador+1:], expressao[pos_operador] # Caso contrário, retornar as subexpressões que são os operandos e o próprio operador


def resolver_expressao(expressao):
    # Essa função recursiva espera como entrada uma lista de strings
    if len(expressao) == 1:
        # Caso a expressão possua apenas um elemento, então ela obrigatoriamente é um valor inteiro que representa o próprio resultado
        return int(expressao[0])
    else:
        # Caso contrário é preciso identificar a operação com menor prioridade e avaliar cada um de seus operandos recursivamete
        esquerda, direita, operador = quebrar_expressao(expressao)
        esquerda = resolver_expressao(esquerda)  # Chamada recursiva para avaliar a subexpressão à esquerda do operador
        direita = resolver_expressao(direita)  # Chamada recursiva para avaliar a subexpressão à direita do operador
        if operador == '+':
            return esquerda + direita  # Avaliar adição
        elif operador == '-':
            return esquerda - direita  # Avaliar subtração
        elif operador == '*':
            return esquerda * direita  # Avaliar multiplicação
        else:
            return esquerda / direita  # Avaliar divisão


# Programa Principal
linha = input()
while linha != '0':
    resultado = resolver_expressao(linha.split())
    print('%1.2f' % resultado)
    linha = input()

