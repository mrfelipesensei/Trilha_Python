#Escolha um número aleatório de 1 a 10 e peça ao usuário para adivinhar. Continue pedindo até ele acertar, usando while
print("Tente a sorte! Escolha um número de 1 a 10: ")

numero = 0
sorteio = 8

while numero != sorteio:
    numero = int(input("Digite o número: "))
    #Vericando o palpite
    if numero > sorteio:
        print("Tente um menor...")
    elif numero < sorteio:
        print("Tente um maior...")
else:
    print("Você ACERTOU!")