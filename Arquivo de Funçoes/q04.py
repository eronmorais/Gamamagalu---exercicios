#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
#se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def numero(n):
    if n > 0:
        return 'P'
    elif n <= 0:
        return 'N'

n = int(input('Digite um numero: '))
print('Esse numero é:',numero(n))


