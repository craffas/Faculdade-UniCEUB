def soma_elementos(lista):
    listaum = lista
    return listaum

listaum = soma_elementos([[1, 2], [23, 5, 9, 10], [1, 8, 16]])
lista_dois = listaum[1]
lista_tres = listaum[2]
listaum = listaum[0]

soma = 0
for i in (listaum, lista_dois, lista_tres):
    soma += listaum[0] + lista_dois[0] + lista_tres[0]
print('\nA soma de todos os elementos da lista é:', soma)
