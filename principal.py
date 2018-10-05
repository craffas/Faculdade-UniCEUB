from carro import Carro
from concessionaria import Concessionaria
from comprador import Comprador
from vendedor import Vendedor

#Criando uma Concessionária

v12 = Concessionaria('V12 Motors')
print(v12.get_nome())
print(v12.get_carros())

#Criando um carro:
up = Carro('UP', 'VW', 2018, 20000, 'NOVO', 'JPE-0923')

#Adicionando carro na Concessionaria:
v12.add_carro(up)
print(v12.get_carros()[0].get_modelo())

#Criando segundo carro:
mobi = Carro('MOBI', 'FIAT', 2017, 17000, 'USADO','PPP-0231')

#Adicionando carro na Concessionaria:
v12.add_carro(mobi)
print(v12.get_carros()[1].get_modelo())

#For para imprimir os modelos:

for item in v12.get_carros():
    print(item.get_placa())

#Registrar venda do UP
#Criar um comprador
#Criar um vendedor

sergio = Comprador('Sergio', '045.483.731-36')
rafael = Vendedor('Rafael', '023.433.921-70', '001')
up.registra_venda(sergio, rafael)
print(up.get_venda())