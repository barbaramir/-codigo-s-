"""
Exercício 5:
Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. Exemplo, se o usuário digitar 3141 
seu programa deverá imprimir na tela 3+1+4+1=9.
"""
numeros = input("Digite os números a serem somados: ")
lista = list(map(float, numeros))
soma = sum(lista)

print(soma)