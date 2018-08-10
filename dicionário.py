estoque = {'Alface': [1000, 2.50],
          "Tomate": [456, 8.90],
          "Batata": [1673, 1.20],
          "Feijão": [2345, 6.75]}

vendas = [["Tomate", 5], ["Feijão", 10], ["Alface", 4]]

valor_total = 0
quantidade_total = 0
#Valor total da Venda
for venda in vendas:
    #Pegando o Produto
    produto = venda [0]
    #Pegando a Quantidade
    quantidade = venda[1]
    #Pegando o valor
    lista_produto = estoque[produto]
    valor = lista_produto[1]
    #Calculando o valor total
    valor_total = valor_total + (quantidade * valor)
    quantidade_total = lista_produto[0] - quantidade
    print('\nValor: R${:.2f} \nItem: {}\nDisponível no estoque: {} unidades.'.format(valor, produto, quantidade_total))
print('\nO valor total das vendas de alimentos é: R${:.2f}\n'.format(valor_total))

