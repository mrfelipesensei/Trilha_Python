#Peça um número ao usuário e informe se ele é divisível por 3 e por 5 ao mesmo tempo
n = int(input("Digite um número: "))

if n%3==0 and n%7==0: 
    print("Divisível por 3 e 7")
else:
    print("Não divisível por 3 e 7")