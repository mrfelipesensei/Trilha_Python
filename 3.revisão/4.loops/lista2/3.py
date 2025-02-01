#Escolha um número secreto entre 1 e 10 e peça ao usuário para adivinhar em até 3 tentativas
sorteio = 8
num = 0
tentativas = 0

while num != sorteio and tentativas < 3:
    try:
        num = int(input("Digite um número: "))
        tentativas+=1 #incremento
        if 1 <= num <= 10: #testando o palpite
            if num > sorteio:
                print("É menor")
            elif num < sorteio:
                print("É maior")

        if num == sorteio:
            print("Você ACERTOU!")
            break
    
    except ValueError: #Tratamento de erros
        print("Entrada Inválida. Digite um número inteiro. ")