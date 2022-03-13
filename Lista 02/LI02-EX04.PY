"""
Exercício 4:
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: Exemplo de saída:
>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho
"""

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

temp = []

for x in meses:
    temp.append(float(input(f"Digite a média de temperatura do mês de {x}: ")))

media_temp = sum(temp) / len(temp)

print(f"A temperatura média anual foi de {media_temp}º.")

for y in temp:
    if y > media_temp:
        print(f"O mês de {meses[temp.index(y)]} esteve acima da média com {y}º.")

