"""
Iterável -> str, range, etc. método: (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'
iterator = iter(texto)

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break