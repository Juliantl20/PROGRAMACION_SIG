import numpy as np
import pandas as pd

# 1. Creación del DataFrame
df_estaciones = pd.DataFrame({
    "Estacion": ["Páramo", "Valle", "Costa", "Selva", "Sabana"],
    "Elevacion": [3200, 1500, 15, 200, 2600],
    "Precipitacion": [850.5, 1200.0, np.nan, 3000.5, np.nan]
})

print("DataFrame original:")
print(df_estaciones)

# 2. Imputación con la media de las estaciones válidas
media_precipitacion = df_estaciones["Precipitacion"].mean()
df_estaciones["Precipitacion"] = df_estaciones["Precipitacion"].fillna(media_precipitacion)

print("\nDataFrame con nulos imputados:")
print(df_estaciones)

# 3. Filtro espacial: estaciones con elevación > 1000
estaciones_altas = df_estaciones[df_estaciones["Elevacion"] > 1000].copy()

print("\nEstaciones altas:")
print(estaciones_altas)

# 4. Cálculo final
precipitacion_promedio_altas = estaciones_altas["Precipitacion"].mean()

print(f"\nPrecipitación promedio anual en estaciones altas: {precipitacion_promedio_altas:.2f}")