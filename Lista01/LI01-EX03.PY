"""
Exercício 3:
No exercício acima você calculou a área de um triângulo a partir da sua base e altura. Faça um programa que receba os 3 
lados de um triângulo – s1, s2 e s3 – e calcule sua área. Compare a resposta com o exercício acima, dada das mesmas entradas. 
Os resultados devem ser idênticos.
"""

lado01 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado02 = float(input("Digite o valor do segundo lado do triângulo: "))
lado03 = float(input("Digite o valor do terceiro lado do triângulo: "))

soma_lados = (lado01 + lado02 + lado03)/2

area_tri = (soma_lados*(soma_lados-lado01)*(soma_lados-lado02)*(soma_lados-lado03))**(1/2)

print(f"A área do triângulo é {area_tri}")