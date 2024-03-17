def omitir_vocales(cadena):
    resultado = ""
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    
    return resultado

texto = input("Ingrese una cadena de texto: ")

texto_sin_vocales = omitir_vocales(texto)
print("Texto sin vocales:", texto_sin_vocales)
