idade = int(input("Digite sua idade: "))

if idade >= 18:
    if idade > 65:
        print("Você é legalmente idoso.")
    else:
        print("Você é adulto.")
elif idade < 18 and idade > 15:
    print("Você é adolescente.")
else:
    print("Você é uma criança.")