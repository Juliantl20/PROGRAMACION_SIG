def calcular_bbox(lista_coordenadas):
    """
    Calcula la caja delimitadora (bounding box) de una lista de coordenadas.

    Parámetros:
        lista_coordenadas (list): Lista de tuplas con formato (latitud, longitud).

    Retorna:
        tuple: (latitud_min, latitud_max, longitud_min, longitud_max)
    """
    latitudes = []
    longitudes = []

    for lat, lon in lista_coordenadas:
        latitudes.append(lat)
        longitudes.append(lon)

    lat_min = min(latitudes)
    lat_max = max(latitudes)
    lon_min = min(longitudes)
    lon_max = max(longitudes)

    return lat_min, lat_max, lon_min, lon_max


# Ejemplo de uso
coordenadas = [
    (4.6097, -74.0817),   # Bogotá
    (6.2442, -75.5812),   # Medellín
    (3.4516, -76.5320),   # Cali
    (10.3910, -75.4794)   # Cartagena
]

bbox = calcular_bbox(coordenadas)
print("Bounding Box:")
print(f"Latitud mínima: {bbox[0]}")
print(f"Latitud máxima: {bbox[1]}")
print(f"Longitud mínima: {bbox[2]}")
print(f"Longitud máxima: {bbox[3]}")