import pandas as pd
from src.analytics import build_dashboard_payload
from src.data_loader import filter_data

def sample_df():
    return pd.DataFrame({
        "vehicle_id": ["a", "b", "c"],
        "manufacturer": ["Maker A", "Maker B", "Maker A"],
        "market_region": ["Europe", "Asia", "Europe"],
        "category": ["SUV", "Sedan", "SUV"],
        "model_year": [2022, 2023, 2023],
        "annual_sales_units": [100, 200, 150],
        "range_km": [300, 400, 350],
        "price_usd": [30000, 40000, 35000],
        "customer_rating": [4.0, 4.5, 4.2],
        "battery_capacity_kwh": [60, 70, 65],
        "battery_type": ["NMC", "LFP", "NMC"],
        "model_name": ["A1", "B1", "A2"],
    })

def test_payload_kpi_vehicle_count():
    payload = build_dashboard_payload(sample_df())
    assert payload["kpis"][0]["value"] == "3"

def test_filter_data_by_category():
    df = sample_df()
    filtered = filter_data(df, {"category": "SUV", "manufacturer": "All", "region": "All", "year": "All"})
    assert len(filtered) == 2

def test_payload_charts_created():
    payload = build_dashboard_payload(sample_df())
    assert "sales_trend" in payload["charts"]
    assert "manufacturers" in payload["charts"]
