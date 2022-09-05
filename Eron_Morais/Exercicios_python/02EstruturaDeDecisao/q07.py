#Faça um Programa que leia três números e mostre o maior e o menor deles

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

#Achando maior numero
maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro


menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < segundo):
    menor = terceiro
    
    print('Maior numero: ',maior)
    print('Menor numero: ', menor)