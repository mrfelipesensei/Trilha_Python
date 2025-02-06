#Crie um dicionário que armazene as notas de um aluno em três matérias e calcule a média

notas = {}

notas["Matemática"] = float(input("Digite a nota: "))
notas["Inglês"] = float(input("Digite a nota: "))
notas["Português"] = float(input("Digite a nota: "))

'''
for chave,valor in notas.items():
    print(f"{chave}: {valor}")
'''

media = (notas["Matemática"] + notas["Inglês"] + notas["Português"]) / 3

print("A média de notas séra:",media)