ultimo = 10
fila = 0
nome = []
sexo = []
idade = []
esp = []

while True:
    print("\nTamanho da fila:", len(nome))
    print('\nFila de Nomes:', nome)
    print('Fila de Sexo:', sexo)
    print('Fila de Idade:', idade)
    print('Fila de Especialidade:', esp)

    operacao = input("\nEscolha qual Operação deseja que seja realizada: A, C, ou S.")

    # Atendimento:
    if operacao == "A":
        morto_nome = nome.pop(0)
        morto_sexo = sexo.pop(0)
        morto_idade = idade.pop(0)
        morto_esp = esp.pop(0)
        print("Matei o Nome:", morto_nome + "\nMatei o Sexo:", morto_sexo + "\nMatei a Idade:", morto_idade + "\nMatei a Especialidade:", morto_esp)

    if operacao == "C":
        name = input("\nDigite seu nome: ")
        nome.append(name)

        sexy = input("Digite seu sexo: ")
        sexo.append(sexy)

        age = input("Digite sua idade: ")
        idade.append(age)

        espc = input("Digite a especialidade: ")
        esp.append(espc)

    elif operacao == "S":
        break
    else:
        print("Digite: A, C ou S.")
