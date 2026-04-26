n = int(input("Cuantos numeros vas a ingresar? "))
lista = []

for i in range(n):
    num = int(input(f"Ingrese numero {i+1}: "))
    lista.append(num)

original = lista.copy()

# Algoritmo Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(f"Lista original: {original}")
print(f"Lista ordenada: {lista}")
