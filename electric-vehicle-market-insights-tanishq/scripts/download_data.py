"""Download the Kaggle dataset using kagglehub and copy matching CSVs to data/.

Run:
    python -m pip install -r requirements.txt
    python scripts/download_data.py

Kaggle may require sign-in or API credentials depending on your environment.
"""
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)
DATASET = "tharishreddy22/electric-vehicle-market-classification-dataset"

def main():
    try:
        import kagglehub
    except ImportError:
        print("Missing kagglehub. Run: pip install 'kagglehub[pandas-datasets]'")
        raise SystemExit(1)
    try:
        downloaded = Path(kagglehub.dataset_download(DATASET))
    except Exception as exc:
        print("Dataset download failed. Check internet access and Kaggle authentication.")
        print(f"Details: {exc}")
        raise SystemExit(2)
    csvs = list(downloaded.rglob("*.csv"))
    if not csvs:
        print(f"No CSV files were found under {downloaded}")
        raise SystemExit(3)
    copied = 0
    for source in csvs:
        target = DATA_DIR / source.name
        if target.exists():
            print(f"Keeping existing file: {target}")
            continue
        shutil.copy2(source, target)
        print(f"Copied {source.name} -> {target}")
        copied += 1
    print(f"Done. CSV files available: {len(list(DATA_DIR.glob('*.csv')))} (newly copied: {copied})")
    print("Review the dataset's schema and license before using it in a public repository.")

if __name__ == "__main__":
    main()
