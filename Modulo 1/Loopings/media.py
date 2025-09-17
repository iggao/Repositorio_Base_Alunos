# solicite ao usuario 4 notas.
# calcule a media
# informe se o aluno esta aprovado (media=7), recuperação(5<media<7)ou reprovado.
# apresente as notas que o aluno tirou, a media e o status de sua situação

# lista
# for
# if/elif/else

notas = [] 
soma = 0
for i in range (4):
    nota = float(input(f'digite a {i+1}ª nota: '))
    notas.append(nota) 
    soma += nota 
media = soma / 4
print(f'as notas do aluno foram: {notas}')
print(f'a média do aluno é: {media:.1f}')
if media >= 7:
    print('aluno aprovado')
elif 5 <= media < 7:
    print('aluno em recuperação')
else:
    print('aluno reprovado')

#notas [] | # criei uma lista vazia que irá armazenar as notas recebidas
#for i in range(4):  # faz a pergunta 4 vezes
#nota = float(input(f'Informe a nota da prova (i+1}; '))
#if nota > 0:  # só aceita nota positivas
#notas.append(nota) # notas.append(nota) adiciona un elemento no final da lista else: # se a nota for negativa apresenta o print
#print('Valor inválido.')
#print(f'Suas notas são: {notas}')   # linha opcional
#media=sum(notas)/len (notas)  # a função sun(notas) soma todas as notas da lista # a função len(notas) informa o tamanho da lista nostas
#if media >=7: # se a media for maior que 7
#print(f'Suas notas foram{notas), sua (media:.2f) e você está aprovado. ') elif 5 <- media < 7; # se a media for de 5 a 6.99
#print(f'Suas notas foram{notas), sua (media:.2f) e você está de recuperação. ') else: # notas abaixo de 5, ou seja, de 4.99 para baixo
#print(f'Suas notas foram{notas), sua (media:.2f) e você está reprovado. ')
# {media:.2f} formata a média para o resultado ter apenas 2 casas decimais