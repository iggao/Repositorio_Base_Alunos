# crie um programa que some todos os numeros impares
# que sao multiplos de 3 e 1 a 30 e apresente o resultado

# etapas para resolução
# 1) criar um for de para captar os numeros impares
# 2) criar uma condicional para checar se o numero é multiplo de 3
# 3) somar os numeros que atende a condicional
# 4) apresentar os resultados

soma = 0 # variavel que ira receber os numeros impares e multiplos de 3
for i in range (1,31,2): 
    if i % 3 == 0: #checagem se os numeros sao multiplos
        soma += i 
print(f'A soma dos números ímpares múltiplos de 3 entre 1 e 30 é: {soma}')