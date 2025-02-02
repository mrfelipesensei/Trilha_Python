#Peça notas ao usuário até que ele digite -1 - Depois, exiba a média das notas digitadas
soma = 0
nota = 0
contador = 0

while nota >=0:
    try:
        nota = int(input("Digite a nota: "))
        if nota > 0:
            soma+= nota
            contador+=1

            media = soma / nota
    except ValueError:
        print("Por favor, digite um número inteiro.")
else:
    print("A média dos números é: ",media)