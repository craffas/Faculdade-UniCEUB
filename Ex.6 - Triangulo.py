def is_triangle(n1,n2,n3):
    if n1 > n2+n3:
        return False
    if n2 > n1+n3:
        return False
    if n3 > n2+n1:
        return False
    else:
        return True
g1 = int(input('Digite o comprimento do primeiro graveto: '))
g2 = int(input('Digite o comprimento do segundo graveto: '))
g3 = int(input('Digite o comprimento do terceiro graveto: '))

print('Resposta: ', is_triangle(g1, g2, g3))