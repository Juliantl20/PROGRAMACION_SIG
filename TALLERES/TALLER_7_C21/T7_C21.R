# ============================================================
# T7_C21: Vectores, DataFrames y Comparación entre Lenguajes
# Lenguaje: R
# Autor: Julian Torres
# ============================================================

# ============================================================
# EJERCICIO 1: HIDROLOGÍA DEL RÍO MAGDALENA
# ============================================================

estaciones <- c(
  "Honda",
  "Puerto Berrío",
  "Barrancabermeja",
  "Puerto Wilches",
  "Calamar"
)

caudales_m3s <- c(1500, 2100, 2800, 3200, 4500)

caudal_maximo <- max(caudales_m3s)
caudal_promedio <- mean(caudales_m3s)

# Conversión vectorizada de m3/s a l/s
caudales_ls <- caudales_m3s * 1000

cat("============================================\n")
cat("EJERCICIO 1: HIDROLOGÍA DEL RÍO MAGDALENA\n")
cat("============================================\n\n")

cat("Estaciones:\n")
print(estaciones)

cat("\nCaudales en m3/s:\n")
print(caudales_m3s)

cat("\nCaudal máximo registrado:", caudal_maximo, "m3/s\n")
cat("Caudal promedio:", caudal_promedio, "m3/s\n")

cat("\nCaudales en litros por segundo:\n")
print(caudales_ls)

df_caudales <- data.frame(
  estacion = estaciones,
  caudal_m3s = caudales_m3s,
  caudal_ls = caudales_ls
)

cat("\nTabla de caudales:\n")
print(df_caudales)


# ============================================================
# EJERCICIO 2: CALIDAD DEL AIRE EN BOGOTÁ
# ============================================================

cat("\n\n============================================\n")
cat("EJERCICIO 2: CALIDAD DEL AIRE EN BOGOTÁ\n")
cat("============================================\n\n")

df_aire <- data.frame(
  estacion = c("Carvajal", "Kennedy", "Fontibón", "Suba", "Usaquén"),
  pm25 = c(55, 42, 38, 15, 12)
)

cat("DataFrame original:\n")
print(df_aire)

cat("\nEstructura técnica del DataFrame:\n")
str(df_aire)

cat("\nResumen descriptivo:\n")
print(summary(df_aire))

df_alerta <- df_aire[df_aire$pm25 > 15, ]
df_alerta$estado <- "Crítico"

cat("\nEstaciones con PM2.5 estrictamente mayor a 15:\n")
print(df_alerta)


# ============================================================
# GRÁFICO DE BARRAS
# ============================================================

dir.create("salidas", showWarnings = FALSE)

png(
  filename = "salidas/T7_C21_grafico_pm25_bogota.png",
  width = 900,
  height = 600
)

barplot(
  height = df_aire$pm25,
  names.arg = df_aire$estacion,
  las = 2,
  col = "gray70",
  main = "Niveles diarios de PM2.5 en estaciones de Bogotá",
  xlab = "Estación",
  ylab = "PM2.5"
)

abline(h = 15, lty = 2, lwd = 2)

text(
  x = 4.5,
  y = 17,
  labels = "Límite = 15",
  cex = 0.8
)

dev.off()

cat("\nGráfico guardado en: salidas/T7_C21_grafico_pm25_bogota.png\n")


# ============================================================
# INDEXACIÓN SOLICITADA
# ============================================================

cat("\nTres primeras estaciones del DataFrame:\n")
print(df_aire[1:3, ])

cat("\nScript T7_C21 ejecutado correctamente.\n")
