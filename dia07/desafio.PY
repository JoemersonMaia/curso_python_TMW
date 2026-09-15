##Construa um programa que realiza o sorteio de um número entre 1 e 15.
##
##O usuário terá 3 chances de acertar o valor.
##
##A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# %%

numero_sorteado = 10

for i in range(3):

    numero = int(input("digite um numero: "))
    if not 1 <= numero_sorteado <= 15:
        continue 

    if numero == numero_sorteado:
        print("parabens vc conseguiu")
        break

    elif numero > numero_sorteado:
        print("numero muito alto")

    else:
        print("numero muito baixo")
    
else:
    print("suas tentativas acabaram")