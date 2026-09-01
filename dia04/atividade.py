# %% 
lista = [2, 1, 2, 3, 1, 3, 4, 1]

numero = float(input("entre com um numero: "))
contador = 0

for i in lista:
    if i == numero:
        contador += 1
print("o numero 1 parece:", contador)