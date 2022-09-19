#Faça um programa, com uma função que necessite de três argumentos, 
#e que forneça a soma desses três argumentos

def numero(n1,n2,n3):
    return n1+n2+n3

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

print(f'A soma desses 3 argumentos é:', numero(n1,n2,n3))