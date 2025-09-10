# 9. Desconto em compras por valor mínimo
# Se o valor da compra for maior que R$150,00, aplique um desconto de
# R$20,00. Caso contrário, não aplique desconto.



valor_da_compra = float(input("Digite o valor da compra: "))

if valor_da_compra > 150:
    desconto = 20
    preço_final = valor_da_compra - desconto
    print(f"Valor com desconto: R${preço_final:.2f}")
else:
    preço_final = valor_da_compra
    print(f"Valor sem desconto: R${preço_final:.2f}")