n = int(input("Cuantos numeros vas a ingresar? "))
lista = []

for i in range(n):
    num = int(input(f"Ingrese numero {i+1}: "))
    lista.append(num)

buscado = int(input("Que numero desea buscar? "))
encontrado = False

for i in range(len(lista)):
    if lista[i] == buscado:
        print(f"El numero {buscado} fue encontrado en la posicion {i}")
        encontrado = True
        break

if not encontrado:
    print(f"El numero {buscado} no fue encontrado")
