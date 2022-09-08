# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até (enquanto) que o usuário informe um valor válido.
# enquanto -> while

nota = int(input('Nota: '))
while not (nota >= 0 and nota <= 10):
    print('Inválido')
    nota= int(input('Nota: '))
print('Nota válida!')
    
