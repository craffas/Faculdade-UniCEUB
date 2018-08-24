def proibida (frase):
    letras_proibidas = ['o', 'd', 't']
    for x in letras_proibidas:
        print('Total de letras', [x], 'é:', frase.count(x))
proibida('Hoje está chovendo desde muito cedo’')


def proibida (frase):
    letras_proibidas = ['m', 'p', 'q', 'a']
    print('-' * 20)
    for x in letras_proibidas:
        print('Total de letras', [x], 'é:',  frase.count(x))
proibida('Amanhã vai ser outro dia’')

