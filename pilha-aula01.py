ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print("Tamanho da fila:", len(fila))
    print("Fila atual:", fila)
    operacao = input("Escolha qual Operação deseja que seja realizada: A, C, ou S.")

# Empilhamento:
    if operacao == "A":
        morto = fila.pop()
        print("Matei o Nº:", morto)
        ultimo = ultimo - 1
    if operacao == "C":
        ultimo = ultimo +1
        fila.append(ultimo)

    elif operacao == "S":
        break
    else:
        print("Digite: A, C ou S.")

