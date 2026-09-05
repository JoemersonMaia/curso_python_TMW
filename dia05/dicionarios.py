# %%
dados_teo = {
            "sobrenome":"Calvo",
            "nome":"teo", 
            "filhos":True,
            "formacao":["estatistica", "bigdata datascience"],
            "cargos":[
                {"nome": "drjr.", "empresa": "tapps"},
                {"nome": "ds pl.", "empresa": "sas"}
            ]
}


print(dados_teo["formacao"][1])
print(dados_teo["cargos"][-1]["empresa"])

# %%
dados_teo["estado civil"] = "casado"

# %%
print(dados_teo)

# %%
print("Chaves:", dados_teo.keys())

print(dados_teo.values())

print("Items:", dados_teo.items())

# %%

for i in dados_teo:
    print(i,"->", dados_teo[i])

# %%

for chave in dados_teo:
    print(i,"->", dados_teo[chave])

# %%
for [chave,valor] in dados_teo.items():
    print(chave, valor)