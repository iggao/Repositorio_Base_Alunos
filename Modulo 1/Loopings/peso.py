# crie um programa que leia o peso de 5 pessoas.
# no final, mostre qual foi o maior e o menor peso lido.

# etapas para resolução:
#1) crie uma lista vazia para receber os pesos
#2) crie um for para receber os pesos das 5 pessoas
#3) adicione os pesos recebidos a lista
#4) ultilize a função max() ou ordene a lista e busque o primeiro e o ultimo elemento
#5) apresente os resultados:

pesos = []
for i in range(4):
    peso = float(input(f'digite o peso da {i+1} pessoa em KG: '))
    pesos.append(peso)
print(f'o maior peso é: {max(pesos)}')
print(f'o menor peso é: {min(pesos)}')