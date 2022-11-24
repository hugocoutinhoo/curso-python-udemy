"""
faça um programa que peça ao usuário para digitar um número inteiro;
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
numero_digitado = input('Digite um número: ')

try:
    int_numero = int(numero_digitado)
    par_ou_impar = int_numero % 2 == 0
    resultado = 'ímpar'

    if par_ou_impar:
        resultado = 'par'

    print(f'O número digitado é {resultado}')
except:
    print('Você não digitou um número inteiro.') 
"""
faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_do_dia = input('Que horas são? ')

try:
    hora = int(hora_do_dia)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Digite apenas números inteiros.')

"""
faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 letras, escreva "Seu nome é muito grande".
"""

 


