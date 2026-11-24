OPENSKY_API_URL = "https://opensky-network.org/api/states/all"

# Koordinat wilayah udara Indonesia (lamin, lomin, lamax, lomax)
INDONESIA_BBOX = {
    "lamin": -11.0,
    "lomin": 95.0,
    "lamax": 6.0,
    "lomax": 141.0,
}

# 17 kolom standar array state vector dari OpenSky REST API
OPENSKY_COLUMNS = [
    "icao24", "callsign", "origin_country", "time_position",
    "last_contact", "longitude", "latitude", "baro_altitude",
    "on_ground", "velocity", "true_track", "vertical_rate",
    "sensors", "geo_altitude", "squawk", "spi", "position_source"
]