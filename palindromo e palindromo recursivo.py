# frase = str(input('\nDigite uma palavra: ')).upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto) -1, -1, -1):
#     inverso += junto[letra]
# if inverso == junto:
#     print('Temos um palíndromo!\n')
# else:
#     print('A palavra não é um palíndromo!')


# def palindromo(palavra):
#     if len(palavra) >1:
#         for x in range(0, int(len(palavra)/2)):
#             if palavra[x] != palavra[(len(palavra) -1) -x]:
#                 return False
#         return True
# print(palindromo('Osso'.upper()))


def is_palindromo_recursivo(palavra):
    if len(palavra) < 2:
        return True
    elif palavra[0] != palavra [-1]:
        return False
    else:
        return is_palindromo_recursivo(palavra[1:len(palavra)-1])

print(is_palindromo_recursivo('Osso'.upper()))
print(is_palindromo_recursivo('Banana'.upper()))
print(is_palindromo_recursivo('Olho'.upper()))
print(is_palindromo_recursivo('Ana'.upper()))
print(is_palindromo_recursivo('Bode'.upper()))