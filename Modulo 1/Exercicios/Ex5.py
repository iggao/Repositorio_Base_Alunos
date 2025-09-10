# Cálculo de gorjeta
# Peça o valor da conta. Se for maior que R$100,00, adicione uma gorjeta
# de 10% e exiba o total a pagar. Caso contrário, adicione uma gorjeta de 5%.



valor_conta = float(input("Digite o valor da conta: R$"))

if valor_conta > 100.00:
  gorjeta = valor_conta * 0.10
  total_a_pagar = valor_conta + gorjeta
  print(f"A gorjeta é de 10%. Total a pagar: R${total_a_pagar:.2f}")
else:
  gorjeta = valor_conta * 0.05
  total_a_pagar = valor_conta + gorjeta
  print(f"A gorjeta é de 5%. Total a pagar: R${total_a_pagar:.2f}")