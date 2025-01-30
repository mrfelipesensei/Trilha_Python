#Crie um programa que receba uma nota de 0 a 10 e exiba "Aprovado" se for maior ou igual a 7, ou "Reprovado" caso contrário
nota = int(input("Digite um número de 0 à 10: "))

'''
if nota >= 7:
    print("Aprovado")
elif nota < 7:
    print("Reprovado")
'''

if nota > 10 or nota < 0:
    print("VALOR IVÁLIDO")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")