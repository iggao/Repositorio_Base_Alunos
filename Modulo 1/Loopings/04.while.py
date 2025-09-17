# crie um codigo que faça a conversão de moeda do real para dolar e vice-versa

#etapas da resolução:
#1) criar uma variavel chamada cotação
#2) solicitar a usuario a opção de conversao desejada
#3) apresentar o resultado da conversao de moeda
#4) perguntar se ele deseja continuar a conversao

letra = 's'
while letra == 's':
    cotacao = float(input('digite a cotação de dolar: '))
    print('-'*50)
    print(f'escolha a opção','-'*15)
    print('-'*50)

    opcao = int(input('1 - Converter dolar para real | 2 - Conversor real para dolar: '))

    if opcao == 1:
        valor = float(input('digite o valor em dolar a ser convertido para real U$: '))
        resultado = valor * cotacao
        print(f'O valor em reais é: {resultado}')
    elif opcao == 2:
        valor = float(input('digite o valor em real a ser convertido para dolar R$: '))
        resultado = valor / cotacao
        print(f'O valor em dolares é: {resultado}')
    else:
        print('Digita uma parada q seja valida.')
    letra = input('Deseja continuar? (s/n)') .lower()