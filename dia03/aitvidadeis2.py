# %% ##questao 1
numero = float(input("digite um numero para saber se ele é impar ou par:"))

if numero % 2 == 0:
    print("numero é par")
else:
    print("numero impar")

# %% ##questao 2
numero1 = float(input("informe o primeiro numero:"))
numero2 = float(input("informe o primeiro numero:"))

if numero1 > numero2:
    print("o maior é", numero1)
else:
    print("o maior numero é", numero2)

# %% ## questao 3
nota = float(input("informe sua nota:"))

if nota >= 7:
    print("aprovado")
elif 5 <= nota <= 6.9:
    print("recuperacao")
else:
    print("reprovado")
# %% ##questao 4
for i in range(1, 30):

    if i % 2 == 0:
        print(i)
# %%
total = 0
for i in range(1, 101):
    total += i
print(total)


# %%
numero = float(input("informe um numero:"))

for i in range(1, 11):
    resultado = numero * i
    print(resultado)

# %%
senha = input("informe a senha:")

while True:
    senha = input("informe a senha:")
    if senha == "1234":
        print("acessi autorizado")
        break
    else:
        print("""acesso negado
        tente novamente""")
        