# E-Motion Insights — EV Market Intelligence

E-Motion Insights is a web-based electric vehicle (EV) market analytics project built with Flask, Python, Pandas, and Plotly. It provides an interactive dashboard for exploring EV market records, comparing manufacturers and categories, and reviewing selected vehicle and market indicators. A Tableau Public Story is embedded to provide an additional visual exploration experience.

> **Dataset note:** The repository includes a small sample dataset so the application can run immediately. For analysis with the full dataset, download the authorized public dataset from Kaggle and place the training CSV in the `data/` folder. Check the dataset's licence and terms before redistributing it.

## Features

- Interactive dashboard built with Flask and Plotly
- Filters for manufacturer, market region, EV category, and model year (where those fields are present)
- Summary metrics and visual comparisons generated from the selected dataset
- Embedded Tableau Public Story
- Sample-data fallback for quick local testing
- Optional full-dataset support

## Tableau Story

Explore the published Tableau Story: [Electric Vehicle Market Performance & Insights](https://public.tableau.com/shared/KRDCWPSS8?:display_count=n&:origin=viz_share_link).

The embedded Story requires an internet connection and must remain publicly accessible on Tableau Public.

## Dataset

The full dataset is available from the public Kaggle dataset page:

[Electric Vehicle Market Classification Dataset — Kaggle](https://www.kaggle.com/datasets/tharishreddy22/electric-vehicle-market-classification-dataset)

To use the full training dataset:

1. Download the dataset from Kaggle, accepting any applicable terms and signing in if required.
2. Find the training CSV, expected to be named `ev_market_train.csv` (or `EV_market_train.csv`).
3. Place it in this project's `data/` directory.
4. Restart the Flask application.

The loader checks for `data/ev_market_train.csv` and `data/EV_market_train.csv` first, then falls back to `data/ev_market_sample.csv`.

You can also point the app at a CSV in another location by setting the `EV_DATA_PATH` environment variable.

**Important:** The bundled sample contains only a subset of records. Results produced with the sample may differ from results produced with the full dataset.

## Project Structure

```text
.
├── app.py                     # Flask application entry point
├── requirements.txt           # Python dependencies
├── data/
│   ├── README.md              # Dataset setup notes
│   └── ev_market_sample.csv   # Small sample dataset
├── src/
│   ├── data_loader.py         # Dataset loading and filtering
│   └── analytics.py           # Dashboard analytics and chart data
├── templates/
│   └── index.html             # E-Motion Insights web interface
├── static/
│   └── css/styles.css         # Frontend styles
├── scripts/
│   └── download_data.py       # Optional dataset download helper
├── tests/
│   └── test_analytics.py      # Analytics tests
└── docs/
    ├── project_report.md
    └── tableau_guide.md
```

## Requirements

- Python 3.10 or newer recommended
- pip
- Internet access to load the embedded Tableau Story

## Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

Replace the placeholders with the URL and folder name of your repository.

### 2. Create and activate a virtual environment (recommended)

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the app

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. Keep the terminal running while you use the app.

## Run Tests

```bash
python -m pytest
```

## Troubleshooting

- **`ModuleNotFoundError: No module named 'flask'`** — run `python -m pip install -r requirements.txt` using the same Python interpreter you use to run `app.py`.
- **The dashboard uses sample data** — check that the full CSV is named correctly and saved inside `data/`, or set `EV_DATA_PATH` to its path.
- **Tableau does not load** — check your internet connection and confirm that the shared Tableau Story is still public.
- **Charts or filters look empty** — verify that the CSV has the expected columns and that selected filters match values in the dataset.

## Technology Stack

- Python
- Flask
- Pandas
- Plotly
- HTML and CSS
- Tableau Public

## Notes and Limitations

- Dashboard results depend on the dataset and any selected filters.
- Missing values in source fields can affect individual charts and calculations.
- Record counts should not be interpreted as market share unless the dataset's sampling and coverage support that conclusion.
- The full dataset is not included in this repository; obtain it from the linked source and follow its licence and terms.

## License

See the `LICENSE` file in this repository for the project's license. Dataset rights and terms are separate from the code license.


> **Before publishing:** Replace the temporary Tableau Story link with the second project owner’s own published Tableau Story URL. The current link is retained only as a temporary preview.
