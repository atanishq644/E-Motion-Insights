# Electric Vehicle Market Performance & Insights

## Abstract
This project explores an electric-vehicle market dataset using data preparation, descriptive analytics, interactive visualization, and dashboard storytelling. The companion Flask web application displays KPIs and charts for recorded annual sales, vehicle category, manufacturer, market region, range, price, customer ratings, and battery capacity. Tableau Desktop/Public is used to create a dashboard and a multi-point story, then those published views can be embedded into the Flask website.

## Problem statement
Raw vehicle data is difficult to interpret without a consistent view of sales, vehicle specifications, and market dimensions. This project transforms the available fields into visual summaries to support exploration and evidence-based discussion.

## Objectives
- Prepare and validate the EV dataset.
- Compare annual sales units across model years, categories, manufacturers, and regions.
- Summarize range, listed price, battery capacity, and customer ratings.
- Build an interactive web dashboard.
- Create a Tableau dashboard and story based on the same dataset.
- Document reproducible setup steps and limitations.

## Dataset
The supplied archive contains `ev_market_train.csv` and `ev_market_test.csv`. The training file has 37 fields, including vehicle identifiers, manufacturer, model year, manufacturing country, market region, category, battery specifications, range, price, annual sales units, customer rating, and recommended use case. The repository includes a 500-row sample for quick startup. For the full analysis, place the complete training CSV in `data/ev_market_train.csv` or set `EV_DATA_PATH`.

## Methodology
1. Load the CSV and normalize field names.
2. Convert numeric columns to numeric types and model year to an integer-compatible type.
3. Inspect missing values, duplicate IDs, invalid ranges, and category labels before interpreting results.
4. Calculate distinct vehicle record count, sales sum, mean range, mean price, mean rating, and mean battery capacity.
5. Create charts for model-year sales, category sales, top manufacturers, market-region sales, range by battery type, and price versus customer rating.
6. Build the Tableau dashboard and story using the supplied course workflow.
7. Validate charts and explain the dataset's scope and limitations.

## Dashboard components
- Six KPI cards.
- Annual sales by model year.
- Annual sales by category.
- Top ten manufacturers by recorded annual sales.
- Annual sales by market region.
- Range distribution by battery type.
- Listed price versus customer rating.
- Interactive manufacturer, region, category, and model-year filters.

## Interpretation rules
- `annual_sales_units` is summed as supplied by the dataset. Verify its definition before describing it as market-wide sales.
- `vehicle_id` distinct count measures unique IDs in the selected file, not necessarily all EVs in a real-world market.
- The field `manufacturing_country` is not automatically a registration country.
- Correlation or visual association does not establish causation.
- The sample dataset is only for testing the app; final findings must be recalculated on the full dataset.

## Limitations
- Dataset completeness, provenance, and field definitions should be checked against the source.
- The repository's bundled sample has only 500 rows and must not be presented as the full dataset.
- No final numerical findings are asserted here; calculate them from the full file before submitting.
- Tableau Public workbooks are public. Do not upload sensitive data.

## Conclusion template
After the full dataset has been analyzed, summarize three or more numerical findings, the strongest patterns in category/manufacturer/region performance, and one limitation. Avoid inventing values or claiming that the sample represents the whole market.
