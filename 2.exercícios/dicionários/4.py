#Crie um dicionário representando um estoque de loja
#Onde a chave é o nome do produto e o valor é quantidade disponível

estoque = {
    "Whey Protein": 30,
    "Creatina" :  45,
    "Termogênico": 23,
    "Coqueteleira": 80,
    "Camiseta": 68,
    "Pré-treino": 0
}

#Peça ao usuário um nome de produto e verifique se ele está no estoque
while True:
    try:
        produto = str(input("Digite o nome do produto: "))
        if not produto.isalpha(): #Verifica se o produto digitado são letras
            raise ValueError("O nome do produto deve conter apenas letras.")
        break
    except ValueError as e:
        print(f"Erro: {e}")

'''
for chave,valor in estoque.items():
    if produto == chave:
        print(f"{chave}: {valor}")
'''
#Verifica se o produto está no estoque
if produto in estoque:
    quantidade = estoque[produto]
    print(f"{produto}: {quantidade}")
else:
    print("Produto não encontrado no estoque")