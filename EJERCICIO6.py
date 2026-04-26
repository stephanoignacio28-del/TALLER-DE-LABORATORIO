n = int(input("Cuantos numeros vas a ingresar? "))
lista = []

for i in range(n):
    num = int(input(f"Ingrese numero {i+1}: "))
    lista.append(num)

print("Parejas:")
for i in range(len(lista)):
    for j in range(len(lista)):
        if i != j:
            print(f"({lista[i]}, {lista[j]})")
