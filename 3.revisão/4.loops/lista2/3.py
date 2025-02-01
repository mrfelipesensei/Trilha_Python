#Escolha um número secreto entre 1 e 10 e peça ao usuário para adivinhar em até 3 tentativas
sorteio = 8
num = 0
tentativas = 0

while num != sorteio and tentativas < 3:
    num = int(input("Digite um número: "))
    tentativas+=1
    if num == sorteio:
        print("Você ACERTOU!")
        break