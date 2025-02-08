#Peça ao usuário para inserir informações sobre um produto
#(nome,preço,quantidade) e armazene em um dicionário

produto = { } #Dicionário vazio

while True:
    try:
        produto["Nome"] = str(input("Digite o nome do produto: "))
        if not produto["Nome"].isalpha(): #Verifica se o produto digitado são letras
            raise ValueError("O nome do produto deve conter apenas letras.")
        break #Sai do loop se o nome for válido
    except ValueError as e:
        print(f"Erro: {e}")

while True:
    try:
        produto["Preço"] = float(input("Digite o preço do produto: "))
        if produto["Preço"] <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        break
    except ValueError:
        print("Erro: Preço inválido. Digite um número decimal")

while True:
    try:
        produto["Quantidade"] = int(input("Digite a quantidade do produto: "))
        if produto["Quantidade"] <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        break
    except ValueError:
        print("Quantidade Inválida. Digite um número inteiro")


print("\nInformações do produto: ")
for chave, valor in produto.items():
    print(f"{chave}: {valor}")