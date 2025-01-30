#Peça a idade do usuário e classifique-o como criança (menor de 12), adolescente (12 a 17), ou adulto (18 até 60), idoso (60 ou mais)
idade = int(input("Digite sua idade: "))

if idade >= 60:
    print("Você é um idoso.")
elif idade >= 18 and idade <60:
    print("Você é adulto.")
elif idade > 12 and idade <= 17:
    print("Você é um adolescente.")
else:
    print("Você é uma criança.")