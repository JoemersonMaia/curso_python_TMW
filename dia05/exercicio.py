# %%
banco ={}

nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))

banco[nome] = [idade]

print(banco)

#%%
lista = [120, "Python", 120.01, "aws", False, [10,20]]

print(lista[-1])
print(lista[1])
print(lista[-1][0])

# %%
palavra01 = input("digite uma palavra")
palavra02 = input(" digite uma palavra")

palavramae = palavra01 + palavra02

print(palavramae)

# %%
portifolio = [
    {"maca": 1.50},
    {"banana": 2.75},
    {"uva": 1.90},
    {"pera": 1.25},
    {"laranja": 0.65},
    {"limao": 1.25},
    {"goiabada": 2.15},
    {"abacaxi": 3.20},
    {"Jaca": 5.80},
]

fruta = input("Informe a fruta: ")

for i in portifolio:
    if fruta in i:
        print(i[fruta])
