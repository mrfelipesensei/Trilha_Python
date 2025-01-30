#Crie uma variável salário com valor de 2000. Aumente o valor dela em 10%
'''
salario = 2000
aumento = salario * 0.1
total = salario + aumento
print(total)
'''
salario = float(input("Digite o Salário: "))
perc = float(input("Digite a porcentagem de aumento: "))

calc = (perc / 100)
aumento = salario * calc
total = salario + aumento

print(total)