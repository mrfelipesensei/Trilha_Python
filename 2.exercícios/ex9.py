tempc = float(input("Digite a temperatura em ºC: "))

if tempc > 30:
    print("Está quente")
elif tempc >= 15 and tempc <=30:
    print("Temperatura amena")
elif tempc < 15:
    print("Está frio")

tempf = (tempc * 9/5) + 32
tempk = (tempc + 273.15) 

print(f"{tempc}ºC equivale à {tempf}ºF")
print(f"{tempc}ºC equivale à {tempk}K")