#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []

for i in range(5):
    numero = int(input('Digite o numero: '))
    vetor.append(numero)
print(vetor)