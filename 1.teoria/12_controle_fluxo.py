#break interrompe o fluxo
#continue pula para a próxima iteração
#else executa ao final do loop se não houver break

for i in range(1,10):
    if i == 5:
        break
    print(i)
else:
    print("Loop concluído!") 