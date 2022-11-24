"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Hugo Luiz'
# outra_variavel = f'{string[:5]}ABC{string[4:]}'
# string[5] = 'ABC' # vai dar erro, pois o str é imutável
# print(string[5])
# print(outra_variavel)
print(string.zfill(100))