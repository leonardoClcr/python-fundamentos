"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este número é par ou ímpar. Caso o usuario nao digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input("Digite um número inteiro: ")

# numero_int = int(numero)

# if numero_int % 2 == 0:
#     print('O seu número é par.')
# else:
#     print('Seu número é ímpar.')


"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. Ex.
bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""

# horario = int(input('Digite a hora:'))

# dia = horario >= 0 and horario <= 11
# tarde = horario >= 12 and horario <= 17
# noite = horario >= 18 and horario <= 23

# if dia:
#     print('Bom dia')
# elif tarde:
#     print('Boa tarde')
# else:
#     print('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome_usuario = input('Digite seu nome: ')

if len(nome_usuario) <= 4:
    print('Seu nome é curto')
elif len(nome_usuario) >= 5 and len(nome_usuario) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')