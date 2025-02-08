#Dada uma lista de palavras
#E uma palavra proibida - remova todas as ocorrências da palavra proibida da lista

palavras = []

while True:
    palavra = input("Digite uma palavra: ").lower()
    palavras.append(palavra)

    if palavra.lower() == "sair":
        break


palavras.remove("nazismo")
palavras.remove("sair")

print(palavras)