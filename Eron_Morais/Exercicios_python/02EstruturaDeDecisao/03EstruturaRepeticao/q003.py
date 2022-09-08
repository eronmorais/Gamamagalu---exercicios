'''Faça um programa que leia e valide as seguintes informações:
- Nome: maior que 3 caracteres;
- Idade: entre 0 e 150;
- Salário: maior que zero;
- Sexo: 'f' ou 'm';
- Estado Civil: 's', 'c', 'v', 'd'
'''

#nome
nome = input('Nome: ')
while len(nome) <= 3:
    print('Inválido')
    nome = input('Nome: ')

print('Válido!')

#Idade
idade = input('Idade: ')
while idade < 0 or idade > 150:
    print('Inválido')
    
