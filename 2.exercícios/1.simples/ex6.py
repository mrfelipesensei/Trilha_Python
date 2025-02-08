idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode votar e dirigir.")
elif idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode nem votar e nem dirigir.")