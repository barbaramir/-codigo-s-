"""
Exercício 3:
Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
>>> O maior elemento é 8 e está na posição 3
>>> O menor elemento é 3 e está na posição 4
Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.
"""

lista = [2, 8, 5, 9, 1, 6]

maior_num = max(lista)
maior_pos = lista.index(maior_num)

print(f"O maior número da sequência é {maior_num} e está na posição {maior_pos}.")

menor_num = min(lista)
menor_pos = lista.index(menor_num)

print(f"O menor número da sequência é {menor_num} e está na posição {menor_pos}.")
