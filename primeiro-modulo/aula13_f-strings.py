# Introdução a formatação de strings (f-strings)
nome = 'Hugo'
altura = 1.82
peso = 94.4
imc = peso / (altura * altura)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura.'
linha_2 = f'pesa {peso} kg e seu IMC é de: {imc:.2f}'

print(linha_1)
print(linha_2)