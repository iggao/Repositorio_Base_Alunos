# adicionar uma nova frase no meu arquivo

# caso eu queira adicionar uma nova frase no arquivo ja criado
# ultilizamos o modo 'a' para nao subescrever no conteudo existente

with open('mensagem.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('\nAprendendo a manipular arquivos.')