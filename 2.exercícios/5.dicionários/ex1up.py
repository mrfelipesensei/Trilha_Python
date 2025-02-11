estoque = {}

while True:
    print("== Sistema de Estoque ==")
    print("1 - Adicionar Produto")
    print("2 - Alterar Nome do Produto")
    print("3 - Exibir Estoque")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do Produto: ").lower()
        if nome in estoque:
            print("Produto já existe!")
        else:
            preco = float(input("Preço do Produto: R$ "))
            quantidade = float(input("Quantidade: "))
            estoque[nome] = {"preço": preco, "quantidade": quantidade}
            print(f"{nome} adicinado ao estoque!")
    
    elif opcao == "2":
        antigo_nome = input("Nome do Produto que deseja alterar: ").lower()
        if antigo_nome in estoque:
            novo_nome = input("Novo nome do Produto: ").lower()
            estoque[novo_nome] = estoque.pop(antigo_nome)
            print(f"Produto: '{antigo_nome}' alterado para '{novo_nome}'.")
        else:
            print("Produto não encontrado!")
    
    elif opcao == "3":
        print("== Estoque Atual ==")
        if not estoque:
            print("Estoque vazio!")
        else:
            for nome, info in estoque.items():
                print(f"{nome} | Preço: R${info['preço']:.2f} | Quantidade: {info['quantidade']}")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")