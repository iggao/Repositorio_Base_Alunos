# peça ao usuario para digitar uma letra
# e for vogal, informe qual vogal
# se for consoante, verifique se é maiuscula ou minuscula 

# Solicitação de entrada de dados do tipo string (texto)
letra = input("Digite uma letra: ")

if letra.lower() in 'aeiou':  # .lower() tranforma para minuscula
    print(f'Vogal "{letra}"')
else:
    if letra.isupper(): # isupper identifica se a letra esta em maiuscula
        print(f'Consoante maiúscula: {letra}')
    else:
        print(f'Consoante minúscula: {letra}')