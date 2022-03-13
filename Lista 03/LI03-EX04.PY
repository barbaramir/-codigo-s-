"""
Exercício 4:
Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6}
"""

dic = {1: "vermelho", 2: "azul", 3: "marrom", 4: "amarelo", 5: "verde"}
for key,value in dic.items(): 
    comp = len(value)
    dic[key] = comp

print(dic)