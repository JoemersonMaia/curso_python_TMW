# %%
garrafa = input("gostaria de uma agua c/gas ou s/gas?")

conta = 0
if garrafa == "s":
    conta = 1,5

elif garrafa== "c":
    conta =2,5

if conta == 0:
    print("entre com a opcao coreta, por favor")
else:
    print("sua conta ficou:", conta)


# %%
garrafa = input("gostaria de uma agua c/gas ou s/gas?")

valor_item = 0
if garrafa == "s":
    valor_item = 1.5
elif garrafa== "c":
    valor_item =2.5


if valor_item == 0:
    print("entre com a opcao correta")      
else:
    quantidade = int(input("quantas garrafas seraio?"))

    total = valor_item * quantidade

    print(f"{quantidade} +  aguas ficou + {total}")

# %%
