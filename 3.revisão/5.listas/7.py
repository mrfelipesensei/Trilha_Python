#Peça ao usuário para digitar palavras até que ele digite "sair"
#Exiba a quantidade de palavras digitadas

palavras = []

while True:
    palavra = str(input("Digite uma palavra: "))

    if palavra.lower() == "sair":
        break

    if palavra.isalpha(): #Verifica se a palavra contém apenas letras
        palavras.append(palavra) #Se sim, adicione-a à lista
    else:
        print("Valor inválido, a palavra deve conter apenas letras.") #Se não exibe erro e não adicona


'''palavras.remove("sair") #remove a palavra sair de palavras'''

quantidade = len(palavras)

print("A quantidade de palavras digitadas é:",quantidade)