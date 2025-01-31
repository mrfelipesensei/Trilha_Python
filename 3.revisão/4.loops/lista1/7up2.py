#Escolha um número aleatório de 1 a 10 e peça ao usuário para adivinhar. Continue pedindo até ele acertar, usando while
print("Tente a sorte! Escolha um número de 1 a 10: ")

numero = 0
sorteio = 8

while numero != sorteio:
    try:
        numero = int(input("Digite o número: "))
        #Verifica se o número está no intervalo correto
        if 1 <= numero <= 10:
            #Testando o palpite:
            if numero > sorteio:
                print("É menor...")
            elif numero < sorteio:
                print("É maior...")
            
        else:
            print("Número fora do intervalo!")
    
    except ValueError: #Tratamento de erros
        print("Entrada Inválida. Digite um número inteiro.")
else:
    print("Você ACERTOU!")