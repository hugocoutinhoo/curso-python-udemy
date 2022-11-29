from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)


numero = input('Em que número eu pensei? ')
int_numero = int(numero)
print('PROCESSANDO...')
sleep(2)

if numero == computador:
    print('Parabéns, você acertou o número!')
else:
    print(f'Eu venci! Você não acertou o número. Pensei no número {computador}')

