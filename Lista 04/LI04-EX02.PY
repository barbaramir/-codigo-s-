"""
Exercício 2:
Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.
"""

dividendo = int(input("Digite o valor do dividendo: "))

divisor = int(input("Digite o valor do divisor: "))

if dividendo % divisor == 0:
    print(f"O número {dividendo} é divisível por {divisor}.")
else: 
    print(f"O número {dividendo} não é divisível por {divisor}.")