#Peça ao usuário a nota de 3 provas, se a média aritmética delas for maior ou igual a 7 exiba aprovado, entre 5 e 6 exiba recuperação, abaixo de 5 exiba reprovado
n1 = int(input("Digite a 1ª nota: "))
n2 = int(input("Digite a 2ª nota: "))
n3 = int(input("Digite a 2ª nota: "))

media = (n1+n2+n3)/3

if media >= 7:
    print(f"Sua média é: {media:.2f} Aprovado!")
elif media >= 5 and media <= 6:
    print(f"Sua média é: {media:.2f} Recuperação")
else:
    print(f"Sua média é: {media:.2f} Reprovado.")
#:.2f é a formatação de media para que exiba somente duas casas decimais após a vírgula