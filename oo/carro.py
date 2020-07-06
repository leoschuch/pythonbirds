""""Você deve ser capaz de escrever uma classe carro que deve possuir 2 atributos compostos por outras classes:
1) motor
2) direção
O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atritubos:
1) Atributo de dado: velocidade
2) Método Acelerar que deverá incrementar a velocidade de uma unidade
3) Métido Frear que deverá decrementar a velocidade em 2 unidades
A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possiveis: Norte, Sul, Leste e Oeste
2) Metodo girar a Direita
3) Metodo girar a Esquerda

Exemplo
>>> # Testando o motor
>>> motor = Motor()
>>> motor.velocidade
0
>>>motor.acelerar()
>>>motor.velocidade
1





"""
# Criação das Constantes
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}

    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        # função que não deixa ficar negativo. O maior valor será o 0:
        self.velocidade = max(0, self.velocidade)
