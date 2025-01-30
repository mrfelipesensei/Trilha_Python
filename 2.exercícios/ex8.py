ticket = str(input("Você tem a passagem? S/N "))
visto = str(input("Você tem o visto? S/N "))
status = "Pode viajar para os EUA" if ticket == "S" and visto == "S" else "Não pode viajar para os EUA"
print(status)