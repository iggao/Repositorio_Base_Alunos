# crie um codigo python que peça um numero ao usuario e exiba
# "numero par" se ele for divisivel por 2.

# etapas de resolução;

# 1) solicitar um numero ao usuario
# 2) verificar se o numero é par ou impar
# 3) informar so o numero é par ou impar

numero = float(input("Digite o número par ou impar"))

if numero % 2 == 0:
    print("Seu numero é par. ")
else:
    print("Seu numero é impar. ")
