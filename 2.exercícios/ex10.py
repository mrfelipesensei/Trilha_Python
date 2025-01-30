tempo = int(input("Por quantas horas ficou estacionado? "))

if tempo > 5:
    taxa1 = tempo * 3
    print(f"Você terá que pagar R${taxa1}")
elif tempo > 2 and tempo <= 5:
    taxa2 = tempo * 4
    print(f"Você terá que pagar R${taxa2}")
else:
    taxa3 = tempo * 5
    print(f"Você terá que pagar R${taxa3}")