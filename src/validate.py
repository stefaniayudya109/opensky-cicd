import pandas as pd


def validate_flight_data(df: pd.DataFrame) -> bool:
    required_cols = {"icao24", "origin_country", "longitude", "latitude", "snapshot_utc"}
    if not required_cols.issubset(set(df.columns)):
        raise ValueError(f"Kolom wajib tidak lengkap: {required_cols - set(df.columns)}")

    if not df.empty:
        if df["icao24"].isnull().any():
            raise ValueError("Ditemukan nilai null pada identifier pesawat (icao24)")
        valid_lat = df["latitude"].dropna().between(-90, 90).all()
        valid_lon = df["longitude"].dropna().between(-180, 180).all()
        if not (valid_lat and valid_lon):
            raise ValueError("Koordinat latitude/longitude berada di luar batas valid")

    return True