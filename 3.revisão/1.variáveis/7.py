#Crie uma variável frase com o texto "Aprendendo Python". Exiba o número de caracteres na frase
'''
frase = "Aprendendo Python"
num_caracteres = len(frase)

num_letras = len(frase) - frase.count(" ")
print(num_letras)
'''
frase = str(input("Digite sua frase: "))

num_carac = len(frase)
num_letras = len(frase) - frase.count(" ")

print(f"Número de caracteres: {num_carac}\nNúmero de letras: {num_letras}")