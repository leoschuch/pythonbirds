class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(luciano.filhos)

    # é possível criar um atributo em tempo real de execução:
    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)

    # é possível remover um atributo em tempo real de execução:
    del luciano.filhos

    # para visualizar tudo de uma classe:
    print(luciano.__dict__)
