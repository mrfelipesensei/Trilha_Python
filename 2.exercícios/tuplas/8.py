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

if animais.count(animal) != 0:
    print(f"{animal} está na tupla")
else:
    print(f"{animal} não está na tupla")