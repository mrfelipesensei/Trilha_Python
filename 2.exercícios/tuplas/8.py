#Dada a tupla animais = 'cachorro','gato','papagaio','elefante'
#Verifique se a palavra "gato" está na tupla
#Verfique se a palavra "leão" está na tupla

animais = 'cachorro','gato','papagaio','elefante'

if animais.count("gato") != 0:
    print("gato está na tupla")
else:
    print("gato não está na tupla")

if animais.count("leão") != 0:
    print("leão está na tupla")
else:
    print("leão não está na tupla")

animal = str(input("Digite um animal: "))

animal_min = animal.lower() #Transforma tudo em minúsculo

if animal_min.isalpha(): #Verifica se foi digitado apenas letras

    if animais.count(animal_min) != 0: #Se a contagem do que foi digitado for != 0
        print(f"{animal_min} está na tupla")
    else:
        print(f"{animal_min} não está na tupla")

else:
    print("Digite apenas letras.")