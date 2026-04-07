# Ejercicio 2: Monitoreo de sensores (ciclo while y control de flujo)

import random

nivel_alerta = 8.5
max_lecturas = 12
lectura_actual = 0
alerta_inundacion = False

while lectura_actual < max_lecturas:
    nivel_rio = random.uniform(5.0, 9.0)
    lectura_actual += 1

    print(f"Lectura {lectura_actual}: nivel del agua = {nivel_rio:.2f} m")

    if nivel_rio >= nivel_alerta:
        alerta_inundacion = True
        print("¡ALERTA ROJA! Posible desbordamiento.")
        break

if alerta_inundacion == False:
    print("Monitoreo finalizado. Niveles estables.")