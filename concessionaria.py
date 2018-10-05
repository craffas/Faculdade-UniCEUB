#Classe Concessionária:
class Concessionaria:
    #Método Construtor:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    #Métodos Acessores:
    def get_nome(self):
        return self.nome

    def get_carros(self):
        return self.carros

    #Método para adicionar uum carro:
    def add_carro(self, carro):
        self.carros.append(carro)