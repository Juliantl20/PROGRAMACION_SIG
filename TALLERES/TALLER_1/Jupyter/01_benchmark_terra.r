library(terra)

ruta <- "/home/rstudio/work/PRACTICA_1/VS/S2A_MSIL1C_20180220T105051_N0206_R051_T32ULE_20180221T134037.SAFE/GRANULE/L1C_T32ULE_A013919_20180220T105539/IMG_DATA/T32ULE_20180220T105051_B04.jp2"

t0 <- Sys.time()

r <- rast(ruta)
res <- r * 1.5
m <- global(res, "mean", na.rm = TRUE)[1,1]

t_total <- as.numeric(Sys.time() - t0)

cat("🟤 Terra\n")
cat("Tiempo total:", t_total, "seg\n")
cat("Media:", m, "\n")
