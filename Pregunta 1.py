numeros_divisibles = []
for num in range(1499, 2701):
    if num % 7 == 0 and num % 5 == 0:
        numeros_divisibles.append(num)

print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros_divisibles)
