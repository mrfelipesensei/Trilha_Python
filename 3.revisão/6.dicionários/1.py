#Peça os usuário digitar uma frase e conte quantas vezes cada palavra aparece

frase = input("Digite a frase desejada: ")

#Divide a frase em palavras
palavras = frase.split()

#Cria um dicionário para armazenar as frequências
frequencias = {}

#Conta as palavras
for palavra in palavras:
    #Remove pontuações e converte para minúsculas
    palavra = palavra.lower().strip('.,!?"')

    if palavra in frequencias:
        frequencias[palavra] += 1 #Conta a palavra
    else:
        frequencias[palavra] = 1

print("Frequência de cada palavra:")
print("\n")
print(frequencias)