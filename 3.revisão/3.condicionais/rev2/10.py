#Peça ao usuário para digitar uma senha. Informe se a senha tem mais de 8 caracteres e contém ao menos um número
senha = input("Digite sua senha: ")

tem_numero = False
for char in senha:
    if char >= '0' and char <= '9': #verifica se o caractere é um número
        tem_numero = True

if len(senha) >= 8:
    if tem_numero:
        print("Senha forte!")
    else:
        print("Senha fraca: deve conter pelo menos um número.")

else:
    print("Senha fraca: deve ter pelo enos 8 caracteres.")