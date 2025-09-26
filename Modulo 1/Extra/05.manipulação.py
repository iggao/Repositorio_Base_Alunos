# ler e imprimir o conteudo do arquivo mensagem.txt

with open('mensagem.txt','r', encoding='utf-8') as arquivo:
    print(arquivo.read()) # aq estamos imprimindo o que o arquivo leu
# e neste caso, não estamos ar...