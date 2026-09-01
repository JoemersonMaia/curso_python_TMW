# %%
count =0
deposito_total = 0

while True:
    deposito = input("digite quanto deseja depositar:")
    if deposito == "":
            break
    
    deposito_total += float(deposito)

print("deposito total:", deposito_total)


# %%