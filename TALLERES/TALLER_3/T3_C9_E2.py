import math

# Función base de distancia
def haversine(lat1, lon1, lat2, lon2, radio=6371.0):
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radio * c


# Clase base del capítulo
class PuntoEspacial:
    def __init__(self, latitud, longitud, nombre="Punto sin nombre"):
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre

    def __str__(self):
        return f"[{self.nombre}] (Lat: {self.latitud}, Lon: {self.longitud})"

    def distancia_hacia(self, otro_punto, radio=6371.0):
        return haversine(
            self.latitud,
            self.longitud,
            otro_punto.latitud,
            otro_punto.longitud,
            radio
        )


# Nueva clase pedida
class RutaGeografica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = []

    def agregar_punto(self, punto):
        self.puntos.append(punto)

    def medir_distancia_total(self):
        distancia_total = 0

        for i in range(len(self.puntos) - 1):
            distancia_total += self.puntos[i].distancia_hacia(self.puntos[i + 1])

        return distancia_total


# Ejemplo de uso
p1 = PuntoEspacial(4.6097, -74.0817, "Bogotá")
p2 = PuntoEspacial(6.2442, -75.5812, "Medellín")
p3 = PuntoEspacial(3.4516, -76.5320, "Cali")

ruta = RutaGeografica("Ruta de los Andes")
ruta.agregar_punto(p1)
ruta.agregar_punto(p2)
ruta.agregar_punto(p3)

print(f"Nombre de la ruta: {ruta.nombre}")
print("Puntos de la ruta:")
for punto in ruta.puntos:
    print(punto)

print(f"Distancia total de la ruta: {ruta.medir_distancia_total():.2f} km")