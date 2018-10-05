#CRIANDO A CLASSE CARRO:
class Carro:
    #Método Construtor:
    def __init__(self, modelo, estado, ano, preco, marca, placa):
        #Atributos de objetos ou instância:
        self.modelo = modelo
        self.estado = estado
        self.ano = ano
        self.preco = preco
        self.marca = marca
        self.placa = placa
        self.comprador = None
        self.vendedor = None

    #Método de acesso:
    def get_modelo(self):
        return self.modelo

    #Método para registrar venda:
    def registra_venda(self, comprador, vendedor):
        self.comprador = comprador
        self.vendedor = vendedor

    def get_placa(self):
        return self.placa

    def get_venda(self):
        return 'Comprador: ' + self.comprador.get_nome() + '/ Vendedor: ' +\
               self.vendedor.get_nome()






