# Poland Inflation Trend Analysis (2020-2025) 📊

An end-to-end data pipeline project that extracts, processes, and visualizes Poland's annual inflation rate (YoY) over a 6-year period. 

## 💡 Project Background & Problem Solving
The initial phase targeted the Polish Official Statistics (GUS) API. However, due to strict server infrastructure rate-limiting (429 errors), the strategy was pivoted to utilize the **Eurostat API** (Harmonized Index of Consumer Prices - HICP dataset). This adjustment successfully secured a reliable, structured data stream for 72 consecutive months.

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** `requests`, `json` (Data Extraction)
- **Data Manipulation:** `pandas`
- **Data Visualization:** `matplotlib`

## 📁 Repository Structure
```text
├── get_eurostat_data.py        # Fetches raw JSON data from Eurostat API
├── visualize_data.py           # Cleans data and generates the line chart
├── poland_eurostat_inflation.json # Extracted structured dataset
└── poland_inflation_chart.png  # Final high-resolution visualization
