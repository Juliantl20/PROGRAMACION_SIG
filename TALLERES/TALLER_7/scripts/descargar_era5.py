
import cdsapi
from pathlib import Path

# ============================================================
# Descarga ERA5-Land desde Copernicus CDS
# Zona: Departamento del Meta, Colombia
# Variable: Temperatura a 2 metros
# Periodo: Enero de 2024
# Formato: NetCDF
# ============================================================

Path("./data_heavy").mkdir(exist_ok=True)

dataset = "reanalysis-era5-land"

request = {
    "variable": ["2m_temperature"],
    "year": "2024",
    "month": "01",
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "time": [
        "00:00", "01:00", "02:00",
        "03:00", "04:00", "05:00",
        "06:00", "07:00", "08:00",
        "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00",
        "21:00", "22:00", "23:00"
    ],
    "data_format": "netcdf",
    "download_format": "unarchived",

    # Departamento del Meta aproximadamente
    # Orden: [Norte, Oeste, Sur, Este]
    "area": [5, -75, 1.5, -68.5]
}

salida = "./data_heavy/era5_land_meta_t2m_2024_01.nc"

client = cdsapi.Client()
client.retrieve(dataset, request).download(salida)

print(f"Descarga finalizada: {salida}")
