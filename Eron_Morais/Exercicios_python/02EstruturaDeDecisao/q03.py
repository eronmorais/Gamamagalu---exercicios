#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

resposta = input('Digite M ou F: ')
if resposta == 'M':
    print('Masculino')
else:
    if resposta == 'F':
        print('Feminino')
    else:
        print('Sexo Invalido')        
    
       
