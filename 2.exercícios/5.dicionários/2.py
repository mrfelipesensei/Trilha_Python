#Peça ao usuário para inserir informações sobre um produto
#(nome,preço,quantidade) e armazene em um dicionário

produto = { } #Dicionário vazio

produto["Nome"] = str(input("Digite o nome do produto: "))

produto["Preço"] = float(input("Digite o preço do produto: "))

produto["Quantidade"] = int(input("Digite a quantidade do produto: "))

print("\nInformações do produto: ")
for chave, valor in produto.items():
    print(f"{chave}: {valor}")