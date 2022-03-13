"""
Exercício 5:
Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20
"""

notas = {'Theodoro': 20, 'Márcia': 50, 'Júnior': 80, 'Helena' : 90}
valores = notas.values()
valor_max = max(valores)
valor_min = min(valores)

for key,value in notas.items():
    if value == valor_max:
        print(f"Nota máxima -> {key}: {value}.")
    
    if value == valor_min: 
        print(f"Nota mínima -> {key}: {value}.")
