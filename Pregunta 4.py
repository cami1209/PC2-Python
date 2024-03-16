def ingresar_calificaciones():
    calificaciones = []
    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
        calificaciones.append(calificacion)
    return calificaciones

def main():
    n = int(input("Ingrese el número de alumnos: "))
    
    alumnos = []
    
    for i in range(1, n + 1):
        print(f"Ingrese los datos del alumno {i}:")
        nombre = input("Nombre del alumno: ")
        calificaciones = ingresar_calificaciones()
        
        alumno = {"Nombre": nombre, "Calificaciones": calificaciones}
        
        alumnos.append(alumno)
    

    print("\nListado de alumnos:")
    for alumno in alumnos:
        print(f"Nombre: {alumno['Nombre']}, Calificaciones: {alumno['Calificaciones']}")


if __name__ == "__main__":
    main()
