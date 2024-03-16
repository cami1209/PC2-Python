numeros_ingresados = []
numeros_pares = []
numeros_impares = []

while True:
    respuesta = input("¿Desea ingresar un número? (si/no): ")
    
    if respuesta.lower() == 'si':
        numero = input("Ingrese un número: ")
        
        try:
            numero = int(numero)
            numeros_ingresados.append(numero)
            
            if numero % 2 == 0:
                numeros_pares.append(numero)
            else:
                numeros_impares.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido")
            continue
    elif respuesta.lower() == 'no':
        break
    else:
        print("Por favor, responda con 'si' o 'no'.")

print("Todos los números ingresados:", numeros_ingresados)
print("Cantidad de números pares:", len(numeros_pares))
print("Cantidad de números impares:", len(numeros_impares))
