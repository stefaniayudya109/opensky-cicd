import argparse
import os
from datetime import datetime, timezone
from src.ingest import fetch_opensky_data
from src.transform import transform_states
from src.validate import validate_flight_data
from src.upload_blob import upload_file_to_blob


def run_pipeline(upload: bool = False) -> str:
    payload = fetch_opensky_data()
    df = transform_states(payload)
    validate_flight_data(df)

    os.makedirs("data/processed", exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    csv_filename = f"opensky_flights_{timestamp}.csv"
    local_csv_path = os.path.join("data/processed", csv_filename)
    df.to_csv(local_csv_path, index=False)
    print(f"Berhasil menyimpan {len(df)} baris data penerbangan ke {local_csv_path}")

    if upload:
        blob_path = f"processed/{csv_filename}"
        url = upload_file_to_blob(local_csv_path, blob_path)
        print(f"Berhasil diunggah ke Azure Blob Storage: {url}")

    return local_csv_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--upload", action="store_true", help="Upload hasil CSV ke Azure Blob")
    args = parser.parse_args()
    run_pipeline(upload=args.upload)