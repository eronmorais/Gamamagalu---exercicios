#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
#Depois modifique o programa para que ele mostre os números um ao lado do outro.


ano = 1
# enquanto ano <= 20, print(ano)
while ano <= 20:
    print(ano)
    ano = ano + 1

print('Modificando o programa')    

for ano in range(1,21):
    #ano = 1
    print(ano, end=' ')

print()
print('Fim do programa!')