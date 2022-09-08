#Faça um programa que leia 5 números e informe o maior número

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))
n5 = int(input('Digite um numero: '))

maior = 0
for n in n1, n2, n3, n4, n5:
    if maior > n:
        maior = maior
    else:
        maior = n

print('O maior numero é:', maior)
