##Construa um programa que realiza o sorteio de um número entre 1 e 15.
##
##O usuário terá 3 chances de acertar o valor.
##
##A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# %%
import random 

def get_input():
        while True:
            try:
                numero = int(input("entre com um numero:"))

            except ValueError as err:
                print("entre com um numero valido")
                continue

            if  1 <= numero <= 15:
                return numero

            print("o valor deve ser entre 1 e 15")

def check_numbers(numero_sorteado,numero):
    if numero == numero_sorteado:
        print("parabens vc conseguiu")
        return True

    elif numero > numero_sorteado:
        print("numero muito alto")
        return False


    else:
        print("numero muito baixo")
        return False


numero_sorteado = random.randint(1,15)


for i in range(3):

    numero = get_input()

    if check_numbers(numero_sorteado=numero_sorteado , numero=numero):
        break

else:
    print("suas tentativas acabaram")