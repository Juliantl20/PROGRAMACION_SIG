# Ejercicio 1: Clasificación iterativa (ciclo for e if-else)

altitudes_fincas = [1350, 1750, 1900, 2300, 1600, 2100]

conteo_especial = 0
conteo_tradicional = 0

fincas_especiales = []
fincas_tradicionales = []

for altitud in altitudes_fincas:
    if altitud >= 1700 and altitud <= 2200:
        fincas_especiales.append(altitud)
        conteo_especial += 1
    else:
        fincas_tradicionales.append(altitud)
        conteo_tradicional += 1

print("=== Reporte de clasificación de fincas ===")
print(f"Fincas aptas para café de especialidad: {conteo_especial}")
print(f"Altitudes clasificadas como especiales: {fincas_especiales}")
print(f"Fincas aptas para café tradicional: {conteo_tradicional}")
print(f"Altitudes clasificadas como tradicionales: {fincas_tradicionales}")