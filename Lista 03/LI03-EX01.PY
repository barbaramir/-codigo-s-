"""
Exercício 1:
Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
Faça um programa que responda as seguintes perguntas:
"""

alunos_ingles = {"João Alves dos Santos","Maria Magalhães", "Antônio da Silva Ferreira", "José Júnior Jarbas", "Henrique da Silva Sauro", "Joaquina Ferreira da Silva", "Fabiana Aparecida Bianco", "Marrone Gutierres", "Carlos Magno Farad", "Antônio da Silva Júnior Amaral"}

alunos_frances = {"João Alves dos Santos", "Antônio da Silva Ferreira", "Fernanda Abdala Mohamed", "Abner Mignon Alib", "Alisson Figueiredo", "Henrique da Silva Sauro", "Maria Magalhães", "Marrone Gutierres", "Joaquina Ferreira da Silva"}

#1.	Quantos alunos estão matriculados na escola, no total?

lista_alunos = alunos_ingles.union(alunos_frances)
total_alunos = len(lista_alunos)

print(f"O número de alunos matriculados na escola é {total_alunos}.")

#2.	Quantos e quais estão matriculados APENAS em INGLES?
apenas_ingles = (alunos_ingles) - (alunos_frances)
qtde_apenas_ingles = len(apenas_ingles)

print(f"{qtde_apenas_ingles} alunos estão matriculados apenas em Inglês. São eles: {apenas_ingles}.")

#3.	Quantos e quais estão matriculados APENAS em FRANCES?
apenas_frances = (alunos_frances) - (alunos_ingles)
qtde_apenas_frances = len(apenas_frances)

print(f"{qtde_apenas_frances} alunos estão matriculados apenas em Francês. São eles: {apenas_frances}.")

#4.	Quantos e quais estão matriculados EM AMBOS os cursos?
ingles_e_frances = (alunos_ingles) & (alunos_frances)
qtde_ingles_e_frances = len(ingles_e_frances)

print(f"{qtde_ingles_e_frances} alunos estão matriculados em ambos os cursos. São eles: {ingles_e_frances}.")

#5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?
somente_um_curso = (lista_alunos) - (ingles_e_frances)
qtde_somente_um_curso = len(somente_um_curso)

print(f"{qtde_somente_um_curso} alunos estão matriculados em apenas um curso.")