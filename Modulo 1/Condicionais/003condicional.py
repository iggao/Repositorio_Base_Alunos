# Criar um codigo python que indique se a temperatura está agradavel ou não
# condições:
# temperatura >= 30° informar que esta muito quente
# temperatura >= 20° informar que esta agradavel
# temperatura >= 10° informar que esta muito frio
# temperaura abaixo dos 10° esta muito frio

# etapas para a resolução:
# 1) solicitar a temperatura para o usuario
# 2)verificar a condicional
# 3) imprimir a resposta segundo a temperatura

temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura >= 30:
    print("Está muito quente!")
elif temperatura >= 20:
    print("Está agradáve!")
elif temperatura >= 10:
    print("Está frio!")
else:
    print("Está muito frio!")