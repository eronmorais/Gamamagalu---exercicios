#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

resposta = input('Digite M ou F: ')
if resposta == 'M' or resposta == 'm':
    print('Masculino')
elif resposta.lower() == 'f':
    print('Feminino')
else:
    print('Sexo Invalido')        
    