#Crie um dicionário onde as chaves são nomes de alunos
#Os valores são listas com suas notas
#Depois calcule a média de cada aluno

notas = {
    "John": [8,7,9],
    "Bob": [7,8,7],
    "Melvin": [9,5,2],
    "Arnold": [0,4,10]
}

for nome, notas_aluno in notas.items():
    media = sum(notas_aluno)/len(notas_aluno)
    print(f"A média de {nome} é: {media:.2f}")