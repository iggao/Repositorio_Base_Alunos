# Criar um código que consuma uma API de clima e informe
# a temperatura e a descrição do clima em um lugar especifico


# Etapa
# 1. Definir a chave de API e o link da requisição
import requests

api_key = '2a1ac38a32354cb7b19133643251408'
cidade = input('Digite o nome da cidade: ') .strip()
url= f'https://api.weatherapi.com/v1/current.json'

# 2. Parametros da requisição
parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt'
}

# 3. fazer a requisição
resposta = requests.get(url, params=parametros)

# 4. Verificar se a requisição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json()  # convertendo a resposta JSON em um dicionário Python
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'Temperatura na cidade {cidade} é {temperatura}°C.')
    print(f'Descrição: {descricao}')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)
