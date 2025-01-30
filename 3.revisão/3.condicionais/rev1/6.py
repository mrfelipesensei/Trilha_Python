#Crie um sistema de login simples que valide se o usuário e senha fornecidos estão corretos - use valores ficos para validação como admin e 123
login_ref = "admin"
senha_ref = "123"

login = input("Digite seu Login: ")
senha = input("Digite sua Senha: ")
#!Nesse caso NÃO usamos os tipos de variáveis antes do input!

if login == login_ref and senha == senha_ref: 
    print("ACESSO PERMITIDO")
else:
    print("Valores inválidos")
    print("ACESSO NEGADO")