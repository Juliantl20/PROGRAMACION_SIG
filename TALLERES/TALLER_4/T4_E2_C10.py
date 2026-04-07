# Ejercicio 2: Diccionarios y Listas

def cargar_datos_espaciales(nombre_archivo):
    """
    Lee un archivo CSV limpio y devuelve una lista de diccionarios
    con las llaves: especie, latitud y longitud.
    """
    datos = []

    with open(nombre_archivo, "r", encoding="utf-8") as f:
        # Omitir encabezado
        next(f)

        for linea in f:
            especie, lat_str, lon_str = linea.strip().split(",")

            registro = {
                "especie": especie,
                "latitud": float(lat_str),
                "longitud": float(lon_str)
            }

            datos.append(registro)

    return datos


# Cargar datos limpios
arboles = cargar_datos_espaciales(archivo_limpio)

print("\nDatos cargados en memoria:")
for arbol in arboles:
    print(arbol)

# Calcular latitud promedio
suma_latitudes = 0

for arbol in arboles:
    suma_latitudes += arbol["latitud"]

latitud_promedio = suma_latitudes / len(arboles)

print(f"\nLatitud promedio de los árboles válidos: {latitud_promedio: