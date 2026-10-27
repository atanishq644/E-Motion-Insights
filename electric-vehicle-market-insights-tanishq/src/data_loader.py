from pathlib import Path
import os
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SAMPLE_PATH = DATA_DIR / "ev_market_sample.csv"

def get_dataset_path():
    """Prefer a full local training CSV; otherwise use the included sample."""
    env_path = os.getenv("EV_DATA_PATH")
    candidates = [Path(env_path)] if env_path else []
    candidates += [
        DATA_DIR / "ev_market_train.csv",
        DATA_DIR / "EV_market_train.csv",
        SAMPLE_PATH,
    ]
    for path in candidates:
        if path and path.exists() and path.is_file():
            return path
    return SAMPLE_PATH

def load_data():
    path = get_dataset_path()
    if not path.exists():
        raise FileNotFoundError(
            "No dataset found. Put ev_market_train.csv in data/ or set EV_DATA_PATH."
        )
    df = pd.read_csv(path)
    df.columns = [str(c).strip().lower() for c in df.columns]
    if "vehicle_id" in df.columns:
        df["vehicle_id"] = df["vehicle_id"].astype("string")
    if "model_year" in df.columns:
        df["model_year"] = pd.to_numeric(df["model_year"], errors="coerce").astype("Int64")
    numeric = [
        "battery_capacity_kwh", "battery_cycle_life", "battery_degradation_pct_5yr",
        "range_km", "efficiency_wh_per_km", "motor_power_kw", "torque_nm",
        "top_speed_kmph", "acceleration_0_100_sec", "max_dc_charging_kw",
        "charging_dc_fast_time_min", "charging_ac_time_hr", "weight_kg",
        "cargo_capacity_liters", "price_usd", "insurance_cost_usd_yearly",
        "resale_value_pct_3yr", "co2_saved_tons_per_year", "annual_sales_units",
        "customer_rating", "safety_rating_stars", "num_motors", "num_seats",
    ]
    for col in numeric:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    note = (
        "Using the bundled 500-row sample. Add the full training CSV to data/ "
        "or set EV_DATA_PATH to analyze the full dataset."
        if path.name == "ev_market_sample.csv"
        else f"Loaded dataset: {path.name} ({len(df):,} rows)."
    )
    return df, note

def filter_data(df, filters):
    out = df.copy()
    mapping = {
        "manufacturer": "manufacturer",
        "region": "market_region",
        "category": "category",
    }
    for key, col in mapping.items():
        value = filters.get(key, "All")
        if value and value != "All" and col in out.columns:
            out = out[out[col].astype(str) == str(value)]
    year = filters.get("year", "All")
    if year and year != "All" and "model_year" in out.columns:
        out = out[out["model_year"] == int(year)]
    return out
