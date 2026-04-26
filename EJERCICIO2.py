cantidad = int(input("Cuantos numeros vas a ingresar? "))
numeros = []

for i in range(cantidad):
    num = int(input(f"Ingrese numero {i+1}: "))
    numeros.append(num)

if numeros:
    mayor = max(numeros)
    menor = min(numeros)
    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}")
