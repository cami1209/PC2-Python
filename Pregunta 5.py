def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))
    
    return cantidad

numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese un dígito: "))

resultado = contar_digitos(numero, digito)

# Imprimir el resultado
print(f"Cantidad de veces {digito} en el número: {resultado}")
