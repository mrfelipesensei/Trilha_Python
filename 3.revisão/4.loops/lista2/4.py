#O usuário tem 5 chances para digitar a senha correta "Python123" - se não o acesso é negado
tentativas = 0
senha = ""
senha_correta = "Python123"

while senha != senha_correta and tentativas < 5:
    senha = input("Digite sua senha: ")
    tentativas+=1 #incremento
    tentativas_restantes = 5 - tentativas #calcula as tentativas restantes

    if senha != senha_correta:
        print("ACESSO NEGADO!")
        if tentativas < 5: #Informa as tentativas restantes
            print(f"Você tem mais {tentativas_restantes} tentativa(s).")
            print("Tente novamente: ")
    elif senha == senha_correta:
        print("ACESSO PERMITIDO")
        break


if senha != senha_correta and tentativas == 5:
    print("Número de tentativas excedido!")