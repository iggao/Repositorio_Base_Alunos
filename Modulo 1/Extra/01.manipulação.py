# criar arquivo, recebendo informação do usuario

# solicitação de entrada
nome = input('Digite seu nome completo: ')
email = input('Digite seu email: ')

# Criar arquivo
arquivo = open('pessoa.txt','a',encoding='utf-8') # estamos criando o arquivo
# armazenando na variavel arquivo, o modo 'a' escreve sempre no final,
# encording utf-8 é para ultilizar o conjunto de caracteres que engloba
# a lingua portuguesa
arquivo.write(nome + '|' + email + '\n' ) #.write é para escrever e o
# \n é para pular linha
arquivo.close() # .close é para fechar o arquivo