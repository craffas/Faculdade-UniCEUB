ultimo = 10
fila = list(range(1, ultimo +1))

while True:
    print("Tamanho da fila:", len(fila))
    print("Fila atual:", fila)

    operacao = input("Escolha qual Operação deseja que seja realizada: A, C, ou S.")

#Atendimento:
    if operacao == "A":
        morto = fila.pop(0)
        print ("Matei o Nº:", morto)
        
    if operacao == "C":
        fila.append(ultimo+1)

    elif operacao == "S":
        break
    else:
        print("Digite: A, C ou S.")

