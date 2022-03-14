"""
Exercício 3:
A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns
Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. Se o valor for um dos que estão na tabela, o programa deve 
retornar aquele barulho. Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado 
está. Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo. 
"""

ref = {"Britadeira": 130, "Cortador de grama": 106, "Despertador": 70, "Cômodo em silêncio": 40}
som_ref = list(ref.keys())
vlr_ref = list(ref.values())
ruido_max = max(vlr_ref) 
ruido_min = min(vlr_ref)

nivel = int(input("Digite o valor de nível sonoro em decibéis: "))

if nivel > ruido_max:
    print(f"O valor de ruído informado é maior que o ruído máximo de referência!")

elif vlr_ref[0] > nivel > vlr_ref[1]: 
    print(f"O valor de ruído informado está entre {som_ref[0]}-> {vlr_ref[0]}(db) e {som_ref[1]}-> {vlr_ref[1]}(db).")

elif vlr_ref[1] > nivel > vlr_ref[2]: 
    print(f"O valor de ruído informado está entre {som_ref[1]}-> {vlr_ref[1]}(db) e {som_ref[2]}-> {vlr_ref[2]}(db).")

elif vlr_ref[2] > nivel > vlr_ref[3]: 
    print(f"O valor de ruído informado está entre {som_ref[2]}-> {vlr_ref[2]}(db) e {som_ref[3]}-> {vlr_ref[3]}(db).")

else: 
    print(f"O valor de ruído informado é menor que o ruído minímo de referência!")  






