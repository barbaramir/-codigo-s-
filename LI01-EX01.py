"""
Lista de exercícios
Tema: tipos numéricos
Exercício 1:
Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
"""

A = float(input("Digite o primeiro número: "))
B = float(input("Digite o segundo número: "))

#A soma de A e B
print(int(A+B))

#A diferença quando se subtrai B de A;
print(B-A)

#O produto (multiplicação) entre A e B;
print(A*B)

#O quociente (parte inteira da divisão) quando se divide A por B;
print(A//B)

#O resto da divisão entre A e B;
print(A%B)

#O resultado de log10 de A;
from math import log10
print(log10(A))

#O resultado de A elevado a B
print(A**B)

