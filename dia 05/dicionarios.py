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
print(dados_teo["cargos"][-1]["empresa"])]

# %%
dados_teo["estado civil"] = "casado"

# %%
print(dados_teo)