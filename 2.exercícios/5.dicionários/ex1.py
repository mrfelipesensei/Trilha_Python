#Exemplo prático - Gerenciando um estoque simples

estoque = {
    "maçã": {"preço": 2.5, "quantidade": 50},
    "banana": {"preço": 1.8, "quantidade": 30},
    "laranja": {"preço": 3.2, "quantidade": 20}
}

produto = input("Digite um produto: ").lower()

if produto in estoque:
    info = estoque[produto]
    print(f"Preço: R${info['preço']} | Quantidade: {info['quantidade']}")
else:
    print("Produto não encontrado!")