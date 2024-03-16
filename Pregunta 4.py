# Función para ingresar las calificaciones de un alumno
def ingresar_calificaciones():
    calificaciones = []
    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
        calificaciones.append(calificacion)
    return calificaciones

# Función principal
def main():
    # Solicitar la cantidad de alumnos
    n = int(input("Ingrese el número de alumnos: "))
    
    # Crear una lista para almacenar los datos de los alumnos
    alumnos = []
    
    # Iterar para ingresar los datos de cada alumno
    for i in range(1, n + 1):
        print(f"Ingrese los datos del alumno {i}:")
        nombre = input("Nombre del alumno: ")
        calificaciones = ingresar_calificaciones()
        
        # Crear un diccionario para almacenar los datos de un alumno
        alumno = {"Nombre": nombre, "Calificaciones": calificaciones}
        
        # Agregar el diccionario a la lista de alumnos
        alumnos.append(alumno)
    
    # Mostrar el listado completo de los alumnos
    print("\nListado de alumnos:")
    for alumno in alumnos:
        print(f"Nombre: {alumno['Nombre']}, Calificaciones: {alumno['Calificaciones']}")

# Llamar a la función principal
if __name__ == "__main__":
    main()
