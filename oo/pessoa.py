class Pessoa:
    olhos = 2 # atributo default ou de classe, que não irá consumir memória e ele serve para toda a classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    # método decorator abaixo:
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':

    luciano = Pessoa(nome='Luciano')
    print(Pessoa.cumprimentar(luciano))

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

    # exemplo do método estático @metodo_estático
    print(Pessoa.metodo_estatico())
    # outro exemplo @
    print(Pessoa.nome_e_atributos_de_classe())
