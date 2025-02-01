#Faça um while que conte de 10 a 1. Se o número for 5 exiba "Metade do caminho!"
i = 10
while i >= 0:
    if i == 5:
        print("Metade do caminho!")
    else:
        print(i) #imprime o valor de i se não for 5
    i-=1 #decrementa o valor em cada iteração
    