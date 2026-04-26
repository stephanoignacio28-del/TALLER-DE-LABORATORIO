numero = int(input("Ingrese un numero: "))
contador = 0

while numero > 1:
    resultado = numero // 2
    print(f"{numero} / 2 = {resultado}")
    numero = resultado
    contador += 1

print(f"Se dividio {contador} veces")
