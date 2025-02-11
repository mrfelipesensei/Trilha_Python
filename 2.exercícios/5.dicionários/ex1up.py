estoque = {}

while True:
    print("== Sistema de Estoque ==")
    print("1 - Adicionar Produto")
    print("2 - Alterar Nome do Produto")
    print("3 - Exibir Estoque")
    print("4 - Apagar Produto")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do Produto: ").lower()
        if nome in estoque:
            print("Produto já existe!")
        else:
            preco = float(input("Preço do Produto: R$ "))
            quantidade = float(input("Quantidade: "))
            estoque[nome] = {"preço": preco, "quantidade": quantidade} #Adiciona o nome, preço e quantidade ao dicionário
            print(f"{nome} adicinado ao estoque!")
    
    elif opcao == "2":
        antigo_nome = input("Nome do Produto que deseja alterar: ").lower() #Cria a variável antigo_nome
        if antigo_nome in estoque:                             #Se antigo_nome estiver no estoque
            novo_nome = input("Novo nome do Produto: ").lower() #Pede ao usuário que digite o novo_nome
            estoque[novo_nome] = estoque.pop(antigo_nome)       #Atualiza o novo nome - retirando o antigo_nome
            print(f"Produto: '{antigo_nome}' alterado para '{novo_nome}'.")
        else:
            print("Produto não encontrado!")
    
    elif opcao == "3":
        print("== Estoque Atual ==")
        if not estoque:     #Se não existir estoque gravado
            print("Estoque vazio!")
        else:
            for nome, info in estoque.items():   #Exibe as informações do estoque cadastrado
                print(f"{nome} | Preço: R${info['preço']:.2f} | Quantidade: {info['quantidade']}")

    elif opcao == "4":
        apagar_nome = input("Nome do Produto que deseja apagar: ").lower() #Cria a variável apagar_nome
        if apagar_nome in estoque:              #Se apagar_nome estiver no estoque
            estoque[nome] = estoque.pop(apagar_nome) #Apaga do esque o nome digitado pelo usuário
            print(f"Produto: '{apagar_nome}' foi apagado do estoque.")
        else:
            print("Produto não encontrado!")

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")