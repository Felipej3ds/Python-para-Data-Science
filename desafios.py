'''
Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
'''

lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

for sublista in lista_de_listas:
    soma = sum(sublista)
    print(soma)

'''
Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
'''

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
terceiros_elementos = [tupla[2] for tupla in lista_de_tuplas]
print(terceiros_elementos)

'''
A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

'''
lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
lista_de_tuplas = [(i, nome) for i, nome in enumerate(lista)]
print(lista_de_tuplas)

'''
Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
'''

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
valores_apartamento = [valor for tipo, valor in aluguel if tipo == 'Apartamento']
print(valores_apartamento)

'''

Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

Glicose igual ou inferior a 70: 'Hipoglicemia'
Glicose entre 70 a 99: 'Normal'
Glicose entre 100 e 125: 'Alterada'
Glicose superior a 125: 'Diabetes'
A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
'''

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

glicemias_rotuladas = [ (rotulo, valor) for valor in glicemia if (rotulo := 'Hipoglicemia' if valor <= 70 else
                        'Normal' if 70 < valor <= 99 else
                        'Alterada' if 100 <= valor <= 125 else
                        'Diabetes')]
print(glicemias_rotuladas) 