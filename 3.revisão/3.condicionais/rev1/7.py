#Verifique se um ano fornecido pelo usuário é bissexto - dica: divisível por 4, mas não por 100, exceto se também for divisível por 400
ano = int(input("Digite um ano: "))

if ano%4 == 0:
    #Se é divisível por 4 ele *pode* ser bissexto
    if ano%100 == 0:
        #Se é divisível por 100 ele *não* é bissexto, a menos que...
        if ano%400 == 0:
            print(f"{ano} é bissexto!")
        else:
            print(f"{ano} não é bissexto!")
    else:
        #Se não é divisível por 100, mas por 4, então é bissexto!
        print(f"{ano} é bissexto!")
else:
    #Se não é divisível por 4, definitivamente não é bissexto
    print(f"{ano} não é bissexto!")