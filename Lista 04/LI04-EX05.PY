"""
Exercício 5:
Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. Exemplos: 
•	Dada a entrada ABT-1234 o programa deveria exibir True
•	Dada a entrada JKL9999 o programa deveria exibir False
•	Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 
"""

inp = input("Digite a placa do veículo: ")
inp_up = inp.upper()

if inp_up[0] and inp_up[1] and inp_up[2] >= "A": 
    if inp_up[3] == "-":
        if inp_up[4] and inp_up[5] and inp_up[6] and inp_up[7] >="0":
          print(True)  
        else: print(False)
    else: print(False)
else:
    print(False)

