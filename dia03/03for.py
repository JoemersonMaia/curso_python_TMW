# %%
nome = "joemerson Maia"

for letra in nome:
    print(letra)

# %%

numero = 2
max_numero = 100

for i in range(1,max_numero+1):
    print(numero, "x", i, "=", numero * i)

# %%

for i in range(4, 101):
    if i % 4 == 0:
        print(i)

# %%
altura_total = 0
qauntidade = 4
for i in range(1, qauntidade):
    altura = float(input("informe uma altura:"))
    altura_total += altura
print(altura_total)

# %%
