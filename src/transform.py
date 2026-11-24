from datetime import datetime, timezone
import pandas as pd
from src.config import OPENSKY_COLUMNS


def transform_states(payload: dict) -> pd.DataFrame:
    states = payload.get("states") or []
    api_time = payload.get("time", int(datetime.now(timezone.utc).timestamp()))

    if not states:
        return pd.DataFrame(columns=OPENSKY_COLUMNS + ["snapshot_utc"])

    df = pd.DataFrame(states, columns=OPENSKY_COLUMNS)
    df["callsign"] = df["callsign"].fillna("").str.strip()
    df["snapshot_utc"] = datetime.fromtimestamp(api_time, tz=timezone.utc).isoformat()
    return df