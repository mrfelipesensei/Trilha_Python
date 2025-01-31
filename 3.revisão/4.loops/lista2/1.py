#Peça 10 números ao usuário e diga quantos são pares e quantos são ímpares
#definindo as variáveis
quantidade = 10
contador = 0
cont_par = 0
cont_impar = 0
#contadores inicializados em 0

#enquanto o contador for menor que a quantidade, pede o número
while contador < quantidade:
    numero = int(input("Digite o número: "))
    contador+=1 #incremento de iteração do contador

    if numero != 0: #Verifica se o número é diferente de zero
        if numero % 2 == 0: #verifica se o número é par
            cont_par+=1 #conta o número par
        elif numero % 2 != 0: #verifica se o número é ímpar
            cont_impar+=1 #conta o número ímpar
    
print(f"A quantidade de pares é: {cont_par}")
print(f"A quantidade de ímpares é: {cont_impar}")