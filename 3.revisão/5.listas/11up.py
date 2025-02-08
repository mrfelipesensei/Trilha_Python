#Dada uma lista de palavras
#E uma palavra proibida - remova todas as ocorrências da palavra proibida da lista

palavras = []

while True:
    palavra = input("Digite uma palavra: ").lower()

    if palavra.lower() == "sair":
        break

    if palavra.isalpha():
        palavras.append(palavra)
    else:
        print("Valor inválido, a palavra deve conter apans letras.")

palavra_proibida = "nazismo"

#Remove TODAS as ocorrências da palavra proibida
while palavra_proibida in palavras:
    palavras.remove(palavra_proibida)

print(palavras)