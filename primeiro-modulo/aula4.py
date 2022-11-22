# Tipos int e float
# int -> Número inteiro 
# O tipo int representa qualquer número
# Positivo ou negativo, int sem sinal é considerado positivo.

print(11) # int
print(-11) #int
print(0)

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# Positivo ou negativo com ponto flutuante
# float sem sinal é considerado positivo

print(1.1, 10.11, sep=", ")
print(0.0, -1.5, sep=", ")

# A função type mostra o tipo que o Python inferiu ao valor

print(type('Hugo'))
print(type(12), type(0), type(-17))
print(type(1.5), type(-1.1), type(0.0))