# %%
# %%
vendas = [
    ["Carlos", 850],
    ["Ana", 1200],
    ["Carlos", 450],
    ["Marcos", 2100],
    ["Ana", 750],
    ["João", 320],
    ["Marcos", 980],
    ["João", 1500]
]


for i in range(len(estoque)):
    produto = estoque[i][0]
    

opcao = input("""
1 - Ver todas as vendas
2 - Ver vendas acima de determinado valor
3 - Calcular faturamento total
4 - Identificar vendedor com maior faturamento
5 - Ver quantidade de vendas por vendedor
6 - Classificar desempenho dos vendedores
7 - Sair
""")

if opcao == "1":
    for venda in vendas:
        print(venda)
elif opcao == "2":
    acima_vendas = int(input("informe o valor"))
    for i in range(len(vendas)):
        vendedor = vendas[i][0]
        numero_vendas = vendas[i][1]
        if numero_vendas > acima_vendas:
            print(vendedor)

elif opcao == "3":
    for i in range(len(vendas)):
        numero_vendas = int(vendas[i][1])
        total += numero_vendas
    print(total)

elif opcao == "4":
    vendedor_maior = ""
    for i in range(len(vendas)):
        vendedor = vendas[i][0]
        numero_vendas = vendas[i][1]  
        if numero_vendas > maior_numero:
            maior_numero = numero_vendas
    print(maior_numero)

elif opcao == "5":
    ver_vendedor = input("informe o vendedor")

    for i in range(len(vendas)):
        vendedor = vendas[i][0]
        numero_vendas = vendas[i][1]  
        if ver_vendedor == vendedor:
            print(numero_vendas)
