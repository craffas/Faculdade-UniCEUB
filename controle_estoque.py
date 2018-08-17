print('Olá, sejam bem vindos ao meu programa!\n')
#Criando Função para converter arquivo em dicionário.
def file_to_dict(file_name):
    #Open file
    file = open(file_name, 'r')
    #Init a dict
    dict = {}
    #Run a file
    for line in file:
        #Remove \n
        line = line.strip()
        #Split Line
        list = line.split(';')
        #Separate list itens
        product_name = list[0].replace('"', '')
        product_quant = int(list[1])
        product_value = float(list[2])
        #Fill the dict
        dict[product_name] = [product_quant, product_value]
    #Close file
    file.close()
    #Return dict
    return dict

#Use function

estoque = file_to_dict('estoque.txt')
print(estoque)

venda = [["Tomate", 5], ["Batata", 10], ["Feijao", 243]]