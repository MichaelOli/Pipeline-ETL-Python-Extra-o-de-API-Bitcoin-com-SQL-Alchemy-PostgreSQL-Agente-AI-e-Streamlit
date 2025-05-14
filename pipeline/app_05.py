import requests
from tinydb import TinyDB
from datetime import datetime
import time



def extrair():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return(response.json())

def transformar(dados):
    valor = dados['data']['amount'],
    cripto = dados['data']['base'],
    moeda = dados['data']['currency']
    dados_tratados = {
        "valor": valor,
        "criptomoeda": cripto,
        "moeda": moeda,
        "timestamp": datetime.now().isoformat()

    }
    return dados_tratados

def load(dados_tratados):
    db = TinyDB('db.json')
    db.insert(dados_tratados)
    print("Dados salvos com sucesso")

if __name__ == "__main__":
    while True:
        dados = extrair()
        dados_tratados = transformar(dados)
        load(dados_tratados)
        print(dados_tratados)
        time.sleep(5)
