# AD1 - Quest�o 5
# Aluno: Sebastiao Alves - Polo: Sao Fidelis

# Subprograma
def jogar(n):
    # Verificar se o jogo acabou em derrota por n�o haver barras
    if n <= 0:
        return False  # Parar o jogo e reportar derrota
    # Verificar se o jogo acabou em vit�ria por haver exatamento 42 barras
    if n == 42:
        return True  # Parar o jogo e reportar vit�ria
    # Se o jogo continua e � possivel aplicar a Regra 1 ent�o aplicar a Regra 1
    if n % 2 == 0:
        venci = jogar(n // 2)
        if venci:
            return True  # Parar o jogo e reportar vit�ria obtida na chamada recursiva
    # Se o jogo continua e � possivel aplicar a Regra 2 ent�o aplicar a Regra 2
    if n % 3 == 0 or n % 4 == 0:
        m = ((n % 100) // 10) * (n % 10)
        if m != 0:  # Evitar chamada que levaria � recurs�o infinita, pois para M == 0 temos N - M == N
            venci = jogar(n - m)
            if venci:
                return True  # Parar o jogo e reportar vit�ria obtida na chamada recursiva
    # Se o jogo continua e � possivel aplicar a Regra 3 ent�o aplicar a Regra 3
    if n % 5 == 0:
        venci = jogar(n - 42)
        if venci:
            return True  # Parar o jogo e reportar vit�ria obtida na chamada recursiva
    # Se a execu��o chegou at� aqui ent�o o jogo foi perdido, pois chegar a esse ponto significa que o 42 n�o foi atingido por nenhuma chamada recursiva que partiu da aplica��o recursiva das regras sobre o N atual.
    return False  # Parar o jogo e reportar derrota


# Programa Principal
numero_dado = int(input())
if jogar(numero_dado):
    print("Venci")
else:
    print("Perdi")
