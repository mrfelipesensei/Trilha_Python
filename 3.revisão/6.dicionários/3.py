#Crie um dicionário que represente um aluno
#Com as chaves: nome, idade e notas (uma lista de três notas)
#Acesse e exiba a segunda nota

aluno = {
    "nome": "Felipe",
    "idade": 28,
    "notas": [8,7,9]
}

segunda_nota = aluno["notas"][1]
print(segunda_nota)