#Peça uma palavra ao usuário e conte quantas vogais ela tem

palavra = input("Digite uma palavra: ")

contador = 0

for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador += 1

print(f"A palavra {palavra} tem {contador} vogais.")