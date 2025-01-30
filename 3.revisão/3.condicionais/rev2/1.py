#Verificar se um número é par ou ímpar
n = int(input("Digite um número: "))

if n != 0:
    if n%2 == 0: 
        print(f"{n} é par!") 
    else: print(f"{n} é ímpar.")
else:
    print("Digite um número diferente de zero!") 