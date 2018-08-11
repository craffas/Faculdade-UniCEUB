# -*- coding: utf-8 -*-
#Abrir arquivo.
arquivo = open('teste.txt', 'r')

#Percorrer um arquivo
for linha in arquivo.readlines():
    print(linha)
#Fechando o arquivo
arquivo.close()