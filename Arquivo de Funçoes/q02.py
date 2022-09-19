'''Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''

numero = int(input('Digite um numero: '))
linha = ""
for i in range(1,numero + 1):
    linha = linha + str(i) + ' '
    print(linha)



