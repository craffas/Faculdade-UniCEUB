disc = [
    [{'nome': 'LTP1'},
     {'Joao': 2.5, 'Maria': 8.9, 'José': 6.7}],

    [{'nome': 'Compiladores'},
     {'Joao': 6.2, 'Maria': 10, 'José': 2.1, 'Mario': 6.9}],

    [{'nome': 'Tópicos Especiais'},
     {'Maria': 9.2, 'José': 9.1, 'Mario': 5.5}],
    ]

print('\nOlá, seja bem vindo, vamos calcular a nota do aluno! \n')
aluno = input('Digite o nome do aluno que deseja obter a nota: ')

for materia in disc:
#Recuperando o discionário de alunos da disciplina.
    dict_alunos = materia[1]
#Verificar se o aluno está na disciplina.
    if aluno in dict_alunos.keys():
        #Recuperar o nome da disciplina.
        nome_disciplina = materia[0]['nome']
        #Recuperando a nota do aluno;
        nota = materia[1][aluno]
        print('\nDisciplina: {}'.format(nome_disciplina))

        #Obter a menção com base na nota.
        if nota>= 9:
            mencao = 'SS'
        elif nota >= 7:
            mencao = 'MS'
        elif nota >= 5:
            mencao = 'MM'
        elif nota >= 3:
            mencao = 'MI'
        elif nota >= 0:
            mencao = 'II'
        else:
            mencao = 'SR'
        print('A menção final do aluno é: {} = {}\n'.format(nota, mencao))
    if aluno not in dict_alunos.keys():
        print('-'*65)
        print('\nO aluno {} não se encontra cadastrado nas seguintes disciplinas:\n1- {}.'.format(aluno, nome_disciplina))