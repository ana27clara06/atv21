# Exercício Python 21: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
print("OS FOGO DE IRÃO EXPLODIR EM:")
fogodeartificio = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for contagem in fogodeartificio:
    print(contagem)
    time.sleep(1)
else:
    print("pow pow pow")