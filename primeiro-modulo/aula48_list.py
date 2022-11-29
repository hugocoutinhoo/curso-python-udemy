"""
Listas em Python - array no JavaScript
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, Ler, Alterar, Apagar = lista[i (CRUD)]
"""
#        0   1   2   3   4   5
# lista = [10, 20, 30, 40]
"""
DELETANDO ELEMENTOS NA LISTA
lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2]) """

""" 
ADICIONANDO ELEMENTOS NA LISTA
lista = [10, 20, 30, 40]
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido: ', ultimo_valor) """

""" 
INSERINDO ITENS EM QUALQUER ÍNDICE DA LISTA 
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(0, 5)
print(lista) """

""" 
CONCATENANDO E ESTENDENDO LISTAS
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a) """

"""
CUIDADOS com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""