import forca
import adivinhacao

print("===================")
print("Escolha o seu jogo!")
print("===================")

print("(1) Forca (2) Adivinhação")

escolha = int(input("Qual jogo?"))

if (escolha == 1):
    print("Jogo Forca")
    forca.jogar()
elif (escolha == 2):
    print("Jogo Adivinhação")
    adivinhacao.jogar()
