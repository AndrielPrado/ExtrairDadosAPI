import json
import requests

api_url_base ='http://servicosflex.rpinfo.com.br:9000'
api_login = '100000'
api_password = '123456'
api_token = []

response = requests.post(api_url_base + '/v1.1/auth', json={'usuario': api_login, 'senha' : api_password})
status = response.status_code

if response.ok:
    print("API ONLINE")
    api_token = response.json()
    api_token = api_token['response']
    api_token['token']
else:
    print("ERRO CONEXAO API")
    #print(autenticacao.json())
    print((response.headers))

