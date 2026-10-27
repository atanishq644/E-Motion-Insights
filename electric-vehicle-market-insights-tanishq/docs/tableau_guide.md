# Tableau Desktop / Tableau Public Guide

This guide follows the supplied Skill Wallet video transcripts. The videos demonstrate the process rather than supplying a finished workbook, so you must create and publish your own Tableau workbook.

## 1. Connect the dataset
1. Extract `ev_market_train.csv` from the provided ZIP file.
2. Open Tableau Desktop or Tableau Public.
3. Choose **Connect → Text File** for CSV data (use Microsoft Excel only if you have an Excel workbook).
4. Select `ev_market_train.csv`.
5. Confirm that Tableau recognizes the 37 fields and inspect the number of rows.

## 2. Prepare data
- Rename the data source to `EV Market Dataset`.
- Check nulls, duplicates, and the uniqueness of `vehicle_id`.
- Confirm `model_year` and numeric performance fields are numeric.
- Keep decimal precision for fields such as price, battery capacity, range, efficiency, acceleration, charging times, and ratings unless a justified display format is desired.
- Use whole-number display formatting for counts or values where rounding is meaningful; do not unnecessarily overwrite source precision.
- Verify `annual_sales_units` and `customer_rating` are numeric.
- Confirm category labels and geographic fields before creating visualizations.

## 3. Suggested Tableau calculated fields
Use the exact field names in the CSV.

**Vehicle Records**
```tableau
COUNTD([vehicle_id])
```

**Annual Sales Units**
```tableau
SUM([annual_sales_units])
```

**Average Range (km)**
```tableau
AVG([range_km])
```

**Average Listed Price (USD)**
```tableau
AVG([price_usd])
```

**Average Customer Rating**
```tableau
AVG([customer_rating])
```

**Average Battery Capacity (kWh)**
```tableau
AVG([battery_capacity_kwh])
```

## 4. Suggested worksheets
- KPI sheets: Vehicle Records, Annual Sales Units, Average Range, Average Listed Price, Average Customer Rating, Average Battery Capacity.
- Sales trend: `model_year` against `SUM(annual_sales_units)`.
- Category performance: `category` against `SUM(annual_sales_units)`.
- Manufacturer ranking: `manufacturer` against `SUM(annual_sales_units)`; sort descending and use Top 10.
- Region performance: `market_region` against `SUM(annual_sales_units)`.
- Battery/range comparison: `battery_type` and `range_km`.
- Price/rating comparison: `price_usd` vs `customer_rating`.

## 5. Dashboard design
The transcript demonstrates a dashboard with six KPI cards, multiple visualizations, floating objects, borders with a small corner radius, a title, images, and filters. For a maintainable responsive design, prefer tiled containers when possible and use floating objects only when precise positioning is necessary. Add filters for category, manufacturer, and manufacturing country/region if the corresponding fields exist.

Suggested dashboard title: **Electric Vehicle Market Performance & Insights**.

## 6. Tableau Story
Create a Tableau Story with these points:
1. EV market performance at a glance.
2. Understanding EV category distribution.
3. Leading manufacturers by recorded annual sales.
4. Customer rating patterns by category.
5. Manufacturing-country / market-region footprint.
6. Battery performance and range.
7. Key insights and limitations.

Use the views supported by the actual data. The provided dataset includes `manufacturing_country` and `market_region`; it does not necessarily represent country-level vehicle registrations. Label the map/region analysis accurately.

## 7. Publish and embed
1. Sign in to Tableau Public.
2. Open the dashboard and choose **File → Save to Tableau Public As**.
3. Repeat for the Story.
4. Open each published view and choose **Share**.
5. Copy the view URL or embed code.
6. Replace the placeholders in `templates/index.html` with the published Tableau embed code, or add the embed URL as a configurable setting.
7. Test the local Flask page and confirm both views load.

Public workbooks are publicly accessible. Do not publish confidential or personal data.
