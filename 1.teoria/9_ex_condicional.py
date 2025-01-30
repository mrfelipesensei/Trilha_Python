nota = float(input("Digite sua nota de 0 à 10: "))

if nota >= 0 and nota <= 10:
    if nota >= 7:
        print("Aprovado!")
    elif nota >=5 and nota <= 6.9:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Número inválido!")