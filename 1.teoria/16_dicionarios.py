#Os dicionários são estruturas de dados que armazenam
#informações no formato chave-valor
#São úteis quando precisamos associar um nome a um valor

#Criando um Dicionário
#A sintaxe básica é:

dados = {
    "nome":"Felipe",
    "idade": 27,
    "curso": "Engenharia de Software"
}

print(dados)

#"nome","idade" e "curso" são chaves
#seus respectivos valores são "Felipe", 27 e "Engenharia de Software"

#Acessando valores em um Dicionário
print("\n")
print(dados["nome"])
print(dados["idade"])


#Se tentarmos acessar uma chave inexistente - erro!
#Para evitar isso - usamos .get()
'''
print(dados["cidade"])
'''
print(dados.get("cidade","Chave não encontrada"))

#Adicionando e Modificando Valores
#Adicionar um novo par:
dados["cidade"] = "Brasília"
print(dados)

#Para modificar um valor existente:
dados["idade"] = 28
print(dados)

#Removendo Itens
#del ou .pop()

del dados["curso"] #Remove a chave 'curso'
print(dados)

idade = dados.pop("idade") #Remove e retorna a idade
print(idade)

print(dados)
print("\n")

#Iterando sobre Dicionários
#Podemos percorrer as chaves, valores ou ambos

#Apenas as chaves
for chave in dados:
    print(chave)

#Apenas os valores
for valor in dados.values():
    print(valor)

#Chaves e valores juntos
for chave, valor in dados.items():
    print(f"{chave}: {valor}")