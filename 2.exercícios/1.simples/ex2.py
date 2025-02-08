anos = int(input("Digite o número de anos: "))

ano = 365
dia = 24
hora = 60
min = 60

tot1 = anos * ano
tot2 = tot1 * dia
tot3 = tot2 * hora
tot4 = tot3 * min
print(f"{anos} anos tem {tot1} dias.")
print(f"{anos} anos tem {tot2} horas.")
print(f"{anos} anos tem {tot3} minutos.")
print(f"{anos} anos tem {tot4} segundos.")