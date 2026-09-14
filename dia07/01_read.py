# %%

nome_arquivo = 'historia.txt'

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

#abri o arquivo
open_file = open(nome_arquivo)

#ler o arquivo
conteudo = open_file.read()
print(conteudo)

#fecha o arquivo
open_file.close()

