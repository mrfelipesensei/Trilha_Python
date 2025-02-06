#Crie um dicionário que armazene as notas de um aluno em três matérias e calcule a média

notas = {}

while True:
    try:
        notas["Matemática"] = float(input("Digite a nota: "))
        '''
        if 0 > notas["Matemática"] > 10 :
            raise ValueError("Valor inválido - Digite uma nota de 0 a 10")
        break
        '''
        if not 0 <= notas["Matemática"] <= 10: #Verifica se a nota está entre 0 e 10
            raise ValueError("Valor inválido - Digite uma nota de 0 a 10")
        break
    except ValueError as e:
        print(f"Erro: {e}")

while True:
    try:
        notas["Inglês"] = float(input("Digite a nota: "))
        if not 0 <= notas["Inglês"] <= 10:
            raise ValueError("Valor inválido - Digite uma nota 0 a 10")
        break
    except ValueError as e:
        print(f"Erro: {e}")

while True:
    try:
        notas["Português"] = float(input("Digite a nota: "))
        if not 0 <= notas["Português"] <= 10:
            raise ValueError("Valor inválido - Digite uma nota 0 a 10")
        break
    except ValueError as e:
        print(f"Erro: {e}")

'''
for chave,valor in notas.items():
    print(f"{chave}: {valor}")
'''

media = (notas["Matemática"] + notas["Inglês"] + notas["Português"]) / 3

print("A média de notas séra:",media)