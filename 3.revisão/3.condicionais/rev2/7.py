#Crie um programa onde o usuário tenta advinhar um número entre 1 a 10 que você definiu. Informe se ele acertou ou não
tentativa = int(input("Digite um número entre 1 a 10: "))

numero = 8

if tentativa == numero: 
    print("Você acertou!") 
else: print("Você errou.")