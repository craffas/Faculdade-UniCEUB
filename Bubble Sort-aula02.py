#Boas vindas
print("Olá, seja bem vindo!")
#Variáveis
lista = [7, 2, 12, 4, 8]
ct = 0 #contador de testes.
#Fluxo
while True:
    for ord in range(0, 4):
        ct = ct + 1
        if lista[ord] > lista[ord+1]:
            ordem = lista[ord]
            lista[ord] = lista [ord+1]
            lista[ord+1] = ordem
            print(lista)
            print("Foram feitos", ct, "testes.")