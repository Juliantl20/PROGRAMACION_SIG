import numpy as np
import pandas as pd

# DataFrame base de censos + coordenadas
df = pd.DataFrame({
    "Ciudad": ["Bogotá", "Medellín", "Cali", "Barranquilla"],
    "Region": ["Andina", "Andina", "Pacífica", "Caribe"],
    "Poblacion": [7181469, 2529403, 2227642, 1206319],
    "Elevacion": [2640, 1495, 1018, 18],
    "Latitud": [4.7110, 6.2442, 3.4516, 10.9685],
    "Longitud": [-74.0721, -75.5812, -76.5320, -74.7813]
})

def calcular_distancias(df):
    """
    Calcula de forma vectorizada la distancia Haversine desde Bogotá
    hacia todas las ciudades del DataFrame y agrega la columna
    'Distancia_Bogota' en kilómetros.
    """
    # Coordenadas de Bogotá
    lat1 = 4.7110
    lon1 = -74.0721
    radio = 6371.0  # km

    # Convertir columnas completas a radianes
    lat1_rad = np.radians(lat1)
    lon1_rad = np.radians(lon1)

    lat2_rad = np.radians(df["Latitud"])
    lon2_rad = np.radians(df["Longitud"])

    # Fórmula de Haversine vectorizada
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distancias = radio * c

    df = df.copy()
    df["Distancia_Bogota"] = distancias

    return df

df_distancias = calcular_distancias(df)

print(df_distancias[["Ciudad", "Distancia_Bogota"]])