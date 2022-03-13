"""
Exercício 3:
Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}
"""

notas = {"português": 3, "biologia": 5, "matemática": 8, "geografia": 3, "história": 7, "artes": 9, "física": 8, "química": 6}

for nota in sorted(notas, key = notas.get, reverse=True):
    print(nota, notas[nota])
