from flask import Flask, render_template, request
from src.data_loader import load_data, filter_data, get_dataset_path
from src.analytics import build_dashboard_payload

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024

@app.route("/", methods=["GET"])
def index():
    df, data_note = load_data()
    filters = {
        "manufacturer": request.args.get("manufacturer", "All"),
        "region": request.args.get("region", "All"),
        "category": request.args.get("category", "All"),
        "year": request.args.get("year", "All"),
    }
    view = filter_data(df, filters)
    payload = build_dashboard_payload(view, df)
    options = {
        "manufacturers": sorted(df["manufacturer"].dropna().astype(str).unique().tolist()) if "manufacturer" in df else [],
        "regions": sorted(df["market_region"].dropna().astype(str).unique().tolist()) if "market_region" in df else [],
        "categories": sorted(df["category"].dropna().astype(str).unique().tolist()) if "category" in df else [],
        "years": sorted([int(x) for x in df["model_year"].dropna().unique()]) if "model_year" in df else [],
    }
    return render_template("index.html", payload=payload, options=options, filters=filters, data_note=data_note)

@app.route("/health")
def health():
    return {"status": "ok", "dataset": str(get_dataset_path())}

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
