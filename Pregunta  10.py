def obtener_mes_numero(mes):
    meses = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }
    return meses.get(mes)

def convertir_fecha(fecha):
    partes = fecha.split()
    
    if len(partes) == 3:
        mes, dia, anio = partes
    
    elif len(partes) == 2:
        mes_str, dia = partes
        anio = input("Ingrese el año: ")
        mes = obtener_mes_numero(mes_str)
        if mes is None:
            return "Mes inválido"
    else:
        return "Formato de fecha no válido."
    
    
    fecha_formateada = f"{anio}-{mes}-{dia.zfill(2)}"

    return fecha_formateada


fecha = input("Ingrese una fecha (mes/día/año o mes día, año): ")


fecha_convertida = convertir_fecha(fecha)


print("Fecha en formato año/mes/día:", fecha_convertida)
