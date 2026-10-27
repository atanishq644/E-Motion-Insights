# E-Motion Insights — Electric Vehicle Market Analytics

E-Motion Insights is an interactive web dashboard for exploring electric-vehicle (EV) market data. Built with Flask, Python, Pandas, Plotly, HTML, and CSS, it presents summary metrics, charts, and filters to help users explore EV records and compare selected manufacturers, categories, regions, and model years where those fields are available. A Tableau Public Story provides an additional interactive view.

> **Data note:** This repository includes a small sample CSV so the application can be tested immediately. The full dataset is not included. Download it from the source linked below and follow the dataset's licence and terms before using or sharing it.

## Features

- Flask-powered web dashboard
- Interactive Plotly charts
- Data filtering and summary metrics based on available dataset fields
- Responsive E-Motion Insights frontend
- Embedded Tableau Public Story
- Sample-data fallback for quick setup
- Optional support for the full training dataset

## Tableau Story

The current preview uses this shared Tableau Story:

[Open the Electric Vehicle Market Performance & Insights Story]([https://public.tableau.com/shared/KRDCWPSS8?:display_count=n&:origin=viz_share_link](https://public.tableau.com/views/E-MotionInsights/EVMarketStory?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link))

The Story requires an internet connection and must remain publicly accessible. **Before final submission, replace this temporary preview with the project owner's own published Tableau Story**, if they have created one.

## Dataset

The public dataset source is:

[Electric Vehicle Market Classification Dataset — Kaggle](https://www.kaggle.com/datasets/tharishreddy22/electric-vehicle-market-classification-dataset)

To use the full dataset:

1. Open the Kaggle page and sign in if required.
2. Download the dataset, subject to its terms and licence.
3. Locate the training CSV, expected to be named `ev_market_train.csv` or `EV_market_train.csv`.
4. Place the CSV in the project's `data/` folder.
5. Restart the Flask application.

The data loader checks for the full training CSV and falls back to `data/ev_market_sample.csv` when the full file is not available. The sample is only a subset, so results may differ from those generated with the full dataset. An alternative file path can be configured with the `EV_DATA_PATH` environment variable.

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── data/
│   ├── README.md
│   └── ev_market_sample.csv
├── src/
│   ├── data_loader.py
│   └── analytics.py
├── scripts/
│   └── download_data.py
├── templates/
│   └── index.html
├── static/
│   └── css/
├── docs/
│   ├── project_report.md
│   └── tableau_guide.md
└── tests/
    └── test_analytics.py
```

## Requirements

- Python 3.10 or newer recommended
- `pip`
- Internet connection to load the embedded Tableau Story

## Run Locally

### 1. Clone your repository

Replace the placeholders with your own GitHub repository URL and folder name:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

Or download the repository ZIP from GitHub and extract it.

### 2. (Recommended) Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. Keep the terminal open while using the site.

## Run Tests

```bash
python -m pytest
```

## Troubleshooting

- **`ModuleNotFoundError: No module named 'flask'`:** Run `python -m pip install -r requirements.txt` using the same Python interpreter that runs `app.py`.
- **The dashboard uses sample data:** Confirm that the full CSV is in `data/` and uses one of the expected filenames, or set `EV_DATA_PATH` to the CSV path.
- **Tableau Story does not load:** Check your internet connection and confirm the Story is public.
- **Charts or filters appear empty:** Confirm the dataset contains the expected columns and that the selected filters match the available values.

## Technology Stack

- Python
- Flask
- Pandas
- Plotly
- HTML and CSS
- Tableau Public

## Notes and Limitations

- Results depend on the dataset loaded and the filters selected.
- Missing or incomplete source values may affect individual charts and calculations.
- Record counts should not be interpreted as market share unless the dataset's sampling and coverage justify that conclusion.
- The dataset's licence and terms are separate from this project's code licence.

## License

See the repository's `LICENSE` file for the code licence. Dataset use is governed separately by the dataset provider's terms.
