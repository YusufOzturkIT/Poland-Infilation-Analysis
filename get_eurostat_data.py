import json
import requests

# Eurostat API URL for Poland (PL), All-items Inflation Rate (CP00)
# This hits the official 'prc_hicp_manr' dataset (Harmonized Index of Consumer Prices - Annual Rate of Change)
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_manr?lang=en&geo=PL&coicop=CP00"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Connecting to Eurostat API Servers...")
print("-" * 65)

try:
    response = requests.get(url, headers=headers)
    print(f"Eurostat Response Status Code: {response.status_code}")
    
    if response.status_code == 200:
        raw_data = response.json()
        
        # Eurostat packages data using dimensions and a flat index mapping. Let's decode it:
        time_positions = raw_data['dimension']['time']['category']['index']  # Maps "2024M01" -> Position Index
        values_dict = raw_data.get('value', {})  # Maps "Position Index" -> Actual Inflation Rate
        
        parsed_inflation_data = []
        
        print("\nDecoding Eurostat Dataset for Poland (PL)...")
        print("-" * 65)
        
        # Loop through time periods sorted chronologically
        for period_str, index_num in sorted(time_positions.items(), key=lambda item: item[1]):
            # Filter to focus on recent years (2020 - 2026)
            year = int(period_str[:4])
            if 2020 <= year <= 2026:
                month = period_str[5:]
                actual_value = values_dict.get(str(index_num))
                
                if actual_value is not None:
                    record = {
                        "year": year,
                        "month": f"Month {month}",
                        "inflation_rate_yoy": actual_value,
                        "country": "Poland",
                        "source": "Eurostat (HICP)"
                    }
                    parsed_inflation_data.append(record)
        
        print(f"Success! Extracted {len(parsed_inflation_data)} valid monthly inflation rows.")
        
        # Print a quick preview of the last 10 records (most recent data up to 2026)
        print("\n--- RECENT INFLATION DATA PREVIEW ---")
        for row in parsed_inflation_data[-10:]:
            print(f"Year: {row['year']} | {row['month']} -> Inflation (YoY): {row['inflation_rate_yoy']}%")
        print("-" * 65)
        
        # Save the structured goldmine to a local JSON file
        output_file = "poland_eurostat_inflation.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(parsed_inflation_data, f, indent=4, ensure_ascii=False)
            
        print(f"Clean dataset has been successfully saved to '{output_file}'!")
        
    else:
        print(f"Eurostat server rejected request with status code: {response.status_code}")

except Exception as e:
    print(f"An processing error occurred: {str(e)}")

print("-" * 65)