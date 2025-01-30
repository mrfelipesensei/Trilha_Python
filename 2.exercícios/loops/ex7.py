#solicita ao usuário o número
num = int(input("Digite o número para calcular o fatorial: "))

#inicializa a variável com 1 (base para o cálculo fatorial)
fatorial = 1

#loop para multiplicar os números de 1 até o número informado
for i in range(1, num + 1):
    fatorial *= i

#exibe o resultado
print(f"O fatorial de {num} é: {fatorial}")