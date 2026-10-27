import pandas as pd
import plotly.express as px
import plotly.io as pio

CHART_CONFIG = {"displayModeBar": True, "responsive": True, "displaylogo": False}

def _chart_json(fig):
    return pio.to_json(fig, validate=True)

def _empty_chart(title):
    fig = px.scatter(title=title)
    fig.add_annotation(text="No data available for this selection", x=0.5, y=0.5,
                       xref="paper", yref="paper", showarrow=False)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return _chart_json(fig)

def _numeric_mean(df, col):
    if col not in df or df[col].dropna().empty:
        return None
    return float(df[col].mean())

def _money(value):
    return "—" if value is None or pd.isna(value) else f"${value:,.0f}"

def _number(value):
    return "—" if value is None or pd.isna(value) else f"{value:,.0f}"

def build_dashboard_payload(df, full_df=None):
    full_df = full_df if full_df is not None else df
    id_col = "vehicle_id" if "vehicle_id" in df else None
    vehicles = int(df[id_col].nunique()) if id_col else int(len(df))
    sales = float(df["annual_sales_units"].sum()) if "annual_sales_units" in df else None
    avg_range = _numeric_mean(df, "range_km")
    avg_price = _numeric_mean(df, "price_usd")
    avg_rating = _numeric_mean(df, "customer_rating")
    avg_battery = _numeric_mean(df, "battery_capacity_kwh")

    kpis = [
        {"label": "Vehicle records", "value": _number(vehicles), "note": "Distinct vehicle IDs where available"},
        {"label": "Annual sales units", "value": _number(sales), "note": "Sum of annual_sales_units in filtered records"},
        {"label": "Average range", "value": f"{avg_range:,.0f} km" if avg_range is not None else "—", "note": "Mean recorded range"},
        {"label": "Average listed price", "value": _money(avg_price), "note": "USD, mean listed price"},
        {"label": "Average customer rating", "value": f"{avg_rating:.2f}/5" if avg_rating is not None else "—", "note": "Mean recorded customer rating"},
        {"label": "Average battery capacity", "value": f"{avg_battery:.1f} kWh" if avg_battery is not None else "—", "note": "Mean recorded battery capacity"},
    ]

    charts = {}
    if "model_year" in df and "annual_sales_units" in df:
        g = df.dropna(subset=["model_year"]).groupby("model_year", as_index=False)["annual_sales_units"].sum()
        fig = px.line(g, x="model_year", y="annual_sales_units", markers=True,
                      title="Annual sales units by model year", labels={"model_year":"Model year","annual_sales_units":"Annual sales units"})
        fig.update_layout(margin=dict(l=20,r=20,t=55,b=20))
        charts["sales_trend"] = _chart_json(fig)
    else:
        charts["sales_trend"] = _empty_chart("Annual sales units by model year")

    if "category" in df:
        g = df.groupby("category", as_index=False).agg(
            vehicle_records=("vehicle_id", "nunique") if "vehicle_id" in df else ("category", "size"),
            annual_sales_units=("annual_sales_units", "sum") if "annual_sales_units" in df else ("category", "size")
        ).sort_values("annual_sales_units", ascending=False)
        fig = px.bar(g, x="category", y="annual_sales_units", title="Annual sales by EV category",
                     labels={"category":"Category","annual_sales_units":"Annual sales units"})
        fig.update_layout(margin=dict(l=20,r=20,t=55,b=90), xaxis_tickangle=-25)
        charts["categories"] = _chart_json(fig)
    else:
        charts["categories"] = _empty_chart("Annual sales by EV category")

    if "manufacturer" in df and "annual_sales_units" in df:
        g = df.groupby("manufacturer", as_index=False)["annual_sales_units"].sum().nlargest(10, "annual_sales_units")
        fig = px.bar(g.sort_values("annual_sales_units"), x="annual_sales_units", y="manufacturer", orientation="h",
                     title="Top 10 manufacturers by recorded annual sales",
                     labels={"manufacturer":"Manufacturer","annual_sales_units":"Annual sales units"})
        fig.update_layout(margin=dict(l=20,r=20,t=55,b=20))
        charts["manufacturers"] = _chart_json(fig)
    else:
        charts["manufacturers"] = _empty_chart("Top manufacturers")

    if "market_region" in df and "annual_sales_units" in df:
        g = df.groupby("market_region", as_index=False)["annual_sales_units"].sum().sort_values("annual_sales_units", ascending=False)
        fig = px.bar(g, x="market_region", y="annual_sales_units", title="Recorded annual sales by market region",
                     labels={"market_region":"Market region","annual_sales_units":"Annual sales units"})
        fig.update_layout(margin=dict(l=20,r=20,t=55,b=70), xaxis_tickangle=-20)
        charts["regions"] = _chart_json(fig)
    else:
        charts["regions"] = _empty_chart("Recorded annual sales by market region")

    if "manufacturing_country" in df and "annual_sales_units" in df:
        g = df.dropna(subset=["manufacturing_country"]).groupby("manufacturing_country", as_index=False)["annual_sales_units"].sum()
        try:
            fig = px.choropleth(g, locations="manufacturing_country", locationmode="country names",
                                color="annual_sales_units", hover_name="manufacturing_country",
                                title="Recorded annual sales by manufacturing country",
                                labels={"manufacturing_country":"Manufacturing country","annual_sales_units":"Annual sales units"})
            fig.update_layout(margin=dict(l=0,r=0,t=55,b=0), geo=dict(showframe=False, showcoastlines=True))
            charts["country_map"] = _chart_json(fig)
        except Exception:
            charts["country_map"] = _empty_chart("Recorded annual sales by manufacturing country")
    else:
        charts["country_map"] = _empty_chart("Recorded annual sales by manufacturing country")

    if "battery_type" in df and "range_km" in df:
        fig = px.box(df, x="battery_type", y="range_km", points="outliers",
                     title="Range distribution by battery type",
                     labels={"battery_type":"Battery type","range_km":"Range (km)"})
        fig.update_layout(margin=dict(l=20,r=20,t=55,b=90), xaxis_tickangle=-20)
        charts["range_battery"] = _chart_json(fig)
    else:
        charts["range_battery"] = _empty_chart("Range distribution by battery type")

    if "price_usd" in df and "customer_rating" in df:
        fig = px.scatter(df, x="price_usd", y="customer_rating", color="category" if "category" in df else None,
                         hover_name="model_name" if "model_name" in df else None,
                         title="Listed price vs customer rating",
                         labels={"price_usd":"Listed price (USD)","customer_rating":"Customer rating"})
        fig.update_layout(margin=dict(l=20,r=20,t=55,b=20))
        charts["price_rating"] = _chart_json(fig)
    else:
        charts["price_rating"] = _empty_chart("Listed price vs customer rating")

    top_maker = "—"
    if "manufacturer" in df and "annual_sales_units" in df and not df.empty:
        maker_sales = df.groupby("manufacturer")["annual_sales_units"].sum()
        if not maker_sales.empty:
            top_maker = str(maker_sales.idxmax())
    top_region = "—"
    if "market_region" in df and "annual_sales_units" in df and not df.empty:
        region_sales = df.groupby("market_region")["annual_sales_units"].sum()
        if not region_sales.empty:
            top_region = str(region_sales.idxmax())

    insights = [
        f"Highest recorded sales manufacturer in the current selection: {top_maker}.",
        f"Highest recorded sales region in the current selection: {top_region}.",
        "Interpret sales totals as sums of the dataset's annual_sales_units field, not verified market-wide sales unless the dataset documentation supports that claim.",
        "Use the filters to compare categories, model years, manufacturers, and regions. Findings may change when filters change."
    ]
    return {
        "kpis": kpis,
        "charts": charts,
        "insights": insights,
        "rows": int(len(df)),
        "dataset_rows": int(len(full_df)),
        "empty": bool(df.empty),
    }
