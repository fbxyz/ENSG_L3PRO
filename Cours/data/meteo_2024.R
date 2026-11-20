# Données météo quotidiennes 2024 de 5 villes françaises (cours 2, analyse univariée)
# Source : Open-Meteo, Historical Weather API (réanalyse ERA5), licence CC BY 4.0
# https://open-meteo.com/en/docs/historical-weather-api
# À lancer depuis le dossier Cours/ : source("data/meteo_2024.R")

villes <- data.frame(
  ville = c("Brest", "Paris", "Strasbourg", "Marseille", "Chamonix"),
  lat   = c(48.39, 48.86, 48.58, 43.30, 45.92),
  lon   = c(-4.49, 2.35, 7.75, 5.37, 6.87)
)

url <- paste0(
  "https://archive-api.open-meteo.com/v1/archive?latitude=%s&longitude=%s",
  "&start_date=2024-01-01&end_date=2024-12-31",
  "&daily=temperature_2m_mean,precipitation_sum,cloud_cover_mean",
  "&timezone=Europe%%2FParis&format=csv"
)

meteo <- do.call(rbind, lapply(seq_len(nrow(villes)), function(i) {
  d <- read.csv(sprintf(url, villes$lat[i], villes$lon[i]), skip = 3)
  names(d) <- c("date", "temperature", "precipitation", "nebulosite")
  cbind(ville = villes$ville[i], d)
}))

write.csv(meteo, "data/meteo_2024.csv", row.names = FALSE, fileEncoding = "UTF-8")
