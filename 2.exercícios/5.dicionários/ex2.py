#Ex Prático - tradutor simples

tradutor = {
    "cahorro": "Hund",
    "gato" : "Katze",
    "abelha": "Biene",
    "água": "Wasser",
    "ovo" : "Ei",
    "inseto" : "Insekt"

}

palavra = input("Digite uma palavra em português: ").lower()

print(tradutor.get(palavra,"Palavra não encontrada"))