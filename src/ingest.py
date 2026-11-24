import json
import os
from datetime import datetime, timezone
import requests
from src.config import OPENSKY_API_URL, INDONESIA_BBOX


def fetch_opensky_data(output_dir: str = "data/raw") -> dict:
    os.makedirs(output_dir, exist_ok=True)
    response = requests.get(OPENSKY_API_URL, params=INDONESIA_BBOX, timeout=30)
    response.raise_for_status()
    payload = response.json()

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    raw_path = os.path.join(output_dir, f"opensky_raw_{timestamp}.json")
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    return payload