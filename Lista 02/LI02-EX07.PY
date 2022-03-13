"""
Exercício 7:
Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.
Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.
"""
#Transformando strings para int: 
strings = ["1", "7", "99", "15"]
str_int = [int(x) for x in strings]

print(str_int)

#Transformando int para string: 
n_int = [1, 7, 99, 15]
int_str = [str(x) for x in n_int]

print(int_str)


