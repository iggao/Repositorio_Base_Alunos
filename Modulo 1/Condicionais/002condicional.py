# crie um codigo que receba 3 notas, calcule a media e informe se o aluno esta aprovado, em recuperação ou reprovado

# OBS: Aprovado media >= 7
 #Recuperação > 4
# Reprovado media < 4

# Etapas
# 1) Solicitar as notas ao usuário
Notinha_do_Mano1 = float(input("Digite a primeira nota: "))
Notinha_do_Mano2 = float(input("Digite a segunda nota: "))
Notinha_do_Mano3 = float(input("Digite a terceira nota: "))
# 2) Calcular a média
media = (Notinha_do_Mano1 + Notinha_do_Mano2 + Notinha_do_Mano3) /3
# 3) Checar a condição do aluno
if media >=7:
    print(f"O aluno tem média {media:.2f} e está aprovado.")
elif 5 <= media < 7:
    print(f"O aluno teve média {media:.2f} e está em recuperação.")
else:
    print(f"O aluno teve média {media:.2f} e está reprovado.")
# 40 Informar o resultado

