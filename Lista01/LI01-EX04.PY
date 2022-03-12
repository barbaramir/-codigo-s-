"""
Exercício 4:
Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.
"""

peso_01 = float(input("Digite o seu peso (kg): "))
altura_01 = float(input("Digite a sua altura (m): "))

imc = peso_01 / (altura_01**2)

print(f"O seu IMC é {imc:.2f}")