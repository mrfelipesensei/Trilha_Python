#Peça ao usuário para digitar palavras até que ele digite "sair"
#Exiba a quantidade de palavras digitadas

palavras = []

while True:
    palavra = str(input("Digite uma palavra: "))
    palavras.append(palavra)
    if palavra == "sair":
        break

palavras.remove("sair") #remove a palavra sair de palavras
quantidade = len(palavras)

print("A quantidade de palavras digitadas é:",quantidade)