#Peça ao usuário inserir três números e exiba o maior deles
n1 = int(input("Digite o 1º Número: "))
n2 = int(input("Digite o 2º Número: "))
n3 = int(input("Digite o 3º Número: "))

if n1 != n2 and n2 != n3:
    if n1 > n2 and n1 > n3: 
        print(f"{n1} é maior que {n2} e {n3}")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} é maior que {n1} e {n3}")
    else:
        print(f"{n3} é maior que {n1} e {n2}")
else:
    print("Os números são iguais!")

