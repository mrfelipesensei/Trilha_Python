#Peça para um usuário inserir um número e diga se ele é divisível por 3 e por 5 ao mesmo tempo
num = int(input("Digite um número: "))
'''
if num%3==0 : print("É divisível por 3")
if num%5==0 : print("É divisível por 5")
'''
if num != 0:
    if num%3 == 0 and num%5 == 0:
        print(f"{num} é divisível por 3 e 5")
    elif num%3 == 0:
        print(f"{num} é divisível por 3")
    elif num%5 == 0:
        print(f"{num} é divisível por 5")