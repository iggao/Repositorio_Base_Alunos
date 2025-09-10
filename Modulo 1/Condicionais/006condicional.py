# crie um codigo python que peça o valor da conta. se for maior que R$100,00
# adicione uma gorjeta de 10% e exiba o total a pagar
# caso contrario, adicione uma gorjeta de 5%

# ETAPAS PARA RESOLUÇÃO
# 1 - solicitar o valor da conta para o usuario
# 2 - se a conta for maior que 100 adicionar 10% de gorjeta e apresentar o total a pagar
# 3 - se a conta for menor que 100 adicionar 5% de gprjeta e apresentar o total a pagar

valor_conta = float(input("Digite o valor da conta: R$"))

if valor_conta > 100:
  gorjeta = valor_conta * 0.10
else:
  gorjeta = valor_conta * 0.05

total_a_pagar = valor_conta + gorjeta

print(f"O total a pagar (incluindo a gorjeta) é: R${total_a_pagar:.2f}")