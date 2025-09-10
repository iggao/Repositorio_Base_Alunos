# Verificação de turno
# Peça ao usuário para digitar "m" para manhã ou qualquer outra tecla
# para tarde. Se for "M", exiba "Bom dia!"", senão exiba "Boa tarde!"".



Cargo_Horario = input("Digite 'M' para manhã ou qualquer outra tecla para tarde: ") .strip() .upper()

if Cargo_Horario == 'M':
    print("Bom dia!")
else:
    print("Boa tarde!")