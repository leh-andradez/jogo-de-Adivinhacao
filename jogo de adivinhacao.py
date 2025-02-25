print("**********************")
print("Bem vindo ao Jogo de Adivinhação!")
print("**********************")
numero_secreto = 82
total_de_tentativas = 5
rodada = 2

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

chute_str = input("Digite o seu número:")
print("você digitou:", chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou!")
    else:
        if (maior):
            print("O seu chute é maior que o número secreto!")
        elif(menor):
            print("O seu chute é menor que o número secreto!")

            rodada = rodada + 1



print("Fim de Jogo!")