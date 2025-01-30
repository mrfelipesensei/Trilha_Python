#Peça um ano ao usuário e determine se ele é bissexto - divisível por 4 mas não por 100, exceto se for divisivle por 400
ano = int(input("Digite um ano: "))
'''
if ano%4==0 and ano%100==1 or ano%400==0:
    print("Teste")
'''    
if ano%4 == 0 and (ano%100 != 0 or ano%400 == 0):
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto.")