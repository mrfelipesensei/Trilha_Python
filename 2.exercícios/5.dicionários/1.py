#Crie um dicionário com informações sobre um livro - (título, autor, ano)
livro = {
    "Título":"Ecce Homo",
    "Autor": "Nietzche",
    "Ano": "2008",
    "Editora": "Companhia de Bolso"
}

for chave,valor in livro.items():
    print(f"{chave}: {valor}")

#Adicioone um novo campo - por exemplo gênero
livro["Gênero"] = "Filosofia"

#Modifique o ano de publicação do livro
livro["Ano"] = "1908"

#Remova o campo gênero do dicionário
del livro["Gênero"]