#criar uma classe conta, com os atributos(numero,agencia,tipo,saldo) e metodos(depósito, saque, transferencia e consultar saldo)

class Conta:
    #Método Construtor:
    def __init__(self, numero, agencia, tipo):
        #Atributos de objetos ou instância:
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo #1 == CC 2 == CP
        self.saldo = 0 #Saldo inicial padrão

    #Metodo para consultar saldo:
    def consultar_saldo(self):
        return self.saldo

    #Método depositar valores:
    def depositar_valores(self, valor):
        self.saldo += valor

    #Método para transferir valores:
    def transferir_valores(self, conta_destino, valor):
        #Verificando se temos saldo:
        if self.consultar_saldo() >= valor:
            self.saldo -= valor
            conta_destino.receber_transferencia(valor)

    #Método para receber transferências:
    def receber_transferencia(self, valor):
        self.saldo += valor

#Desenvolvendo Sistema
conta1 = Conta('123', '456', 1)
conta1.depositar_valores(1000)

conta2 = Conta('999', '999', 2)
conta2.depositar_valores(300)

conta1.transferir_valores(conta2, 100)
print(f'O saldo da conta um é: {conta1.consultar_saldo()}')
print(f'O saldo da conta dois é: {conta2.consultar_saldo()}')
