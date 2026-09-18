# %%
import requests

cep = input("entre com o CEP: ")

ceps = ["01519000", "13329120", "44230000"]

url ="https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url.format(cep=cep))

if resposta.status_code == 200:
    dados = resposta.json()

for chave, valor in dados.items():
    print(chave, "->", valor)