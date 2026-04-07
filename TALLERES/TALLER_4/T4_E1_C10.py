# Ejercicio 1: I/O y Excepciones

# 1. Crear el archivo crudo
contenido_crudo = """Especie,Latitud,Longitud
Roble,4.6097,-74.0817
Pino,4.6XYZ,-74.0900
Cedro,4.6150,-74.0850
Eucalipto,NULA,-74.0700
Nogal,4.6200,-74.0650"""

archivo_crudo = "arboles_crudos.txt"
archivo_limpio = "arboles_limpios.csv"

with open(archivo_crudo, "w", encoding="utf-8") as f:
    f.write(contenido_crudo)

print(f"Archivo '{archivo_crudo}' creado correctamente.")


# 2. Función para limpiar el inventario
def limpiar_inventario(archivo_entrada, archivo_salida):
    """
    Lee un archivo de inventario forestal con posibles errores en coordenadas.
    Si una línea es válida, la escribe en un nuevo archivo limpio.
    Si falla la conversión a float, omite la línea y muestra una advertencia.
    """
    with open(archivo_entrada, "r", encoding="utf-8") as f_in, \
         open(archivo_salida, "w", encoding="utf-8") as f_out:
        
        # Leer encabezado y copiarlo al archivo limpio
        encabezado = f_in.readline()
        f_out.write(encabezado)

        # Procesar línea por línea
        for linea in f_in:
            partes = linea.strip().split(",")

            especie = partes[0]
            lat_str = partes[1]
            lon_str = partes[2]

            try:
                latitud = float(lat_str)
                longitud = float(lon_str)

                f_out.write(f"{especie},{latitud},{longitud}\n")

            except ValueError:
                print(f"Advertencia: la especie '{especie}' tuvo un error en las coordenadas y fue omitida.")


# Ejecutar la limpieza
limpiar_inventario(archivo_crudo, archivo_limpio)
print(f"Archivo limpio generado: '{archivo_limpio}'")