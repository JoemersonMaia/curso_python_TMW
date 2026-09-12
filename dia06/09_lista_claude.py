##. Classificador de idade
##Crie uma função classificar_idade(idade) que recebe um número e retorna:
##
##"criança" se menor que 12
##"adolescente" se entre 12 e 17
##"adulto" se 18 ou mais

# %%
def classificar_idade(idade:int)->str:
    if idade <= 12:
        print("ciranca")
    elif idade > 12 and idade <=17:
        print("adoslecente")
    else:
        print("adulto")
        return print

classificar_idade(18)


##2. Buscar em lista
##Crie uma função tem_item(lista, item) que recebe uma lista e um item, e 
##retorna True se o item estiver na lista e False caso contrário (sem usar
## o operador in diretamente — percorra com for e if).
# %%


# %%
def tem_item(lista:list ,item: int)->str:
    for i in range(len(lista)):
        if item == lista[i]:
         return "tem"
        else:
            return 'nao tem'

tem_item([1,2], 2)


##3. Contador de palavras
##Crie uma função contar_palavras(texto) que recebe 
##uma frase (string) e retorna um dicionário onde as chaves
##são as palavras e os valores são quantas vezes cada palavra aparece no texto.
##
##Exemplo:
##
##python
##contar_palavras("o gato viu o rato o gato correu")
### {'o': 3, 'gato': 2, 'viu': 1, 'rato': 1, 'correu': 1}

# %%

def contar_palavras(texto):
    palavras = texto.split()
    contador = {}
    for i in range(len(palavras)):
        if palavras[i] in contador:
            contador[palavras[i]] += 1
        else:
            contador[palavras[i]] = 1
    print(contador)

contar_palavras("eu sou eu sou eu")


##Crie uma função atualizar_estoque(estoque, produto, quantidade) onde estoque é um 
##dicionário {produto: quantidade}.
##
##Se o produto já existe, soma a quantidade
##Se não existe, cria com aquela quantidade
##Se a quantidade for negativa e maior que o estoque atual, imprime "Estoque insuficiente"
##    e não faz a alteração

# %%

def atualizar_estoque(estoque: dict, produto: str, quantidade: int) -> dict:
    if produto in estoque:
        if quantidade < 0 and estoque[produto] < abs(quantidade):
            print("Estoque insuficiente")
        else:
            estoque[produto] += quantidade
    else:
        if quantidade > 0:
            estoque[produto] = quantidade
        else:
            print("Produto não encontrado")

    print(estoque)
    return estoque


estoque = {"bieleta": 20, "junta homocinética": 50}

atualizar_estoque(estoque, "cabo de vela", 10)

# %%
