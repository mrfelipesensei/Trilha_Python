#Peça ao usuário para inserir 5 nomes e armazene-os em uma lista, depois exiba os nomes em ordem alfabética
nomes = []

for i in range(5):
    while True:
        try:
            nome = input(f"Digite o {i+1}º nome: ")
            if nome.isalpha(): #Verifica se a string contém apenas letras
                nomes.append(nome)
                break
            else:
                raise ValueError("Entrada inválida. Digite apenas letras.")
        except ValueError as e:
            print(e)

#Ordena a lista de nomes em ordem alfabética
nomes.sort()

print("\nNomes em Ordem Alfabética: ")
for nome in nomes:
    print(nome)