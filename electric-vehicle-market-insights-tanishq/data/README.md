# Data folder

`ev_market_sample.csv` is a bundled 500-row sample used for a quick local demo.

The full `ev_market_train.csv` and optional `ev_market_test.csv` files are excluded from GitHub because of their size. Download them from the [original Kaggle dataset](https://www.kaggle.com/datasets/tharishreddy22/electric-vehicle-market-classification-dataset), then place `ev_market_train.csv` in this folder. The Flask app automatically prefers the full training CSV when it is present.

You can also run `python scripts/download_data.py` from the project root to try downloading the dataset via KaggleHub. If access or authentication prevents the script from working, download the files through the Kaggle website instead.
